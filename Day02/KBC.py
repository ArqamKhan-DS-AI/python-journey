def ask_question(question: list[str], correct_answer: int, prize: int) -> int:
    """Asks a single question. Returns prize money if correct, 0 if wrong, -1 if quit."""
    for text in question:
        print(text)
        
    try:
        answer = int(input("Enter the correct answer (numbers 1-4) or press 0 to quit: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return 0 # Treat invalid input as a wrong answer for now
        
    if answer == 0:
        print("You chose to quit.")
        return -1 # Signal to quit
    elif answer == correct_answer:
        print(f"Correct! You won {prize}.")
        return prize
    else:
        print(f"Wrong answer! The correct answer was {correct_answer}.")
        return 0 # No prize for wrong answer

def play_game() -> None:
    print("\nWelcome to KBC!")
    
    # 1. Define the questions and prizes (using lists)
    q1 = ["\nWhich country hosted FIFA in 2022?", "1. UAE", "2. USA", "3. Qatar", "4. France"]
    q2 = ["\nWhat is the capital of Indonesia?", "1. Jakarta", "2. Java", "3. Kuala Lumpur", "4. Singapore"]
    q3 = ["\nWhich religion is the fastest growing?", "1. Christianity", "2. Islam", "3. Hinduism", "4. Buddhism"]
    q4 = ["\nWhat is the capital of Canada?", "1. Ottawa", "2. Toronto", "3. El Salvador", "4. Chicago"]
    
    # 2. Put them in a list of tuples so we can loop through them easily
    questions = [
        (q1, 3, 5000),   # (question list, correct answer number, prize money)
        (q2, 1, 10000),
        (q3, 2, 20000),
        (q4, 1, 40000)
    ]
    
    total_score = 0
    
    # 3. The loop
    for q, correct_ans, prize_money in questions:
        result = ask_question(q, correct_ans, prize_money)
        
        if result == -1:
            print("You quit the game.")
            break # Stop the loop
        elif result == 0:
            print(f"Game over! You go home with {total_score}.")
            print(f"The correct answer was option {correct_ans}.")
            break # Stop the loop
        else:
            total_score += result
            print(f"Current total score: {total_score}")
            
    print(f"\nThanks for playing! Final score: {total_score}")

def main() -> None:
    play_game()

if __name__ == "__main__":
    main()