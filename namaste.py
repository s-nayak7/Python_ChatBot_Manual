
import datetime
import time
#Returns a greeting message based on the current time of day.
name=input("Please enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 11:
    print("Good Morning, " + name + "!")
elif 11 <= presentHour < 17:
    print("Good Afternoon, " + name + "!")
elif 17 <= presentHour < 20:
    print("Good Evening, " + name + "!")
else:
    print("Good Night, " + name + "!")


print("hello! welcome dear cuties")
print("You can ask me anything you want")
# dictionary of responses for the chat bot
responses = {
    "hello": "Hello there! How can I help you today?",
    "how are you?": "I am fine, thank you for asking",
    "what is your name?": "My name is Friend",
    "what is your favorite color?": "My favorite color is blue",
    "what is your favorite food?": "My favorite food is pizza"
}

# function of get response of chat bot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower().strip()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "Sorry, I don't understand your question. Can you please rephrase it?"

while True:
    userInput = input("please ask your question: ")
    if "bye" in userInput.lower():
        print("Goodbye! Have a great day!")
        break
# reply the user question by calling the function getResponseOfBot
    reply = getResponseOfBot(userInput)
    print("Bot response:", reply)
