
from typing import Type


class DataType: 
    @property
    def name(self):
        return self.name
    
    @property
    def length(self):
        if self.length: return self.length
        raise TypeError("Length is not defined")


class Text(DataType): 
    def __init__(self) -> None:
        self.name = 'TEXT'
        
class Varchar(DataType):
    def __init__(self, length: int) -> None:
        self.name = 'VARCHAR'
        self.length = length

class Char(DataType): 
    def __init__(self, length: int) -> None:
        self.name = 'CHAR'
        self.length = length

class Int(DataType): 
    def __init__(self) -> None:
        self.name = 'INT'

class Float(DataType): ...

class Date(DataType): ...

class Boolean(DataType): ...
