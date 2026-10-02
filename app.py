import os 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
human_msg = HumanMessage("Explain what a dictionary is in Python with an example.")
system_msg = SystemMessage("You are a Python tutor who explains concepts with simple code examples.")
messages = [system_msg, human_msg]

model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    api_key=api_key
)

response = model.invoke(messages)
print(response.content)
