num = 3 
num1 = 3.14

print(type(num))
print(type(num1)) # überprüfen für den Typ wert - float 
"""
Arithmetic Oparators:
Addition:           3 + 3
Subtraction:        3 - 2
Multiplication:     3 + 3
Division:           3 / 2
Floor Division:     3 // 2
Exponent:           3 ** 3
Modulus:            3 % 2

# 
# """
class terminal_color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(terminal_color.HEADER, terminal_color.UNDERLINE +"Arithmetic Oparators:" + terminal_color.ENDCOLOR)
"""
Addition:           3 + 3
Subtraction:        3 - 2
Multiplication:     3 * 3
Division:           3 / 2
Floor_Division:     3 // 2
Exponent:           3 ** 3
Modulus:            3 % 2
"""
a = "3 + 2"
b = "3 - 2"
c = "3 / 2"
d = "3 * 2"
e = "3 // 2"
f = "3 ** 2"
g = "3 % 2"
print(f"Addition: {terminal_color.BLUE + a + terminal_color.ENDCOLOR} = ", 3 + 2)
print(f"Subtraction:  {terminal_color.BLUE + b + terminal_color.ENDCOLOR} =", 3 - 2)
print(f"Division: {terminal_color.BLUE + b + terminal_color.ENDCOLOR} = ", 3 / 2)
print(f"Multiplication: {terminal_color.BLUE + d + terminal_color.ENDCOLOR} = ", 3 * 2)
print(f"Floor Division: {terminal_color.BLUE + e + terminal_color.ENDCOLOR} = ", 3 // 2)
print(f"Exponent: {terminal_color.BLUE + f + terminal_color.ENDCOLOR} = ", 3 ** 2)
print(f"Modulus: {terminal_color.BLUE + g + terminal_color.ENDCOLOR} = ", 3 % 2)

h = "3 * (2 + 1)"
print(f"Addition: {terminal_color.BLUE + h + terminal_color.ENDCOLOR} = ", 3 * (2 + 1))

num2 =  1
# num2 = num2 + 1
# short way syntax
num2 += 1
print(f"num + 1 = {num2}")

# absolute value
print("absolute value of -3: ",abs(-3))

# round
print("round a float number 3.75: ", round(3.75))
