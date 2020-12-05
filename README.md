## Command Line Flashcards
_____________________

## How to play
Simply fork and clone repo down. Run pipenv install to install dependencies. Game can be played through the command line from the flashcards file. There are options on what level you would like to play on. You can also create your own cards through the command line as well.

__Description__
_______________
This project was created using the language python to access our database that we created with sql. Peewee is the simple ORM we choose to populate and interact with our database.

__Date__ | __Progress__ | __Working On__ |
--------- | -----------| ------------- |
| 11/23/20 | Started working on populating sql database, created questions | user interaction in command line |
| 11/24/20 | Have easy questions and game launching in the command line | need to work on hard and medium launch functions |
| 11/26/20 | Launched easy and medium questions, game fully functional. | na|

__Model__
```
class FlashCards(FlashGame):
    category = CharField()
    difficulty = CharField()
    question = CharField()
    answer = CharField()
    correct = IntegerField()
    incorrect = IntegerField()
```

