from enum import Enum

class BaseEnum(str, Enum):
    @classmethod
    @property
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]
    
    @classmethod
    @property
    def records(cls):
        return {choice.name: choice.value for choice in cls}
    
    @classmethod
    @property
    def reverse_records(cls):
        return {choice.value: choice.name for choice in cls}
    
    @classmethod
    def get(cls, key, default=None):
        return cls.records.get(key, default)
    
    @classmethod
    def get_key(cls, value, default=None):
        return cls.reverse_records.get(value, default)