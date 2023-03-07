# Print Wellcome Message
my_message = 'Hello World' 

"""
Eine Konvention ist die schreib weise der Variablen, 
das wenn es aus 2 Wöternbesteht es mit _ 'BORDERLINE' geschrieben wird.
 
another_message = 'Serhat's World' <- Dieses ist nicht erlaubt 
Doubleqoutes müssen ' ' sein oder " ' ' "

"""
another_message = "Serhat's World"

print(my_message)
print(another_message)

# Länge der Ausgabe
print(len(my_message))
print('Die länge der Ausgabe für: ', another_message, 'sind', len(another_message), 'Buchstaben!')

"""
AUSGABE:
Hello World
Serhat's World
11
Die länge der ausgabe für:  Serhat's World sind 14 Buchstaben!
"""

# Einzelne Buchstaben Ausgeben lassen zugreifen
# my_message = 'Hello World' 
print(my_message[4]) # o
print(my_message[:4]) # Hell - alles bis zum 3. Buchstaben 
print(my_message[0:10]) # Hello Worl - alles von 0. Buchstaben bis zum 9. 
# Hello 
print(my_message[0:5]) # Alles von 0 bis 4. Zeichen
# World
print(my_message[6:]) # ab der 6. Zeichen alles Ausgeben lassen

# Alles Lower / Uppercase
print(my_message.lower())
#hello world
#HELLO WORLD
print(my_message.upper())

print(my_message.count('Hallo')) # findet nichts in der Variabel 'Hallo' = 0

print(my_message.count('Hello')) # in diser Variable kann es 'Hello finden'

print(my_message.find('un'))
print(my_message.find('W'))

"""
variable verändern und versetzten bzw. ersetzten
"""

my_message.replace('World', 'Coding Challenge') # funkioniert nicht
print(my_message)

my_new_message = my_message.replace('World', 'Coding Challenge')
print(my_new_message)

"""
string concatination
"""
greeting = 'Hello'
namen = 'Serhat'

kombi = greeting + ', ' + namen + '!'
print(kombi)

# Formatted string
vari1 = '\n{}, {}. Welcome...'.format(greeting, namen) # Format übernimmt für das 0. und 1. klammer in vari1 die variablen
print(vari1)

# f-string
vari2 = f'\n{greeting.expandtabs(tabsize=8)}, {namen.upper()}. Welcome!'
print(vari2)

# 'dir()' -funkion
print('\n', dir(vari2))

#print(help(str))
