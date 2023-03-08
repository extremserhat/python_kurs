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

"""
comparisons operator:
Equal:                  3 == 2
Not Equal:              3 != 2
Greater Than:           3 > 2 
Less Than:              3 < 2
Greater or Equal:       3 >= 2
Less or Equal:          3 <= 2
"""
num_1 = 3
num_2 = 2
print(terminal_color.HEADER + terminal_color.UNDERLINE + "Comparisons Operator:" + terminal_color.ENDCOLOR)
print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Equal \t\t\t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 == num_2)

print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Not Equal \t\t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 != num_2)

print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Greater Than \t\t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 > num_2)

print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Less Than \t\t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 < num_2)

print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Greater or Equal \t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 >= num_2)

print(f"is {terminal_color.GREEN + str(num_1) + terminal_color.ENDCOLOR}\t Less or Equal \t\t{terminal_color.GREEN + str(num_2) + terminal_color.ENDCOLOR} =\t ", num_1 <= num_2)

# cast string to int
num_3 = '100'
num_4 = '200'

print(f"cast the '{num_3}'" + terminal_color.GREEN + " string " + terminal_color.ENDCOLOR + "to " + terminal_color.CYAN + "int" + terminal_color.ENDCOLOR + f" and '{num_4}'" + terminal_color.GREEN + " string " + terminal_color.ENDCOLOR + "to " + terminal_color.CYAN + "int " + terminal_color.ENDCOLOR + "for addition and the result should be", int(num_3) + int(num_4))



