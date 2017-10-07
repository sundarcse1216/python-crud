import interface
import abc


class InsertRecords:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def insert_record(self):
        pass
