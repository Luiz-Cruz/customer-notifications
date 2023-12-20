from abc import ABC, abstractmethod

class NotificationRepository(ABC):
    @abstractmethod
    def save(self, message):
        raise NotImplementedError
    