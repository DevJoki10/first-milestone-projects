# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# 1.  Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# 2. Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# 3. Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# 4. Display Results:
# At the end of the quiz, display the user's total score.

# Sample Questions:
# 1. What is 2 + 2?
# a) 3
# b) 4
# c) 5
# d) 6
# 2. What color is the sky on a clear day?
# a) Red
# b) Blue
# c) Green
# d) Yellow
# 3. How many legs does a spider have?
# a) 6
# b) 7
# c) 8
# d) 9
# 4. What sound does a cow make?
# a) Meow
# b) Bark
# c) Moo
# d) Quack
# 5. What is the opposite of 'hot'?
# a) Warm
# b) Cold
# c) Cool
# d) Boiling

def run_quiz():
    score = 0
    questions = [
        {"question": "1. What is 2 + 2? (a) 3 (b) 4 (c) 5", "answer": "b"},
        {"question": "2. What color is the sky on a clear day? a) Red  b) Blue c) Green d) Yellow", "answer": "b"},
        {"question": "3. How many legs does a spider have? a) 6 b) 7 c) 8 d) 9", "answer": "c"},
        {"question": "4. What sound does a cow make? a) Meow b) Bark c) Moo d) Quack", "answer": "c"},
        {"question": "5. What is the opposite of 'hot'? a) Warm b) Cold c) Cool d) Boiling", "answer": "b"}
    ]

    for question in questions:
        print(question["question"])  
        
       
        while True:
            user_answer = input( "Your answer: ").lower()  
            if user_answer not in ["a", "b", "c", "d"]:
                print("Invalid option! Please choose a, b, c, or d.")
            else:
                break  
        
        if user_answer == question["answer"]:
            score += 1

    return f"Final Score: {score} out of {len(questions)}"
print(run_quiz())
