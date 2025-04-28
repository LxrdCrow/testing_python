import random

last_answer = None  # Variable to store the previous answer
answers = {  # Dictionary with answers for each random number
    1: "Definitely yes",
    2: "You can count on it",
    3: "Without a doubt",
    4: "Reply hazy, try again",
    5: "Ask again later",
    6: "Better not tell you now",
    7: "My sources say no",
    8: "Outlook not so good",
    9: "Very doubtful",
    10: "Destiny will decide"
}

while True:  # The loop continues until the user decides to stop
    # Ask a question
    question = input("Ask a question: ")
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Map the random number to the answer
    answer = answers[random_number]

    # If the answer is the same as the previous one, generate another number
    while answer == last_answer:
        random_number = random.randint(1, 10)
        answer = answers[random_number]

    # Store the answer for the next cycle
    last_answer = answer
    # Provide the answer to the question
    print(f"Magic 8 Ball: {answer}\n")

    # Ask if the user wants to continue
    while True:  # This loop continues until a valid response is given
        continue_question = input("Do you want to ask another question? (yes/no): ")
        
        # If the user answers "no", exit the loop
        if continue_question.lower() == 'no':  
            print("Goodbye!")
            break
        # If the user answers "yes", continue the loop
        elif continue_question.lower() == 'yes':
            print("Feel free to ask more questions!")
            break
        # Invalid response, ask again
        else:
            print("Invalid answer, please reply with 'yes' or 'no'.")
    
    # If the user answered 'no', the outer loop breaks
    if continue_question.lower() == 'no':
        break
