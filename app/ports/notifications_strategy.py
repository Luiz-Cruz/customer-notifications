from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    @abstractmethod
    def execute(self, message):
        raise NotImplementedError
    