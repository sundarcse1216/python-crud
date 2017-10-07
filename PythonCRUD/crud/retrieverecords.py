import abc


class RetrieveRecords:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_all_records(self):
        pass
