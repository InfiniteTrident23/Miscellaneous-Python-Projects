# Will require Chatterbot library installation.
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.en')

while True:
    query = input(">>> ")
    print(chatbot.get_response(query))
    if "exit" in query:
        break
