def quiz_app():
    questions = [
        "What is the keyword to define a function in python",
        "Which data type is used to store True or False?"
        "What symbol is used to start a comment in python",
        "Which fuction is used to get input from the user"
        "What is the index of the first element in python list"
    ]
    answers = [
        'def',
        'bool',
        '#'
        'input',
        '0'
    ]
    score = 0
    for q,a in zip(questions,answers):
        user_ans = input(f"{q}\n your Answer:")
        if user_ans.lower() == a.lower():
            print("correct")
            score += 1
        else:
            print(f"Wrong! Correct Answer: {a}\n")
    print(f"your final score: {score}/{len(questions)}")

    #Bonus: Feedback
    if score == len(questions):
        print("Feedback: Excellent! you are a python pro") 
    elif score >= len(questions) * 0.6:
        print("Feedback: Good job! Keep Practicing.")      
    else:
        print("Feedback: Try Again! practice makes perfect.")    

    again = input("\n Do you want to play again? (Yes/no):").strip().lower()
    if again == "yes":
        quiz_app()
    else:
        print("Thanks for playing! Bye!" )


quiz_app()
