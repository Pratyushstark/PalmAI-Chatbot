#Install necessary dependencies
import streamlit as st
import pprint
import google.generativeai as palm
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
from gtts import gTTS
from io import BytesIO
import tempfile

#Mention your api key here provided to you by https://makersuite.google.com/app
palm.configure(st.secrets['palm-api-key'])
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

#Title of application
st.title("A chatbot with the capabilities of PalmAI 🤖")

#Setting up the prompt area of app
prompt = st.text_input("Enter your question here..")
if prompt:
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800
)
    st.write(completion.result)
else:
    st.write("type something and hit enter...")
