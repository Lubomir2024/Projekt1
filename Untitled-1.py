"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lubomír Vaňura
email: Lubomir.2@seznam.cz
"""
# nadefinování oddělovače
oddelovac = ("-" * 60)

#zadání vstupních parametrů (uživatelé a heslo)

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# program pro zadání vstupu
jmeno = input("username: ")
if jmeno in uzivatele:
    print()
else: 
    jmeno not in uzivatele
    print("Wrong user")
    exit()
heslo = input("password: ")

if uzivatele.get(jmeno) and uzivatele[jmeno] == heslo:
    print()
else:
    print("unregistered user, terminating the program..")
    exit()

#uvítací příkaz pro analýzu textu v dalším kroku 
print(oddelovac)   
print("Welcome to the app,",jmeno)
print("\n", "We have 3 texts to be analyzed.")
print(oddelovac)

#text který je definován v zadání

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

#výběr z odstavců v textu v rozsahu 1 až 3

hodnota_min = 1
hodnota_max = len(TEXTS)
vyber_hodnoty = input("Enter a number btw. 1 and 3 to select: 1:  ")

#podmínka pro případ mimo rozsah 1-3

if vyber_hodnoty not in {"1", "2", "3"}:
    print(oddelovac)
    print(" Enter a number btw. 1 and 3 to select: 1:  ") 
else:
    (f"continue")

#nevhodny vyber hodnot
if not vyber_hodnoty:
    print(oddelovac)
else:
    # Kontrola platnosti
    if hodnota_min <= int(vyber_hodnoty) <= hodnota_max:
        vyberove_cislo = int(vyber_hodnoty)
        slovicka = TEXTS[vyberove_cislo - 1].split()
        
        # Počítání slov
        number_of_words = len(slovicka)
        number_of_tc_words = len([word for word in slovicka if word.istitle()])
        number_of_uc_words = len([word for word in slovicka if word.strip(".,!?;:").isupper() and word.isalpha()])
        number_of_lc_words = len([word for word in slovicka if word.strip(".,!?;:").islower()])
        number_of_num_strings = len([word for word in slovicka if word.isdigit()])
        sum_of_numbers = sum([int(num) for num in slovicka if num.isdigit()])
        
        # Výstupní informace
        print(oddelovac)
        print(f"There are {number_of_words} words in the selected text.")
        print(f"There are {number_of_tc_words} titlecase words.")
        print(f"There are {number_of_uc_words} uppercase words.")
        print(f"There are {number_of_lc_words} lowercase words.")
        print(f"There are {number_of_num_strings} numeric strings.")
        print(f"The sum of all numbers is {sum_of_numbers}.")
        print(oddelovac)
    else:
        print("incorrect number")
        exit()

# Seznam pro uchování počtu výskytů délky slov
pocitana_delka = {}

# Pro každý text v TEXTS
for text in TEXTS:
    slova = text.split()  # Rozdělíme text na slova
    
    for slovo in slova:
        # Odstraníme interpunkci
        slovo = ''.join(sluvko for sluvko in slovo if sluvko.isalnum())
        
        # Zjistíme délku slova
        delka_slova = len(slovo)
        
        # Pokud délka slova existuje ve slovníku, zvýším počet
        if delka_slova in pocitana_delka:
            pocitana_delka[delka_slova] += 1
        else:
            pocitana_delka[delka_slova] = 1

# Seřazení délky dle velikosti
trizena_delka = sorted(pocitana_delka.items())

# Hlavička tabulky s odsazením 
print(f"{'LEN':<5}| {'OCCURENCES':<40}| {'NR.'}")
print(oddelovac)

# srovnání sloupcu do posloupnosti
for delku, pocitat in trizena_delka:
    print(f"{delku:<5}| {'*' * pocitat:<40}| {pocitat}")



