# main.py
from agent import run_agent

print("Groq Chatbot Ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = run_agent(user_input)
    print("Bot:", response)