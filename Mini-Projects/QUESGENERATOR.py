from tkinter import *
from tkinter import messagebox
import random
from QSS import * #YOU CAN FIND THIS FILE IN THE SAME RESPIRATORY 😁

def close():
    user_input =messagebox.askyesno("DO YOU WANT TO END?","JARHE HO?")
    if user_input ==1:
        messagebox.showinfo("THANK YOU!!","BOIII BOIII!!")
        start.destroy()
    elif user_input == 0:
        messagebox.showinfo("THANK YOU!!","TUSSI NHI JARHE <3")

def first():
    start.destroy()
    global choice
    choice = "python"
    main()
    
def second():
    start.destroy()
   
    global choice
    choice = "cpp"
    main()
    
def main():
        
        def info():
            T.delete(1.0,END)
            T.insert( END,"""THIS PROJECT IS MADE BY ANIKET YADAV!! MY CONTACT INFORMATIONS :=
                EMAIL ID :- yadavaniket7611@gmail.com
                LINKEDIN :- I WILL INSERT IT LATER ALAS ARHA H BRO!!""")

        def roll(*args):
            T.yview(*args)

        def update():
            global click_count
            
            click_count+=1
            if click_count>1:
                T.delete(1.0,END)
                solutionb.config(state=DISABLED)
                click_count = 0
            else:
                solutionb.config(state=NORMAL)
                T.insert(END,random_key)
                click_count = 2
 
        def question():
            
            global random_value,random_key
            if choice == "python":
                random_key = random.choice(list(python.keys()))
                random_value = python[random_key]
            elif choice =="cpp":
                random_key = random.choice(list(cpp.keys()))
                random_value = cpp[random_key]
            
            
            
        def combine_qb():
            question()
            update()

        def solution():
            T.insert(END,f"\n\n{random_value}")
            solutionb.config(state=DISABLED)
        
        window = Tk()
        window.title("PYTHON RANDOM QUESTIONS")
        window.geometry("1000x600")
        window.minsize(1000,600)
        window.maxsize(1000,600)
        

        name = Label(window,text="RANDOM QUESTION GENERATOR",bg="black",fg = "aqua",font =("verdana",25,"bold",))
        name.pack(side=TOP)
        window.config(bg="black")
        
        slider = Scrollbar(window, orient=VERTICAL,command= roll,bg="black")
        slider.pack(side=RIGHT,fill = Y)

        T = Text(window, height = 25, width = 100,font=("cascadia code", 12, 'bold'),bg ="black",fg="#347890")
        T.pack(pady=(25,0))

        questionb = Button(window, text ="QUESTION", width= 25,bg="black",fg="white", font=("verdana",8,"bold"),activebackground="white",activeforeground="red",command = combine_qb )
        questionb.pack(pady=(0,0))
        solutionb = Button(window,text = "SOLUTION", width= 25 , bg ="black", fg="white", font=("verdana",8,"bold"),activebackground="white",activeforeground="#943c09", command = solution,state=DISABLED)
        solutionb.pack()

        hehe = Menu(window)
        hehe.add_cascade(label="INFORMATION",command=info)
        window.config(menu=hehe)
        window.mainloop()
        
start = Tk()
start.config(bg= "black")
start.title("RANDOM QUESTION GENRATOR")
start.geometry("300x370")
start.minsize(300,370)
start.maxsize(300,370)
click_count = 0

wel = Label(start, text= "WELCOME",bg="black",fg = "aqua",font =("verdana",25,"bold"))
wel.pack(pady=(100,0))

choose = Label(start, text= "CHOOSE UR \nPREFERED\n LANGUAGE",bg="black",fg = "aqua",font =("verdana",10,"bold"))
choose.pack()

pyb = Button(start,text = "PYTHON",width= 25,bg="black",fg="white", font=("hack",8,"bold"),activebackground="white",activeforeground="red",command= first,relief="ridge")
pyb.pack()

cb = Button(start,text = "C++",width= 25,bg="black",fg="white", font=("hack",8,"bold"),activebackground="white",activeforeground="red",command= second,relief="ridge")
cb.pack()

exitb = Button(start,text = "exit",width= 25,bg="black",fg="white", font=("hack",8,"bold"),activebackground="white",activeforeground="red",command= close,relief="ridge")
exitb.pack(pady=(0,100))

start.mainloop()
