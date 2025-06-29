import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only the first time)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"(hi|hello|hey)",
        ["Hello!", "Hey there!", "Hi, how can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.", "You can call me NLP-Bot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How can I assist you today?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it", "It's okay"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Glad to hear it!"]
    ],
    [
        r"(.*) help (.*)",
        ["I can assist you. Please tell me your query in detail."]
    ],
    [
        r"(.*) your creator?",
        ["I was created by a Python developer using NLTK."]
    ],
    [
        r"quit",
        ["Bye! Have a nice day.", "Goodbye, take care!"]
    ],
    [
        r"(.*)",
        ["I’m sorry, I didn’t understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("Hi, I'm your NLP Chatbot. Type 'quit' to exit.")
chatbot.converse()
