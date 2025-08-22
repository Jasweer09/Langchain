#Model (Azure OpenAI)
from langchain_openai import AzureChatOpenAI
# Prompt Template
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
#Response
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
# Load .env
load_dotenv(dotenv_path=r"C:\Jasweer\my_project\Langchain\.env")

# Azure OpenAI credentials
AZURE_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

if not AZURE_KEY or not AZURE_ENDPOINT or not AZURE_DEPLOYMENT:
    raise ValueError("Azure OpenAI environment variables not set properly")

# LangChain Tracking
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = "ChatBot"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("You are helpful assistante. Please response to the user queries"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    
)

## Streamlit framework

st.title('Langchain Demo with OPENAI API')
input_text = st.text_input("Search the topic u want")

#call AzureOpenAI LLM
llm = AzureChatOpenAI(
    deployment_name=AZURE_DEPLOYMENT,
    openai_api_key=AZURE_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    openai_api_version="2025-01-01-preview"
)

#output
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))