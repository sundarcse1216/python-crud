import interface
import abc


class UpdateRecords:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update_records(self, value, cause):
        pass
