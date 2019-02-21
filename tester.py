from chatterbot.trainers import ListTrainer  # Training chatbot
from chatterbot import ChatBot
import os
import pyfiglet 



chatbot = ChatBot('Test')
trainer= ListTrainer(chatbot)

for _file in os.listdir('files'):
	conv = open('files/' + _file, 'r').readlines()
	trainer.train(conv)
 

result = pyfiglet.figlet_format("Teckzite2K19") 
print(result) 
result = pyfiglet.figlet_format("INNOHACK '19") 
print(result) 
print(" Hi I am TravelBot . I help you to guide and suggest some best tourist spots in AndhraPradesh. Feel free to ask me anything . I'm training myself to be better and help you people" )
result = pyfiglet.figlet_format("TravelBot") 
print(result)

while True:
	message = input('You : ')
	if message.strip() != "bye" :
		reply = chatbot.get_response(message)
		print("Chatbot ::" , reply)
	if message.strip() == "Bye": 
		print("Chatbot :: Bye")
		break