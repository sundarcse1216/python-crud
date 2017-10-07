import abc


class Commons:
    abc.__metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def finalized(self):
        pass
