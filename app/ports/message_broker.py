from abc import ABC, abstractmethod

class MessageBroker(ABC):
    @abstractmethod
    def send_to_queue(self, message):
        pass
