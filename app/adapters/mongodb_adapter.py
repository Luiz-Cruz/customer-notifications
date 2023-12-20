import os
from pymongo import MongoClient
from loguru import logger

from app.ports.user_repository import UserRepository

class MongoDBAdapter(UserRepository):
    def __init__(self):
        self.client = MongoClient(os.environ.get('MONGO_URI'))
        self.db = self.client[os.environ.get('MONGO_DB')] 

    def find_by_id(self, user_id: str) -> dict:
        logger.info(f"Finding user {user_id}")
        user = self.db.users.find_one({"_id": user_id})
        logger.info(f"User {user_id} found: {user}")
        return user