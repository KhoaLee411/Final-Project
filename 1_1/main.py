from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load the environment variables
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Bạn là trợ lý ảo AI sẽ dịch các từ đơn trong Tiếng Anh thành Tiếng Việt một cách chính xác nhất.\nCác từ tôi chat dưới đây bạn hãy dịch nó.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Tuyệt vời! Tôi đã sẵn sàng. Bạn cứ đưa từ tiếng Anh, tôi sẽ cố gắng dịch sang tiếng Việt chính xác nhất có thể.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hello",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Xin chào\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Phenomenon",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hiện tượng\n",
      ],
    },
  ]
)

response = chat_session.send_message("Hello")

print(response.text)