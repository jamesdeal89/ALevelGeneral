import random
import time
import sortSearch

print(sortSearch.Sort.bubble())
# chatbot, class which contains some functions and holds information in attributes
class Chatbot():
    # initialize our class object
    # here we pass parameters into this function:
    # 'self', the class we're in, and 'name', with a default value
    def __init__(self, name = ""):
        # the '.' shows that 'personality' is a part of the 'Chatbot' class
        # self refers to the class code is in, without having to write 'Chatbot.personality'
        self.personality = random.choice(["aggressive","dismissive","suprised","chipper"])
        if name == "":
            self.name = random.choice(["James","Mary","Robert","Patricia","John","Jennifer","Michael","Linda","William","Elizabeth","David","Barbara","Richard","Susan","Joseph","Jessica","Thomas","Sarah","Charles","Karen","Christopher","Nancy","Daniel","Lisa","Matthew","Betty","Anthony","Margaret","Mark","Sandra","Donald","Ashley","Steven","Kimberly","Paul","Emily","Andrew","Donna","Joshua","Michelle","Kenneth","Dorothy","Kevin","Carol","Brian","Amanda","George","Melissa","Edward","Deborah","Ronald","Stephanie","Timothy","Rebecca","Jason","Sharon","Jeffrey","Laura","Ryan","Cynthia","Jacob","Kathleen","Gary","Amy","Nicholas","Shirley","Eric","Angela","Jonathan","Helen","Stephen","Anna","Larry","Brenda","Justin","Pamela","Scott","Nicole","Brandon","Emma","Benjamin","Samantha","Samuel","Katherine","Gregory","Christine","Frank","Debra","Alexander","Rachel","Raymond","Catherine","Patrick","Carolyn","Jack","Janet","Dennis","Ruth","Jerry","Maria","Tyler","Heather","Aaron","Diane","Jose","Virginia","Adam","Julie","Henry","Joyce","Nathan","Victoria","Douglas","Olivia","Zachary","Kelly","Peter","Christina","Kyle","Lauren","Walter","Joan","Ethan","Evelyn","Jeremy","Judith","Harold","Megan","Keith","Cheryl","Christian","Andrea","Roger","Hannah","Noah","Martha","Gerald","Jacqueline","Carl","Frances","Terry","Gloria","Sean","Ann","Austin","Teresa","Arthur","Kathryn","Lawrence","Sara","Jesse","Janice","Dylan","Jean","Bryan","Alice","Joe","Madison","Jordan","Doris","Billy","Abigail","Bruce","Julia","Albert","Judy","Willie","Grace","Gabriel","Denise","Logan","Amber","Alan","Marilyn","Juan","Beverly","Wayne","Danielle","Roy","Theresa","Ralph","Sophia","Randy","Marie","Eugene","Diana","Vincent","Brittany","Russell","Natalie","Elijah","Isabella","Louis","Charlotte","Bobby","Rose","Philip","Alexis","Johnny","Kayla"])
        else:
            # here 'self.name' instead of just 'name' means we ensure we're referencing the 'name' of the class
            # ,not just any other name in the program
            self.name = name
        self.greetings = ["hello","hi","howdy","aloha","hi-ya","hey","wassup","hi","good evening","what's up?","how's it going?","welcome","buenos dias","hiya","sup","yo","bonjour","good morrow","shalom"]
    # main function
    def chat(self):
        self.intro()
    # function to ask question
    # function to find out information
    # function for slow print character by character from chatbot
    def slowPrint(self, toPrint):
        for character in toPrint:
            time.sleep(random.uniform(0.02,0.15))
            print(character,end='')
        print()
    
    def chat(self):
        print(random.choice(self.greetings, " I'm ", self.name))
        self.person = "What should I address you as?:"


# example notes 
bob = Chatbot # creating an instance of the class 'Chatbot'
alice = Chatbot # creating a second instance of the class 'Chatbot'


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
