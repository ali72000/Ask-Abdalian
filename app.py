import streamlit as st
import openai

# Set your API key securely
client = openai.OpenAI(api_key=st.secrets["openai_api_key"])

st.set_page_config(page_title="AskAbdalian 🤖", layout="centered")
st.title("AskAbdalian 🤖")
st.markdown("Ask anything, powered by OpenAI!")

user_question = st.text_input("What's your question?")

if st.button("Get Answer") and user_question:
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for Cadet College Hasanabdal."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response.choices[0].message.content
            st.success(answer)
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
