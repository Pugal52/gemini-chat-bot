import streamlit as st
import google.generativeai as genai


st.title("Vanakam")
genai.configure(api_key="AIzaSyCRflTQm2WJAzaubGWdZkufpzr9BPwUfaY")
text = st.text_input("Enter your query")
model = genai.GenerativeModel('gemini-pro')    
chat = model.start_chat(history=[])    
 
if st.button("Answer"):
 response = chat.send_message(text) 
 st.write(response.text)

