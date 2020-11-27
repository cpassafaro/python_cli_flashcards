import psycopg2
from main import FlashCards 

conn = psycopg2.connect(
    database='flashcards', user='postgres', password='', host='localhost', port=5432
)

conn.autocommit = True


#pull easy information
cursor = conn.cursor()
# cursor.execute(insert)
# result = cursor.fetchall()
# print(result)

#game into
def game_intro():
    print('Welcome to Trivia!')
    createorplay = input('Are you here to play or create new trivia cards? p for play or c for create:')
    if(createorplay == 'p'):
        launch_game()
    elif(createorplay == 'c'):
        create_cards()
    else:
        print('Please enter a valid response p for play or c for create')
        game_intro()


#create gameplay
def launch_game():
    choose_difficulty = input('Choose easy, medium, or hard:')
    if(choose_difficulty == 'easy'):
        launch_easy()
    elif(choose_difficulty == 'medium'):
        launch_medium()
    elif(choose_difficulty == 'hard'):
        launch_hard()
    else:
        print('Please enter a valid response')
        launch_game()

#user can create new cards
def create_cards():
    category = str(input('Please enter a flashcard category:'))
    difficulty = str(input('Please enter a flashcard difficulty:'))
    question = str(input('Please enter a flashcard question:'))
    answer = str(input('Please enter a flashcard answer:'))
    insert = f"""insert into flashcards (category, difficulty, question, answer) values ('{category}', '{difficulty}', '{question}', '{answer}')"""
    cursor.execute(insert)
    cursor.execute('select * from flashcards')
    result = cursor.fetchall()
    print(result)

def launch_easy():
    # correct = 0
    # incorrect = 0 

    print('Here are your easy questions!')
    easy = "select * from flashcards where difficulty= 'easy' "
    cursor.execute(easy)
    result = cursor.fetchall()
    for i in range(len(result)):
        user_answer= str(input((f'{result[i][3]}:')))
        print(result[i][4])
        if(user_answer == result[i][4]):
            print('Correct')
            score = result[i][5]
            new_score = score + 1

            cursor.execute(f'update flashcards set correct = {new_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {new_score} times and incorrect {result[i][6]} times during this session")

        elif(user_answer != result[i][4]):
            print('Incorrect')
            score = result[i][6]
            incorrect_score = score +1

            cursor.execute(f'update flashcards set incorrect = {incorrect_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {result[i][5]} times and incorrect {incorrect_score} times during this session")

    play_again = input('Would you like to play again? y or n:')
    if(play_again == 'y'):
        easy_mode = input('Would you like to stay in easy mode? y or n:')
        if(easy_mode == 'y'):
            launch_easy()
        elif(easy_mode == 'n'):
            launch_game()

def launch_medium():
    print('Here are your medium questions!')
    medium = "select * from flashcards where difficulty= 'medium' "
    cursor.execute(medium)
    result = cursor.fetchall()
    for i in range(len(result)):
        user_answer= str(input((f'{result[i][3]}:')))
        print(result[i][4])
        if(user_answer == result[i][4]):
            print('Correct')
            score = result[i][5]
            new_score = score + 1

            cursor.execute(f'update flashcards set correct = {new_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {new_score} times and incorrect {result[i][6]} times during this session")

        elif(user_answer != result[i][4]):
            print('Incorrect')
            score = result[i][6]
            incorrect_score = score +1

            cursor.execute(f'update flashcards set incorrect = {incorrect_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {result[i][5]} times and incorrect {incorrect_score} times during this session")

    play_again = input('Would you like to play again? y or n:')
    if(play_again == 'y'):
        easy_mode = input('Would you like to stay in medium mode? y or n:')
        if(easy_mode == 'y'):
            launch_medium()
        elif(easy_mode == 'n'):
            launch_game()

def launch_hard():
    print('Here are your hard questions!')
    hard = "select * from flashcards where difficulty= 'hard' "
    cursor.execute(hard)
    result = cursor.fetchall()
    for i in range(len(result)):
        user_answer= str(input((f'{result[i][3]}:')))
        print(result[i][4])
        if(user_answer == result[i][4]):
            print('Correct')
            score = result[i][5]
            new_score = score + 1

            cursor.execute(f'update flashcards set correct = {new_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {new_score} times and incorrect {result[i][6]} times during this session")

        elif(user_answer != result[i][4]):
            print('Incorrect')
            score = result[i][6]
            incorrect_score = score +1

            cursor.execute(f'update flashcards set incorrect = {incorrect_score} where ID = {result[i][0]}')

            print(f"You've answered this correct {result[i][5]} times and incorrect {incorrect_score} times during this session")

    play_again = input('Would you like to play again? y or n:')
    if(play_again == 'y'):
        easy_mode = input('Would you like to stay in hard mode? y or n:')
        if(easy_mode == 'y'):
            launch_hard()
        elif(easy_mode == 'n'):
            launch_game()



game_intro()

# testing script
# cursor.execute('''SELECT * from flashcards''')
# result = cursor.fetchall()
# print(result)
