import streamlit as st
import google.generativeai as genai


if "GENAI_API_KEY" in st.secrets:
    GENAI_API_KEY = st.secrets["GENAI_API_KEY"]
else:
    GENAI_API_KEY = "SUA_CHAVE_AQUI"

genai.configure(api_key=GENAI_API_KEY)

st.title("🤖 Minha IA Privada")
st.caption("Interface rodando no Moto E20 / Código na Nuvem")


model = genai.GenerativeModel("gemini-1.5-flash")


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])


for message in st.session_state.chat.history:
    
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)


if prompt := st.chat_input("O que quer saber hoje?"):
    
    with st.chat_message("user"):
        st.markdown(prompt)

    
    response = st.session_state.chat.send_message(prompt)

    
    with st.chat_message("assistant"):
        st.markdown(response.text)
