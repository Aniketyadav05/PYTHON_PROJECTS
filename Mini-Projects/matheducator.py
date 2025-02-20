import random
import time
operators = ["+","-","*"]
min_operand = 3
max_operand = 12
total_problems = 10
def generate_problem():
    left= random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) +" "+ operator + " "+ str(right)
    answer= eval(expr)
    return expr , answer

wrong= 0 
input("\t\tPRESS ENTER TO START")
print("\t\t-------------------------------")

start_time = time.time()

for i in range(total_problems):
    expr , answer = generate_problem()
    while True:
        guess = input("\t\tPROBLEM NO."+ str(i+1)+ ":"+ expr + "=")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("\t\t------------------------------------------")
print("\t\tNICE WORK! YOU FINISHED IN ", total_time, "seconds!")