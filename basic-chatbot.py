
def simple_chatbot():
    print("🤖 Chatbot: Hello! I'm your simple chatbot.")
    print("Type something like 'hello', 'how are you', or 'bye'. Type 'bye' to exit.\n")

    while True:
        # Take user input and convert to lowercase for uniformity
        user_input = input("You: ").lower()

        # Match responses based on input
        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
simple_chatbot()
