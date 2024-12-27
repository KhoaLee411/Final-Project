from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

# Lấy API key
api_key = os.getenv("API_KEY")

# Sử dụng API key
print(f"Your API key is: {api_key}")