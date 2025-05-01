# Sorting House Game in Python

houses = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

# function to ask questions and get user input
def ask_question(text, options):
    print("\n" + text)
    for key, value in options.items():
        print(f"  {key}) {value['text']}")
    
    while True:
        try:
            answer = int(input("Enter your answer: "))
            if answer in options:
                return answer
            else:
                print("Wrong input. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# dictionary to store questions and their options
questions = [
    {
        "text": "Q1) Do you like Dawn or Dusk?",
        "options": {
            1: {"text": "Dawn", "points": {"Gryffindor": 1, "Ravenclaw": 1}},
            2: {"text": "Dusk", "points": {"Hufflepuff": 1, "Slytherin": 1}}
        }
    },
    {
        "text": "Q2) When I’m dead, I want people to remember me as:",
        "options": {
            1: {"text": "The Good", "points": {"Hufflepuff": 2}},
            2: {"text": "The Great", "points": {"Slytherin": 2}},
            3: {"text": "The Wise", "points": {"Ravenclaw": 2}},
            4: {"text": "The Bold", "points": {"Gryffindor": 2}}
        }
    },
    {
        "text": "Q3) Which kind of instrument most pleases your ear?",
        "options": {
            1: {"text": "The violin", "points": {"Slytherin": 4}},
            2: {"text": "The trumpet", "points": {"Hufflepuff": 4}},
            3: {"text": "The piano", "points": {"Ravenclaw": 4}},
            4: {"text": "The drum", "points": {"Gryffindor": 4}}
        }
    },
    {
        "text": "Q4) Which is your favourite holiday?",
        "options": {
            1: {"text": "Christmas", "points": {"Gryffindor": 1, "Slytherin": 1}},
            2: {"text": "Easter", "points": {"Hufflepuff": 1, "Ravenclaw": 1}},
            3: {"text": "Halloween", "points": {"Slytherin": 1, "Ravenclaw": 1}},
            4: {"text": "New Year", "points": {"Hufflepuff": 1, "Gryffindor": 1}}
        }
    },
    {
        "text": "Q5) Which do you identify with most?",
        "options": {
            1: {"text": "The brave", "points": {"Gryffindor": 3}},
            2: {"text": "The wise", "points": {"Ravenclaw": 3}},
            3: {"text": "The kind", "points": {"Hufflepuff": 3}},
            4: {"text": "The bold", "points": {"Slytherin": 3}}
        }
    },
    {
        "text": "Q6) What is your favorite color?",
        "options": {
            1: {"text": "Red", "points": {"Gryffindor": 2}},
            2: {"text": "Blue", "points": {"Ravenclaw": 2}},
            3: {"text": "Yellow", "points": {"Hufflepuff": 2}},
            4: {"text": "Green", "points": {"Slytherin": 2}}
        }
    },
        
        {
            "text": "Q7) What is your favorite animal?",
            "options": {
                1: {"text": "Lion", "points": {"Gryffindor": 3}},
                2: {"text": "Eagle", "points": {"Ravenclaw": 3}},
                3: {"text": "Badger", "points": {"Hufflepuff": 3}},
                4: {"text": "Snake", "points": {"Slytherin": 3}}
            }
        },
        {
            "text": "Q8) What is your favorite subject?",
            "options": {
                1: {"text": "Defense Against the Dark Arts", "points": {"Gryffindor": 2}},
                2: {"text": "Potions", "points": {"Slytherin": 2}},
                3: {"text": "Herbology", "points": {"Hufflepuff": 2}},
                4: {"text": "Charms", "points": {"Ravenclaw": 2}}
            }
        },
        {
            "text": "Q9) What is your favorite food?",
            "options": {
                1: {"text": "Pizza", "points": {"Slytherin": 3}},
                2: {"text": "Pasta", "points": {"Ravenclaw": 2}},
                3: {"text": "Burger", "points": {"Gryffindor": 1}},
                4: {"text": "Cake", "points": {"Hufflepuff": 3}}
            }
        },
        {
            "text": "Q10) What is your favorite drink?",
            "options": {
                1: {"text": "Butterbeer", "points": {"Gryffindor": 1, "Hufflepuff": 1}},
                2: {"text": "Pumpkin Juice", "points": {"Ravenclaw": 1, "Slytherin": 1}}
            }   

    
        }
]

# dictionary to store user answers
answers = {}

# loop through questions and get user input
for i, q in enumerate(questions, start=1):
    user_choice = ask_question(q["text"], q["options"])
    answers[f"Q{i}"] = user_choice
    # update house scores based on user choice
    for house, points in q["options"][user_choice]["points"].items():
        houses[house] += points

# print final scores for each house
print("\n--- Final Scores ---")
for house, score in houses.items():
    print(f"{house}: {score}")

# determine the winning house
max_score = max(houses.values())
winners = [house for house, score in houses.items() if score == max_score]


print("\n🧙 The Sorting Hat has made its decision...")
for winner in winners:
    print(f"🏆 {winner} 🏆")

print("Welcome to Hogwarts!")

