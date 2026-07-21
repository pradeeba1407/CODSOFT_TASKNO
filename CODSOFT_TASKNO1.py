# Rule-Based Chatbot

print("🤖 Welcome to Rule-Based Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions based on predefined rules.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")