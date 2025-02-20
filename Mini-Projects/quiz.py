quiz = {
    "question1":{
        "question": "what is the capital of india?",
        "answer": "new delhi",
    },
    "question2":{
        "question": "what is the name of the prime minister of india",
        "answer": "narendra modi",
    },
    "question3":{
        "question": "what is the capital of rajasthan?",
        "answer": "JAIPUR",
    },
    "question4":{
        "question": "what is the capital of HARYANA?",
        "answer": "CHANDIGARH",
    },
    "question5":{
        "question": "what is the capital of ITALY?",
        "answer": "ROME",
    },
    "question6":{
        "question": "what is the capital of FRANCE?",
        "answer": "PARIS",
    },#WE CAN ALSO ADD MORE AND MORE QUESTIONS TO MAKE IT A BETTER AND LONGER QUIZ GAME
    
}

score = 0 
for key, value in quiz.items():
    print(value['question'])
    answer = input("ANSWER>>")

    if answer.lower() == value['answer'].lower():
        print("CORRECT ANSWER\n")
        score = score +1
        print(f"YOUR SCORE IS {score}\n")

    else:
        print("WRONG ANSWER")
        print(f"THE CORRECT ANSWER IS:{value['answer']}\n")


print(f"YOU GOT {score} / OUT OF 6 QUESTIONS")
print(f"YOUR PERCENTAGE IS {int(score/6*100)}%")