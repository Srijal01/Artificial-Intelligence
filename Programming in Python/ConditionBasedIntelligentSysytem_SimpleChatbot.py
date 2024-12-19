# Chatbot with personalized interaction and more responses
def chatbot_response(user_input, user_name=None):
    user_input = user_input.lower()

    if user_name:
        greeting = f"Hello, {user_name}!"
    else:
        greeting = "Hello!"

    if "hello" in user_input or "hi" in user_input:
        return f"{greeting} How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing well, thanks for asking!"
    elif "weather" in user_input:
        return "Today's weather is sunny with a temperature of 25°C."
    elif "your name" in user_input:
        return "I'm a simple chatbot. I don't have a name, but you can call me Chatbot!"
    elif "bye" in user_input:
        return "Goodbye! It was nice talking to you!"
    elif "set a reminder" in user_input:
        return "I don't have a reminder feature yet, but I will let you know when I can help with that!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "thanks" in user_input:
        return f"You're welcome, {user_name if user_name else 'friend'}!"
    else:
        return "Sorry, I didn't understand that. Could you ask something else?"

# Simple interaction with user asking for their name
def chat():
    print("Welcome to the Chatbot!")
    name = input("What's your name? ").strip()
    print(f"Nice to meet you, {name}!")

    while True:
        user_input = input(f"{name}: ")
        response = chatbot_response(user_input, user_name=name)
        print(f"Bot: {response}")

        if "bye" in user_input.lower():
            break

# Start chat
chat()
