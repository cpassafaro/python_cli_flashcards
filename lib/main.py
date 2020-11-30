#this is the section that populates the database
from peewee import *

db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class FlashGame(Model):
    class Meta: 
        database = db

class FlashCards(FlashGame):
    category = CharField()
    difficulty = CharField()
    question = CharField()
    answer = CharField()
    correct = IntegerField()
    incorrect = IntegerField()

# db.drop_tables([FlashCards])
db.create_tables([FlashCards])

def populate():
    question1 = FlashCards(category = 'geography', difficulty='easy', question = 'Which continent is the worlds largest?', answer = 'Asia', correct = 0, incorrect = 0)
    question1.save()
    question2 = FlashCards(category = 'geography', difficulty='medium', question='What sea is considered to have healing properties because of its mineral content?', answer='The Dead Sea', correct = 0, incorrect = 0)
    question2.save()
    question3 = FlashCards(category='geography', difficulty='hard', question='What Pacific Island country has the largest raised coral atoll?', answer='The Soloman Islands', correct = 0, incorrect = 0)
    question3.save()
    question4 = FlashCards(category='pop culture', difficulty='easy', question= 'Who sings Genie in a Bottle?', answer='Christina Aguilera', correct = 0, incorrect = 0)
    question4.save()
    question5 = FlashCards(category='pop culture', difficulty='medium', question='What movie depicts a janitor at a high level college, who solves difficult blackboard problems at night?', answer='Good Will Hunting', correct = 0, incorrect = 0)
    question5.save()
    question6 = FlashCards(category='pop culture', difficulty='hard', question='What is Christinas least favorite movie ever?', answer='Avatar the Last Airbender', correct = 0, incorrect = 0)
    question6.save()
    question7 = FlashCards(category='history', difficulty='easy', question='Who ended the apatheid in South Africa', answer='Nelson Mandela', correct = 0, incorrect = 0)
    question7.save()
    question8 = FlashCards(category='history', difficulty='medium', question='Who was assasinated to start WWI?', answer='Franz Ferdinand', correct = 0, incorrect = 0)
    question8.save()
    question9 = FlashCards(category='history', difficulty='hard', question='Where was Franz Ferdinand assasinated?', answer='Sarajevo, Bosnia', correct = 0, incorrect = 0)
    question9.save()
    #section that is populating database

# populate()

