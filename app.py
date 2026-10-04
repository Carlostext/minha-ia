import streamlit as st
import google.generativeai as genai

GENAI_API_KEY = "SUA_NOVA_CHAVE_AQUI"
genai.configure(api_key=GENAI_API_KEY)

st.title("Minha IA privada")
st.caption("Interface rodando no Moto E20 / Código na nuvem")

model = genai.GenerativeModel("grmini-1.5-flash")

if "messages" not in st.session_state:
   st.session_state.messages = []

chat = model.start_chat(
    history=[
        {"role":"user" if m["role"] == "user" else "model", "parts": [m["content"]]}
        for m in st.session_state.messages
    ]
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("O que quer saber hoje?"):

   with st.chat_message("user"):
       st.markdown(prompt)
   st.session_state.messages.append({"role": "user", "content": prompt})

   response = chat.send_message(prompt)

   with str.chat_message("assistant"):
       st.markdown(response.text)
   st.session_state.messages.append({"role": "assistant", "content": response
