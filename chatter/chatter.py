# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging

def getTrainingList():
    conversation_file = open("conversations.txt","r", encoding="utf-8-sig")
    conversations = conversation_file.read()
    training_list = conversations.splitlines(keepends=False)

    return training_list




# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'Artie',
    trainer='chatterbot.trainers.ListTrainer'
)

print("Chatterbot training")
training_list = getTrainingList()
print(training_list)
# Start by training our bot with the english corpus data
chatbot.train(training_list)
print("Chatterbot finished training")