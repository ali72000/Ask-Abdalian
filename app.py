import streamlit as st
import openai

st.set_page_config(page_title="AskAbdalian 🤖", layout="centered")
st.title("AskAbdalian 🤖")
st.markdown("Ask anything, powered by OpenAI!")

# ✅ Correct way to access key
openai.api_key = st.secrets["openai"]["openai_api_key"]

user_question = st.text_input("What's your question?")

if st.button("Get Answer") and user_question:
    try:
        with st.spinner("Thinking..."):
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for Cadet College Hasanabdal students."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
