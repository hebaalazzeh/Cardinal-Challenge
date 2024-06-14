
def introduction():
    print("Welcome to the Stanford Trivia Challenge: Cardinal Knowledge!")
    print("Test your knowledge about Stanford University.")
    print("You'll be given a series of questions with multiple choice answers.")
    print("For each question, type the letter of your choice and press Enter.")
    print("Let's see how much you know about Stanford! Good luck!\n")

questions = [
    {
        "question": "When was Stanford University founded?",
        "choices": ["a) 1885", "b) 1890", "c) 1895", "d) 1900"],
        "answer": "a"
    },
    {
        "question": "What is the nickname of Stanford's athletic teams?",
        "choices": ["a) Bears", "b) Cardinal", "c) Ducks", "d) Tigers"],
        "answer": "b"
    },
    {
        "question": "Which of the following is the motto of Stanford University?",
        "choices": [
            "a) Lux et Veritas", 
            "b) Veritas", 
            "c) Die Luft der Freiheit weht", 
            "d) Mens et Manus"
        ],
        "answer": "c"
    },
    {
        "question": "What are Stanford's official colors?",
        "choices": ["a) Blue and Gold", "b) Red and White", "c) Cardinal and White", "d) Green and Yellow"],
        "answer": "c"
    },
    {
        "question": "Who was the first president of Stanford University?",
        "choices": ["a) David Starr Jordan", "b) Jane Stanford", "c) John Hennessy", "d) Donald Kennedy"],
        "answer": "a"
    },
    {
        "question": "In which city is Stanford University located?",
        "choices": ["a) San Francisco", "b) Palo Alto", "c) Berkeley", "d) San Jose"],
        "answer": "b"
    },
    {
        "question": "Which famous technology company was founded by Stanford alumni Larry Page and Sergey Brin?",
        "choices": ["a) Facebook", "b) Microsoft", "c) Google", "d) Apple"],
        "answer": "c"
    },
    {
        "question": "What is the name of Stanford's student newspaper?",
        "choices": ["a) The Daily Californian", "b) The Stanford Daily", "c) The Stanford Review", "d) The Stanford Sun"],
        "answer": "b"
    },
    {
        "question": "Which Stanford alumnus co-founded Nike?",
        "choices": ["a) Bill Gates", "b) Steve Jobs", "c) Phil Knight", "d) Elon Musk"],
        "answer": "c"
    },
    {
        "question": "What is the name of Stanford's primary library?",
        "choices": ["a) Widener Library", "b) Green Library", "c) Doe Library", "d) Bancroft Library"],
        "answer": "b"
    }
]

def display_question(question_dict):
    print(question_dict["question"])
    for choice in question_dict["choices"]:
        print(choice)

def get_player_answer():
    answer = input("Your answer: ")
    return answer.lower()

def check_answer(player_answer, correct_answer):
    return player_answer == correct_answer

def play_game():
    score = 0
    for question in questions:
        display_question(question)
        player_answer = get_player_answer()
        if check_answer(player_answer, question["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    return score

def end_game_summary(score, total_questions):
    print(f"Game Over! You scored {score} out of {total_questions}.\n")

def main():
    introduction()
    score = play_game()
    end_game_summary(score, len(questions))

if __name__ == "__main__":
    main()
