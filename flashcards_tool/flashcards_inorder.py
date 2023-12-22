import json

def display_question(question_data):
    print("\nQuestion:", question_data['question'])
    options = question_data['incorrect'][:]
    options.append(question_data['answer'])
    options = sorted(options)  # Shuffle the options
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    return options.index(question_data['answer']) + 1

def main():
    with open('flashcards.json', 'r') as file:
        flashcards = json.load(file)

    for card_id, card_data in flashcards.items():
        correct_answer = display_question(card_data)
        user_answer = None
        while user_answer is None:
            try:
                user_input = input("\nEnter your answer (Enter the option number): ")
                user_answer = int(user_input)
                if user_answer < 1 or user_answer > 5:
                    print("Please enter a valid option number.")
                    user_answer = None
            except ValueError:
                print("Please enter a valid option number.")
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. {card_data['answer']}")

        if card_id != str(len(flashcards) - 1):
            next_card = input("Press 'y' to continue to the next question: ")
            if next_card.lower() != 'y':
                break

if __name__ == "__main__":
    main()
