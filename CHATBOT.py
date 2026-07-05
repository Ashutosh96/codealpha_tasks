# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    # Normalize input (lowercase for easy matching)
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("🤖 Chatbot is ready! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        
        if user_input.lower() == "bye":
            break

# Run the chatbot
run_chatbot()
