# Title: Sagittariusbot
# Author: Sagi
# Date: September 27 2021

# Create a bot that asks the user 5 questions about me. Every time the user says yes, the points increase. Every time the user says no, the points decrease.

# Introduce the bot
print("Oh, hey there! My name is Sagittariusbot. I'll be quizzing you today about how well you know Sagi!")
print()

# Ask what the user's name is
print("What's your name?")
# Get the user's name and STORE it somewhere
username = input()
print()
print(f"Welcome {username}!")
print()

score = 0
score == 0
# Ask the user Question 1.
answer1 = input("When is Sagi's birthday? \na. June 4 \nb. December 17 \nc. November 27 \nd. February 10 \nAnswer: ")
if answer1 == "c" or answer1 == "November 27":
    score += 1
    print("Correct")
    print("score: ", score)
    print("\n")
else:
    score = 0
    print("Incorrect! The answer was November 27.")
    print("Score: ", score)
    print("\n")
print()

# Ask the user Question 2.
answer2 = input("Where was Sagi born? \na. Canada \nb. Israel \nc. Russia \nd. Ukraine \nAnswer: ")
if answer2 == "b" or answer2 == "Israel":
    score += 1
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was Israel.")
    print("score: ", score)
    print("\n")
print()

# Ask the user Question 3.
answer3 = input("What is Sagi's favourite sport? \na. swimming \nb. soccer \nc. hockey \nd. volleyball \nAnswer: ")
if answer3 == "a" or answer3 == "swimming":
    score = 0
    score += 2
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was swimming.")
    print("score: ", score)
    print("\n")
print()

# Ask the user Question 4.
answer4 = input("What is Sagi's favourite number?: \na. 37 \nb. 46 \nc. 73 \nd. 11 \nAnswer: ")
if answer4 == "a" or answer4 == "37":
    score = 0
    score += 3
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was 37.")
    print("score: ", score)
    print("\n")
print()

# Ask the user Question 5
answer5 = input("The team Sagi is competing or coaching for our school this year for is: \na. Volleyball \nb. Soccer \nc. Swim team \nd. Swimming assistant Coach \nAnswer: ")
if answer5 == "d" or answer5 == "Swimming assistant Coach":
    score = 0
    score += 4
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was Swimming assistant Coach.")
    print("score: ", score)
    print("\n")
print()

print("Congratulations! You completed the quizzo about Sagi")
print("Here are your results:")
print(f"Total Score: {(score /5) * 100}%")









