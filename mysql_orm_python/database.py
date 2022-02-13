import mysql.connector as mysql
from .connectionoptions import ConnectionOptions
from .model import Model
from .utils import get_all_models, duplicates

from typing import Dict, Sequence

class Database:
    def __init__(self, connection_options: dict | ConnectionOptions) -> None:
        self.connection = self.connect(connection_options)
        self.con_options = connection_options
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS `{}`".format(connection_options.database_name))
        self.cursor.execute("USE `{}`".format(connection_options.database_name))
        self.__load_models()
    
    def connect(self, connection_options: dict | ConnectionOptions) -> mysql.connection:
        if isinstance(connection_options, ConnectionOptions):
            connection_options = {'host': connection_options.host, 'user': connection_options.user, 'password': connection_options.password}
        return mysql.connect(**connection_options)

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()
        
    def __load_models(self) -> Sequence[Model]:
        models = get_all_models()
        dups = duplicates(models)
        if dups: raise TypeError("Duplicate model names: {}".format(dups))
        self.__models = self.__models_map(models)
        for model in models:
            self.cursor.execute(model._build_create_query())
        
    def __models_map(self, models) -> dict:
            return {model.__name__: model for model in models}
    
    @property
    def models(self) -> Dict[str, Model]:
        return self.__models
