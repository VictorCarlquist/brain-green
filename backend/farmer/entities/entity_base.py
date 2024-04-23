import abc


class EntityBaseInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'listItem') and 
                callable(subclass.listItem))


    @abc.abstractmethod
    def listItems(self, filter: dict):
        """Load in the data set"""
        raise NotImplementedError
