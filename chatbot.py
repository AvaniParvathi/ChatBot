import streamlit as st #deploying platform for py projects
import google.generativeai as genai
API_KEY = "AIzaSyC5zeiEWIscklFBeKY1fkt-2bNGMOCaC10"

genai.configure(api_key=API_KEY)   #for access to our work
model = genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
  st.session_state.chat = model.start_chat(history=[])  #to continue chatting in single session

st.title("Chatbot - Your companion")
st.write("This is a chatbot for you")

if "messages" not in st.session_state:  #adding messages to history
  st.session_state.messages = [] 

for message in st.session_state.messages:
  with st.chat_message(message["role"]):  #who uses the bot
    st.markdown(message["content"])  #also displays the content

if prompt := st.chat_input("Hello.. How can i help?!"):
  st.session_state.messages.append({"role": "user", "content": prompt})  #appends our que to prompt
  with st.chat_message("user"):  #sends gen ai bot that que is asked
    st.markdown(prompt)
  response = st.session_state.chat.send_message(prompt)  #reply given by api and stores in response

  st.session_state.messages.append({"role": "assistant", "content": response.text})  
  with st.chat_message("assistant"):
    st.markdown(response.text)
