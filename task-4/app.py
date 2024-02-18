import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you', ["I'm good, thanks!", "I'm doing well, how about you?"]),
    (r'i\'m (.*)', ["Hi {}, nice to meet you!", "Hey {}, how can I help you?"]),
    (r'(.*) your name?', ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]),
    (r'quit', ["Bye! Take care.", "Goodbye, have a great day!"]),
]

chatbot = Chat(patterns, reflections)

def chat_with_bot():
    print("Hello! I'm ChatBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat_with_bot()
