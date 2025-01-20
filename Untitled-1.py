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

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

def main():
    username = input("username: ")
    password = input("password: ")
    
    splitter = ("-" * 30)
    min_value = 1
    max_value = len(TEXTS)

    if users.get(username) == password:
        print(splitter)
        print("Welcome to the app,", username)
        print("We have", max_value, "texts to be analyzed.")
        print(splitter)

        selected_number = int(input(f"Enter a number between {min_value} and {max_value} to select: "))
        if min_value <= selected_number <= max_value:
            analyze_text(TEXTS[selected_number - 1])
        else:
            print(f"Please select a number between {min_value} and {max_value}.")
    else:
        print("unregistered user, terminating the program...")
        exit()
    
def analyze_text(text):
    splitter = ("-" * 30)
    words = text.split()
    num_words = len(words)
    titlecase_words = sum(1 for word in words if word.istitle())
    uppercase_words = sum(1 for word in words if word.isupper())
    lowercase_words = sum(1 for word in words if word.islower())
    numeric_strings = [word for word in words if word.isdigit()]
   
    num_numeric = len(numeric_strings)
   
    sum_numbers = sum(int(num) for num in numeric_strings) 

    print(splitter)
    print(f"There are {num_words} words in the selected text.")
    print(f"There are {titlecase_words} titlecase words.")
    print(f"There are {uppercase_words} uppercase words.")
    print(f"There are {lowercase_words} lowercase words.")
    print(f"There are {num_numeric} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers}")
    print(splitter)
    print("\nLEN|  OCCURENCES  |NR.")
    print(splitter)
    word_lengths = [len(word.strip(".,!?;:")) for word in words] 
    for i in range(1, 16):
        count = word_lengths.count(i)
        if count > 0:
            print(f"{i:>3}|{'*' * count:<16}|{count:<3}")

main()

