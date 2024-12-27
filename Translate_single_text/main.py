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

def translate_single_text(json):
  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          f"Bạn là trợ lý AI sẽ dịch một từ đơn trong ngôn ngữ Tiếng Anh (en) thành ngôn ngữ {json['dest_language']} một cách chính xác nhất. Các từ tôi chat với bạn ở dưới đây bạn hãy dịch nó cho tôi. Ví dụ: Hello bạn sẽ trả lời là \"Xin chào\"",
        ],
      },
      {
        "role": "model",
        "parts": [
          "Tuyệt vời! Tôi hiểu rồi. Bạn cứ đưa từ tiếng Anh, tôi sẽ cố gắng dịch sang tiếng Việt một cách chính xác nhất có thể. Rất vui được giúp bạn!\n",
        ],
      },
    ]
  )

  response = chat_session.send_message(json['text'])

  # Loại bỏ ký tự \n trong response.text
  cleaned_response = response.text.replace('\n', '')

  print(cleaned_response)

json_1 = {
 'text': 'Hello',
 'dest_language': 'vi'
 }

translate_single_text(json_1)