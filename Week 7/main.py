# main.py
from agent import run_agent

def chat():
    print("🧠 Stateful LangGraph Agent")
    print("Type 'exit' to quit")
    print("Type '/load <session_id>' to resume a session\n")

    session_id = None

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Load existing session
        if user_input.startswith("/load"):
            try:
                session_id = user_input.split(" ")[1]
                print(f"✅ Loaded session: {session_id}\n")
            except:
                print("❌ Usage: /load <session_id>\n")
            continue

        # Run agent
        result = run_agent(user_input, session_id)

        session_id = result["session_id"]
        print(f"Bot: {result['response']}\n")


if __name__ == "__main__":
    chat()