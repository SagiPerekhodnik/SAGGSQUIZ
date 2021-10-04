# Title: Sagittariusbot
# Author: Sagi
# Date: September 27 2021

from rich import print
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

# Ask the user Question 1.
answer1 = input("When is Sagi's birthday? \na. June 4 \nb. December 17 \nc. November 27 \nd. February 10 \nAnswer: ")
if answer1 == "c" or answer1 == "November 27":
    score = 0
    score += 1
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was Israel.")
    print("score: ", score)
    print("\n")
print()


for question in questions = [
["What is the colour of the sun?"]
]

# Fo each question, print it out and ask the user to answer
    for question in questions:

# Ask the user Question 2.
answer2 = input("Where was Sagi born? \na. Canada \nb. Israel \nc. Russia \nd. Ukraine \nAnswer: ")
if answer2 == "b" or answer2 == "Israel":
    score == 0
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
if answer3 == "b" or answer3 == "Israel":
    score = 0
    score += 1
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was swimming.")
    print("score: ", score)
    print("\n")
print()

# Ask the user Question 4.
answer4 = input(
    "Calculate this math question to determine Sagi's favourite number: (27+11)*74/76=?") \na.  \nb.Israel \nc.Russia \nd.Ukraine \nAnswer: ")
if answer1 == "b" or answer1 == "Israel":
    score = 0
    score += 1
    print("Correct")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer was Israel.")
    print("score: ", score)
    print("\n")
print()

# Ask a list of questions
list_of_questions = ["Did you eat? ", "Did you study? ", "Did you do your laundry? ", "Did you call your grandma? ",
                     "Did you read today? "]

answerYes = 0.0
answerMaybe = 0.0
answerNo = 0.0

for i in list_of_questions:

    answer = input(i).strip(",. !?''").lower()

    if answer == "yes":
        answerYes += 3
    elif answer == "i don't know":
        answerMaybe += 2
    elif answer == "no":
        answerNo += 1

# Calculate their score
Answer_yes_percentage = answerYes / 15.0 * 100
Answer_maybe_percentage = answerMaybe / 10.0 * 100
Answer_no_percentage = answerNo / 5.0 * 100

print(f"Yes percentage: {round(Answer_yes_percentage, 1)}%")
print(f"Maybe percentage: {round(Answer_maybe_percentage, 1)}%")
print(f"No percentage: {round(Answer_no_percentage, 1)}%")








