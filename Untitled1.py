# Let's make some drinks
import random

# build a dictionary of questions:

questions = {
    'strong': 'Do ye like yer drinks strong? Y/N', 
    'salty': 'Do ye like it with a salty tang? Y/N',
    'bitter': 'Are ye a lubber who likes it bitter? Y/N',
    'sweet':'Would ye like a bit of sweetness with yer poison? Y/N',
    'fruity': 'Are ye one for a fruity finish? Y/N'}

# build a dictionary of ingredients:

ingredients = {
    'strong': ['glug of rum', 'slug of whisky', 'splash of gin'], 
    'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],
    'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],
    'sweet':['sugar cube', 'spoonful of honey', 'splash of cola'],
    'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']}

# empty dictionary to store answers
answers = {}

def drink_name():
    names={'Verbs': ['Fluffy', 'Jumping'], 'Nouns': [' penguin', ' dolphin']}
    rname = (random.choice(names['Verbs']) + random.choice(names['Nouns']))
    print (answers)
    print(' ')
    print('hmmm let me think')
    print('sounds like you want a ',rname.upper())
    print('')
    print("It's made with...")
    print('')
    

def pick_ingredients():
    for key in answers.keys():
        if answers[key] =='Y' or answers[key] =='y' or answers[key]=='yes' or answers[key]=='Yes':
            print(random.choice(ingredients[key]))
        else:
            pass

def want_drink():
    
    print ("Do you wan't a drink? ")
    x=input()
    if x =='Y' or x =='y' or x=='yes' or x=='Yes':
        for key in questions.keys():
            print(questions[key])
            answers[key]=input()
        drink_name()
        pick_ingredients() 
   
    else:
        print('Have a good day.  Come again soon.')




if __name__ =='__main__': 
    want_drink()
    