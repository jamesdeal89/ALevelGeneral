name = input("what is your name?:")
print("hello" + name)

while True:
    print("ask me anything")
    question = input(":")
    if "capital" in question.lower():
        if "france" in question.lower():
            print("F")
        if "spain" in question.lower():
            print("S")