from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import streamlit as st
from  dotenv  import load_dotenv
load_dotenv()
import os
model=HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

chat=ChatHuggingFace(llm=model)
st.header("Ask me anything")
user_input=st.text_input("Enter prompt")
result=chat.invoke(user_input)

if st.button("GO"):
    st.text(result.content)

