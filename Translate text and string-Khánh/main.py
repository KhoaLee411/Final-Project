
import google.generativeai as genai 
import os 
import re
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key = api_key)
model = genai.GenerativeModel('gemini-pro')
def is_vietnamese(text):
    vietnamese_chars = r'[àáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]'
    return bool(re.search(vietnamese_chars,text))
# Hàm dịch một từ bằng Gemini
def translate_single_gemini(text,target_language='Vietnamese'):
    if is_vietnamese(text):
        print( text )
        return text  
    
    try:
        prompt= f"translate the following text into {target_language}: '{text}' "
        response = model.generate_content(prompt)
        print( response.text.strip()) 
        return response.text.strip()    
    except Exception as e : 
        print(f"error during translation with Gemini: {e}")
        return None
# Hàm dịch nhiều từ bằng Gemini
def translate_multiple_gemini(texts , target_language="Vietnamese"):
    if isinstance(texts,str):
        texts = [texts]
    translations =[]
    for text in texts:
        translations.append(translate_single_gemini(text, target_language))
    return translations

# Thử nghiệm: 
if __name__ == "__main__":

 translate_single_gemini('Aircraft')
 translate_single_gemini('máy tính')
    
 texts_to_translate= ["AI means Artificial Intelligence"]
 translate_multiple_gemini(texts_to_translate)
 translate_multiple_gemini('The airplane just tookoff')
    
    