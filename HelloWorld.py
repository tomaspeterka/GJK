# This script was created by Tomas Peterka, 22.9.2023. As an excuse for not doing it on time :)

import time


languages = "| English | French | Spanish | German | Italian | Japanese | Portuguese | Hindi | Polish | Czech |"
hello_languages = ["Hello", "Bonjour", "Hola", "Guten Tag", "Salve", "こんにちは", "Olá", "नमस्ते", "Dzień dobry", "Ahoj"]

for greetings in hello_languages:
    time.sleep(0.5)
    print (greetings)

time.sleep(0.5)
print()
time.sleep(0.5)

#print("                                                     \U0001F310")

print (languages)

while True:
    language = input("Choose a language please: ").lower()

    if language == "czech":
        print()
        print("You've choosed the ultimate language of the world. Try to learn it :) ")

        time.sleep(3)
        print("Here you have some quote, because you've been waiting realy long time: ")
        print()
        print("„Čeština je krásná řeč. Ona má obrovskou plejádu slov pro obyčejný věci. Třeba kulaťoučké jablíčko. To neřeknete jinou řečí. Angličan musí říct “a litte round apple“, malé kulaté jablko…. Tomu přece chybí barva i vůně.“ —--  Jan Werich")
        print()
        
        break
    elif language == "english":
        print("You are closer to the language you want to use.")
    else:
        print("You choosed the wrong language. Try it again!")


time.sleep(10)

print("Created by TomCODES")