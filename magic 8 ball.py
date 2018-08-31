import random

name=input("Please type your name")
print("Welcome %s" % name)
my_list=["yes", "i don't think so", "try again", "doesnt look good bud", "maybe"]

while True:
    question = input("What is your question?")
    print(random.choice(my_list))
    if question == "stop":
        break

    else:
        sys.exit
    
    

