from abc import ABC, abstractmethod

class MessageBroker(ABC):
    @abstractmethod
    def execute(self, message):
        raise NotImplementedError
