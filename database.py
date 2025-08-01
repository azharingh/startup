from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("DATABASE_URL")

client = MongoClient(uri)

db = client["item_db"]

collection = db["item_collection"]
user_collection = db["user_collection"]
