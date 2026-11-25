import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# التأكد من جلب المفتاح بشكل صحيح
my_secret_api_key= os.getenv("NVIDIA_API_KEY")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=my_secret_api_key # ضع المفتاح مباشرة هنا للتجربة
)


st.title("ENG OSAMA CHATBOT : HOW CAN I HELP YOU")
user_question = st.text_input("اكتب سؤالك هنا")

if st.button("إرسال"):
    if user_question:
        response = client.chat.completions.create(
            model="moonshotai/kimi-k3.1-pro",
            messages=[{"role": "user", "content": user_question}],
            stream=True
        )
        st.write_stream(response)