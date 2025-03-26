import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.",],
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You ?",],
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",],
    ],
    [
        r"i am fine",
        ["Great to hear that", "Glad to hear that",],
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ",],
    ],
]

def chatbot():
    print("Hi, I'm a chatbot created using NLTK. Type quit to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()