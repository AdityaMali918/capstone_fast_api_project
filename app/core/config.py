import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.api_key = os.getenv("API_KEY","api_key")
        self.secret_key = os.getenv("SECRET_KEY","secret")
        self.redis_url = os.getenv("REDIS_URL",'redis://')
        self.hash_algorithm = os.getenv("HASH_ALGORITHM",'HS256')
        self.access_token_expiry_minutes = os.getenv("ACCESS_TOKEN_EXPIRY_MINUTES",'30')
        self.model_path = os.getenv("MODEL_PATH",'app/models/model.joblib') 


settings = Settings()