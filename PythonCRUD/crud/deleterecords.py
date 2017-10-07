import abc


class DeleteRecords:
    abc.__metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def delete_records(self, cause):
        pass
