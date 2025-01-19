"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lubomír Vaňura
email: Lubomir.2@seznam.cz
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

splitter = ("-" * 60)

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

name = input("username: ")
password = input("password: ")

value_min = 1
value_max = len(TEXTS)

if users.get(name) and users[name] == password:
    print(splitter)   
    print("Welcome to the app,", name)
    print("\n", "We have", value_max, "texts to be analyzed.")
    print(splitter)
    value_level = input (
    f"Enter a number btw. {value_min} and {value_max} to select: 1:  "
    )
    users.get(name) and users[name] == password
    pass
    print(splitter)
else: 
    name not in users
    print("unregistered user, terminating the program..")
    exit()
#______________________________________________________________
   
    if value_min <= int(range) <= value_max:
        selected_text = int(range)  # Vybere text na základě hodnoty range
        wordy = TEXTS[selected_text - 1].split()  # Rozdělí text na slova
        total_number_of_words = len(wordy)  # Spočítá počet slov
        print(f"Vybraný text: {TEXTS[selected_text - 1]}")
    else: 
        value_level not in selected_text
    print("Value is outside of the range.")
        
#_______________________________________________________________       
    number_of_words = len(wordy)
    number_of_tc_words = len([word for word in wordy if word.istitle()])
    number_of_uc_words = len([word for word in wordy if word.strip(".,!?;:").isupper() and word.isalpha()])
    number_of_lc_words = len([word for word in wordy if word.strip(".,!?;:").islower()])
    number_of_num_strings = len([word for word in wordy if word.isdigit()])
    sum_of_numbers = sum([int(num) for num in wordy if num.isdigit()])
           
    print(splitter)
    print(f"There are {number_of_words} words in the selected text.")
    print(f"There are {number_of_tc_words} titlecase words.")
    print(f"There are {number_of_uc_words} uppercase words.")
    print(f"There are {number_of_lc_words} lowercase words.")
    print(f"There are {number_of_num_strings} numeric strings.")
    print(f"The sum of all numbers is {sum_of_numbers}.")
    print(splitter)
    

# Seznam pro uchování počtu výskytů délky slov
counting_lenght = {}

for text in TEXTS:
    word = text.split() 
    
    for word in text:
       
        word = ''.join(words for words in word if words.isalnum())
        
        word_lenght = len(word)
        
        if word_lenght in counting_lenght:
            counting_lenght[word_lenght] += 1
        else:
            counting_lenght[word_lenght] = 1

sorted_lenght = sorted(counting_lenght.items())
 
print(f"{'LEN':<5}| {'OCCURENCES':<40}| {'NR.'}")
print(splitter)

for lenght, count in sorted_lenght:
    print(f"{lenght:<5}| {'*' * count:<40}| {count}")



