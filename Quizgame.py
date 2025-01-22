

Questions=("1. Which country has the largest population?","2.What is the capital of India?",
          "3.Which comapny has the highest turnover?","4.What is the capital of Maharashtra ",
          "5.Which one is the largest mammal on earth")
Options=(("1. A.India","1. B.USA","1. C.China","1. D.Russia"),("2. A.Nagpur","2. B.Jaipur","2. C.Bangalore","2. D.New Delhi"),
         ("3. A.Alibaba","3. B.Tesla","3. C.Lambo","3. D.Reliance"),
         ("4. A.Mumbai","4. B.Nagpur","4. C.Bangalore","4. D.New Delhi"),
         ("5. A.Blue Whale","5. Elephant","5. C.Lion","5. D.Tiger"))

Answers=("C","D","B","A","A")


print("Hey Everyone Lets start the quiz!!!!!!!!")

count=1
correct=0
total=len(Answers)
while count<5:
    for que in range(len(Questions)):
        print(Questions[que])
        print(Options[que])
        ans=input("Provide your ans for above question with four options: ")
        print("--------------------------------------------------------------")
        if ans==Answers[que]:
            print("Correct!! you got this ")
            correct+=1
        else:
            print("Incorrect, You need more study")
        print("--------------------------------------------------------------")
        count += 1

score=(correct/total)*100


print("*******************************************************")
print("***************Results Are Here !!!!*******************")
print("*******************************************************")
print()
print(f"You scored {score}%")