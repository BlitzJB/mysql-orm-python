class ConnectionOptions:
    def __init__(self, **kwargs) -> None:
        self.host = kwargs.get('host', 'localhost')
        self.user = kwargs.get('user', 'root')
        self.password = kwargs.get('password', '')
        self.database_name = ...
        self.__dict__.update(kwargs)
