import datetime   #date and time user using this bot
import time

name = input("Nimo: Hello and welcome!\nMay I know your name please?: ")
time.sleep(2)
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Nimo: Good morning!", name)
elif 11 <= presentHour <= 17:
    print("Nimo: Good afternoon!", name)
elif 17 <= presentHour <= 20:
    print("Nimo: Good evening!", name)
else:
    print("Nimo: Good night!", name)
                
time.sleep(2)     
       
print("I'm Nimo, your personal AI chatbot.")
print("Ask me basic stuff, or tap 'bye' to exit.")

#Chatbot Memory Creation [dictionary of responses]
responses = {
    "hello" : "Hi, how are you doing today?",
    "how are you" : "I'm fine thank you. What about you?",
    "i'm fine too" : "Cool!",
    "who are you?" : "My name is Nimo and I am your personal chat assistant.",
    "i'm happy" : "Glad to hear that, I'm happy for you too.",
    "bye" : "Ok bye! Have a nice day!"
}

#Method/Function to get response of Chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:    #If user says hello
            return responses[eachKey]
        
    return "Sorry, I don't know that yet. I will learn it soon."    

#User input
while True:
    userInput = input("Your message: ")
    time.sleep(2)
    reply = getResponseOfBot(userInput)
    print("Nimo: ", reply)
    
    if "bye" in userInput.lower():
        break