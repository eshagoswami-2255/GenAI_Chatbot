api_key = "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"
from groq import Groq

from groq import Groq
import streamlit as st 
from dotenv import load_dotenv
import os


llm = Groq(api_key=api_key)

st.subheader("Groq QnA Bot")
query = st.chat_input(
    placeholder="Ask me anything..."
)

if query:
    st.chat_message("user").markdown(query)

    res = llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role":"user",
                "content":query
            }
        ]
)


    finalAnswer = res.choices[0].message.content
    st.chat_message("ai").markdown(finalAnswer)
