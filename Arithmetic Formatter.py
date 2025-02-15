def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5: # checks that there are five or less problems
        return 'Error: Too many problems.'
    if any('*' in prob or '/' in prob for prob in problems): # checks that only the right operators are used
        return "Error: Operator must be '+' or '-'."
    final_string = ''
    all_first_number = []
    all_second_number = []
    all_operator = []
    for k in range(len(problems)): # iterates through number of problems
        number = ''
        for char in problems[k]: # iterates through string for the kth problem
            if not char.isdigit() and char != '+' and char != '-' and char != ' ': # checks if theres a bad character
                return 'Error: Numbers must only contain digits.'
            if char.isdigit(): # if the character is a digit
                number += char
            if char == '+' or char == '-': # if the character is the operator
                all_first_number.append(number)
                all_operator.append(char)
                number = ''
        all_second_number.append(number)
    for i in all_first_number: # Checks if any of the first numbers are more than four digits
        if int(i) > 9999: # string -> int
            return 'Error: Numbers cannot be more than four digits.'
    for i in all_second_number: # Checks if any of the second numbers are more than four digits
        if int(i) > 9999: # string -> int
            return 'Error: Numbers cannot be more than four digits.'
    for j in range(len(problems)): # first number/line formatting
        if len(all_first_number[j]) >= len(all_second_number[j]):
            final_string += "  "
        else:
            for i in range(2 + len(all_second_number[j]) - len(all_first_number[j])):
                final_string += " "
        final_string += str(all_first_number[j])
        if j < len(problems) - 1:
            final_string += "    "
    final_string += "\n"
    for k in range(len(problems)): # second number and operator line formatting
        final_string += str(all_operator[k])
        for j in range(max(len(all_first_number[k]),len(all_second_number[k])) - len(all_second_number[k]) + 1):
            final_string += " "
        final_string += str(all_second_number[k])
        if k < len(problems) - 1:
            final_string += "    "
    final_string += "\n"
    for j in range(len(problems)): # dash lines and spaces
        for k in range(max(len(all_first_number[j]),len(all_second_number[j])) + 2):
            final_string += "-"
        if j < len(problems) - 1:   
            final_string += "    "
    if show_answers == True:
        final_string += "\n"
        for j in range(len(problems)):
            first_int = int(all_first_number[j])
            second_int = int(all_second_number[j])
            answer = eval(f'{first_int} {all_operator[j]} {second_int}')
            for k in range(max(len(all_first_number[j]),len(all_second_number[j])) - len(str(answer)) + 2): # how many spaces needed before answer
                final_string += " "
            final_string += str(answer)
            if j < len(problems) - 1:
                final_string += "    "
    return final_string

def main():
    print(arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 + 49"]))
    

main()
