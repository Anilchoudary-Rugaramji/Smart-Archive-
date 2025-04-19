import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Smart Archive"
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")


settings = Settings()
