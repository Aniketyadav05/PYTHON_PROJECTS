
python = {
        """Write a program that returns the sum of the even numbers of a list?
        FOR TEST CASE: take a list of 5 elments and give input as [2,4,5,9,4] your answer should be 10!""": """n = int(input("enter the no of elements you want in your lists"))
    pp= []
    sum = 0
    for  i in range(n):
        p = int(input("enter"))

        pp.append(p)

    for i in range(n):
        if pp[i]%2==0:
            sum =sum + pp[i]
        else:
            pass
    print(sum)
    """,
    """write a program to reverse a string?
    FOR TEST CASE : input = hello world , Output should be :dlrow olleh""":"""pp = input("ENTER A STRING")
    print(pp[::-1])""",
    "WRITE A PROGRAM FOR A GUESS THE NO GAME":"""
import random

count = 1
 
print("WELCOME TO THE GAME")
print("ENTER THE RANGE IN WHICH YOU WANT TO GUESS THE NUMBER")
start = int(input("ENTER THE STARTING"))
end = int(input("ENTER THE ENDING"))
RN = random.randint(start, end)

 
while (1):

    guess = int(input("GUESS THE NO"))
    if (RN == guess):
        print("GOOD")
        print(f"TURNS YOU TOOK TO GUESS THE NUMBER ",count)
        break
    else:
        print("guess again!")
        choice = input("WANT TO GUESS AGAIN OR TAKE A HINT ")
        if(choice == "guess"):
            pass
        elif(choice == "hint"):
            if(RN%2==0):
                print("THE NO IS EVEN")
            else:
                print("THE NO IS ODD")
        else:
            print("ENTER A VALID CHOICE")
    count+=1

""",
"WRITE A PROGRAM FOR A HANGMAN GAME":"""import random
words = ["lemon", "apple", "banana","laptop", "gupta", "suggest", "guest", "python","random","systum","hangman","think","let","eat","paper","maths","sky","corona",
         "instagram", "moment", "loneliness","flowers"]

word = random.choice(words)

name = input("ENTER YOUR NAME ")
age = int(input("ENTER YOUR AGE "))
if age>=10:
    print(F"WELCOME {name} TO THE HANGMAN GAME")
    choice = input("DOU YOU WANT TO PLAY THE GAME ")

    if choice == "yes":
        length = len(word)
        
        
        for i in word:
            print(i + ' _ '*(length-1), end =' ')
            break
        j = 2
        count = 0  
        g = 1
        while(1):
            
            guess = input(f"ENTER YOUR GUESS FOR THE {j} LETTER ")
            if j<length:
            
                if guess == word[g]:
                    x = i + " " +guess +((length - j)* " _ ")
                    i= i+ " " +guess
                    print(x)
                    j = j+1
                    g = g+1
                elif guess is not  word:
                    print("TRY AGAIN")
                count+=1
                
            elif j == length:
                print("you won ")
                print(f"IT TOOK ONLY {count} TRIES TO GUESS THE WORD")
                break
    elif choice == "no":
        print("JAA JAA CHAL!!")
    else:
        print("NO HI LIKHNA SIKHLE")
elif age<10:
    print("YOU SHOULD BE OLDER THAN 10 TO PLAY THIS GAME YOU CHILD!")

else:
    print("AWW!!!! SOME ERROR OCCURED TRY AGAIN WITH CORRECT ENTRIES")
"""

    }
cpp = {
        "WAP TO FIND FACTORIAL OF A NO":"""#include<stdio.h>
void findfact(int, long int*);
int main()
{
	long int fact;
	int num1;
	scanf("%d",&num1);
	findfact(num1, &fact);
	printf("THE FACTORIAL IS %d is: %ld\n",num1, fact );
	return 0;
	
}
void findfact(int n, long int*f)
{
	int i;
	*f = 1;
	for(i=1;i<=n;i++)
	{
		*f=*f*i;
	}
}
""",
"WAP TO FIND FACTORIAL USING RECURSSIVE FUNCTION":"""#include<stdio.h> 
int factorial(int); 
int main() 
{ 
int n=5; 
long int f; 
f = factorial(n); 
printf("%d! = %ld\n", n, f); 
return 0; 
} 
int factorial(int n) 
{ 
if (n == 0) 
return 1; 
else 
return(n * factorial(n-1)); 
} 
""",
"WAP TO SHOW THE INHERITANCE WORKS ":"""#include<iostream>
using namespace std;
class hello {
	public:
		int a =20;
		int b = 10;
		
};
class hello2
{
	public:
		int aa =20;
		int bb = 10;
		
};
int main(){
	hello s1;
	hello2 s2;
	cout<<s1.a<<endl;
	cout<<s1.b<<endl;
	cout<<s2.aa<<endl;
	cout<<s2.bb<<endl;
}""",
"WAP TO FIND SUM OF ALL THE NUMBERS TILL n USING RECURSSIVE FUNCTION":"""#include<iostream>
using namespace std;

int sum(int k){
	if (k>0)
	{
		return k+sum(k-1);
		
	}
	else{
		return 0;
		
	}
}
	
	
int main()
{
	int result = sum(10);
	cout<<result;
	return 0;
}"""
    }