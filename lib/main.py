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

db.drop_tables([FlashCards])
db.create_tables([FlashCards])
question1 = FlashCards(category = 'geography', difficulty='easy', question = 'Which continent is the worlds largest?', answer = 'Asia')
question1.save()
question2 = FlashCards(category = 'geography', difficulty='medium', question='What sea is considered to have healing properties because of its mineral content?', answer='The Dead Sea')
question2.save()
question3 = FlashCards(category='geography', difficulty='hard', question='What Pacific Island country has the largest raised coral atoll?', answer='The Soloman Islands')
question3.save()
question4 = FlashCards(category='pop culture', difficulty='easy', question= 'Who sings Genie in a Bottle?', answer='Christina Aquilera')
question4.save()
question5 = FlashCards(category='pop culture', difficulty='medium', question='What movie depicts a janitor at a high level college, who solves difficult blackboard problems at night?', answer='Good Will Hunting')
question5.save()
question6 = FlashCards(category='pop culture', difficulty='hard', question='What is Christinas least favorite movie ever?', answer='Avatar the Last Airbender')
question6.save()
question7 = FlashCards(category='history', difficulty='easy', question='Who ended the apatheid in South Africa', answer='Nelson Mandela')
question7.save()
question8 = FlashCards(category='history', difficulty='medium', question='Who was assasinated to start WWI?', answer='Franz Ferdinand')
question8.save()
question9 = FlashCards(category='history', difficulty='hard', question='Where was Franz Ferdinand assasinated?', answer='Sarajevo, Bosnia')
question9.save()
#section that is populating database

