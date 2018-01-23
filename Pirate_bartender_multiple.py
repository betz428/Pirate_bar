
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
    rname_upper=rname.upper()
    print (answers)
    print(' ')
    print('hmmm let me think')
    print('sounds like you want a ',rname_upper)
    print('')
    print("It's made with...")
    print('')
    
    
    
    def pick_ingredients(rname_upper,customers,current_customer):
        drink_ingredients={rname_upper:[]}
        for key in answers.keys():
            if answers[key] =='Y' or answers[key] =='y' or answers[key]=='yes' or answers[key]=='Yes':
                rand_ingredient=random.choice(ingredients[key])
                drink_ingredients[rname_upper].append(rand_ingredient)
                print(rand_ingredient)
               
            else:
                pass
            
        customers[current_customer[0]].append(drink_ingredients)
        
    pick_ingredients(rname_upper,customers,current_customer)
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
    same_drink_count=0
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
            print('')
            print ("Do you want a different drink, one you have already had, or do you want to close your tab?")  
            drinks_made_list = (customers[current_customer[0]])
            print('Here is what you have had so far:')
            for dictionaries in drinks_made_list:
                for keys in dictionaries:
                    print (keys)
            print('')        
            print('Enter "New" for a different drink - "Same" for a repeat drink - "tab" to close out')
            answer = input()
            if answer.upper() == 'NEW':
                print('OK, lets make something new.')
                drink +=1
                for key in questions.keys():
                    print(questions[key])
                    answers[key]=input()
                drink_name(customers,current_customer)
               
                print (drink)
            
            elif answer.upper() == 'SAME':
                
                print('')
                print('Which drink would you like?')
                for dictionaries in drinks_made_list:
                    for keys in dictionaries:
                        print (keys)
                drink_wanted=input('Enter the name of the drink you want ', )
                print('')
                print ('Ah a ', drink_wanted, 'That is made with:')
                for dictionaries in drinks_made_list:
                    if drink_wanted.upper() in dictionaries:
                        print(dictionaries[drink_wanted.upper()])
                print ('Coming right up')
                print('')
                same_drink_count+=1
                repeat=str(same_drink_count)
                update_list=drink_wanted+'_'+repeat
                customers[current_customer[0]].append({update_list:''})
            
            else:
                print ("It's on the house today.  Come back again")
                break
                
        if drink > limit-1:
            print ('Go home you drunk!')
            break
   

if __name__ =='__main__': 
    drink=0
    limit=5
    want_drink(drink,limit,customers)
        
   
