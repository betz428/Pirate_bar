
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
customers ={'CHASE BETZER': []}



def drink_name(customers,current_customer):
    names={'Verbs': ['Fluffy', 'Jumping', 'Fat', 'skinny', 'yummy'], 'Nouns': [' penguin', ' dolphin',' Iguana',' Snake', ' Parrot']}
    rname = (random.choice(names['Verbs']) + random.choice(names['Nouns']))
    print (answers)
    print(' ')
    print('hmmm let me think')
    print('sounds like you want a ',rname.upper())
    print('')
    print("It's made with...")
    print('')
    customers[current_customer[0]].append(rname.upper())
    
    
    def pick_ingredients(rname,customers,current_customer):
        drink_ingredients={rname:[]}
        for key in answers.keys():
            
            if answers[key] =='Y' or answers[key] =='y' or answers[key]=='yes' or answers[key]=='Yes':
                rand_ingredient=random.choice(ingredients[key])
                drink_ingredients[rname].append(rand_ingredient)
                print(rand_ingredient)
               
            else:
                pass
            
        print(drink_ingredients) 
        return drink_ingredients
    pick_ingredients(rname,customers,current_customer)
    print('')
    
    

def add_drink():
    pass



def ask_name(current_customer):
    
    name = input('Hey matey, what be your name? ', )
    name_upper=name.upper()
    current_customer=current_customer.append(name_upper)
    if name_upper in customers:
        print('Welcome back', name_upper)
        return current_customer
        
    else:
        print('Welcome to the pirate bar! ', name_upper)
        customers.update({name_upper:[]})
        return current_customer

def want_drink(drink,limit,customers):
    while drink < limit:
        current_customer=[]
        ask_name(current_customer)
        
        
        drink=len(customers[current_customer[0]])
        if drink == 0:
            print ("Do you wan't a drink? ")
            x=input()
            if x =='Y' or x =='y' or x=='yes' or x=='Yes':
                for key in questions.keys():
                    print(questions[key])
                    answers[key]=input()
                drink_name(customers,current_customer)
                
                
                
            else:
                print("""Never heard of a pirate that does't drink...
                Get outta here""")
                break
    
                
        elif drink > 0 and drink <limit: 
            print ("Do you wan't another drink? ")
            print('So far you have had: ', customers[current_customer[0]])
            x=input()
            if x =='Y' or x =='y' or x=='yes' or x=='Yes':
                drink +=1
                for key in questions.keys():
                    print(questions[key])
                    answers[key]=input()
                drink_name(customers,current_customer)
               
                print (drink)
            else:
                print ('Come back again')
                break
                
        if drink > limit-1:
            print ('Go home you drunk!')
            break
   

if __name__ =='__main__': 
    drink=0
    limit=5
    want_drink(drink,limit,customers)
        
   
