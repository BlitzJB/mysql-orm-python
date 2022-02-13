from typing import get_type_hints

BLACKLISTED = [] # Class attributes that are to not be created like table cols

class Model:
    def __init__(self):
        print('this triggered')
        print(self.__build_create_query())
        
    def _build_create_query(self):
        hints = get_type_hints(self.__class__)
        query = f"""
            CREATE TABLE IF NOT EXISTS `{self.__class__.__name__}` (
                {', '.join(
                    [
                        f'{k} {v.name}'
                        for k,v in hints.items() 
                        if k not in BLACKLISTED
                    ]
                )}
            )
        """
        return query
        
        
# class Varchar(Model):
#     name = 'VARCHAR'
#     def __init__(self, length: int) -> None:
#         #self.name = 'VARCHAR'
#         self.length = length
# 
# class Int(Model):
#     name = 'INT'
#     
# class Text(Model):
#     name: Varchar(length=255)
#     id: Int
#     def __init__(self) -> None:
#         print('this triggered')
#         super().__init__()
    