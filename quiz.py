import random


question = {"what is option one? ": {"a": True, "b": False, "c": False, "d": False},
 "what is option two? " : {"a": False, "b": True, "c": False, "d": False},
 "wich is c? " : {"a": False, "b": False, "c": True, "d": False},
 "what is option b? " : {"a": False, "b": True, "c": False, "d": False},
 "wich is b? " : {"a": False, "b": True, "c": False, "d": False},
 "what is option four? " : {"a": False, "b": False, "c": False, "d": True},
  "wich is a? " : {"a": True, "b": False, "c": False, "d": False},
 "what is option a? " : {"a": True, "b": False, "c": False, "d": False},
 "what is option three? " : {"a": False, "b": False, "c": True, "d": False},
 "what is option c? " : {"a": False, "b": False, "c": True, "d": False},
 }

def exam(username):
    counter = 0
    number = 0
    while counter < 5:
        exam = random.choice(list(question.keys()))
        print(exam)
        test = question[exam].keys()
        print(list(test))
        answer = input("enter answer(a,b,c,d): ")
        result = question[exam][answer]
        if result == True:
            number += 1
        question.pop(exam)
                
        counter += 1

    print(f"your number is {number}")
    q = open("number.txt", "a")
    num = q.write(f"{username} number is {number}")
    q.close()

