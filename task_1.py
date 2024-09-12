from datetime import datetime
greeting=["hi","hello","Good morning","hey"]
personal=["how old are you","how are you"]
def chatbot_response(message):
    if message in greeting:
        return message + " how can i help you"
    elif message in personal:
        return "I'm just a bot, but I'm here to assist you!"
    elif "date" in message:
        date=datetime.now()
        formatted_datetime = date.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime
    elif "thank" in message:
        return "You are welcome.Any other questions"
    else:
        return "I'm sorry,I didn't understand that"
    
def chat():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()