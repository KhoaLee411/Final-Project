from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY_KHANH")
print("Hello world", api_key)