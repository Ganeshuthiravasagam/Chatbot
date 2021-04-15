from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Unagi',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)


 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there 🙋🏽‍♂‍ ",
    "What's your name?",
    "I'm Unagi🤟🏽",
    "How you doing?",
    "I'm dude. How are you?",
    "I’m fine buddy",
    "That’s good to hear……",
    "Who created you?",
    "Ganesh uthiravasagam ✨",
    "Do you have any surname?",
    "Nope 🙅🏽‍♂‍",
    "Will you marry me?",
    "Sorry, I'm in a relationship 🙂",
    "How are you doing?",
    "I'm doing great 🤩",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 
