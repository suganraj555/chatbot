from random import randint
def greet_random():
    greetings=['hi','hello','vannakam','howdy']
    return greetings[randint(0,len(greetings)-1)]


'''chatbot.py'''
greetings = greet_random()
qm = ['quit','bye','exit']
print(greetings,"iam jarvis, what is your query? if you want to quit ,type quit")
while True:
    msg = input()
    if msg in qm:
        break
    elif "add" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x+y)
    elif "mul" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x*y)
    elif "sub" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x-y)
    elif "div" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x/y)
    elif "square" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        print(x**2)

   
    
