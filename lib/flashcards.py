import psycopg2
from main import FlashCards 

conn = psycopg2.connect(
    database='flashcards', user='postgres', password='', host='localhost', port=5432
)

conn.autocommit = True


#pull easy information
# easy = "select * from flashcards where difficulty= 'easy' "
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
        print('Please enter a valid response /n p for play or c for create')


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


#pick how many cards they want to review
#keep track of how many cards have been answered correctly

game_intro()
