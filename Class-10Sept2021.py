import random

name = input("what is your name?:")
print("hello" + name)

while True:
    print("ask me anything!")
    question = input(":").lower()
    if "capital" in question:
        if "france" in question:
            print("F")
        elif "spain" in question:
            print("S")
        else:
            print("I don't know that capital.")
    elif "cia" in question:
        print("I'm not at liberty to say...")
        print("How about I ask you some questions now?")
        break
    else:
        print("I don't understand.")

questionBank = ["how are you?:", 
                "are you wealthy?:",
                "what is your location?:"
                "what is your occupation?:"
                "Am I your friend?:"
                "Am I your soulmate?:"
                "What did you eat earlier?"]
while True:
    ans = input(random.choice(questionBank))
