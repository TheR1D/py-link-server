import os
from config import database
from model import Link

if os.path.exists("test.db"):
    os.remove("test.db")

database.create_all()

