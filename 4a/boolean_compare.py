# Enter expressions to compare as strings as logic_string_1 & 2 below:
logic_string_1 = "(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))"
logic_string_2 = "(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)"

divider = '-------------------'
print(divider*2)
print("1:",logic_string_1)
print("2:",logic_string_2)
print(divider*2)
print("input - output")
print("a b c - 1 2 unequal")
for a in range(2):
    print(divider)
    for b in range(2):
        print()
        for c in range(2):
            print(a, b, c, "-", int(eval(logic_string_1)), int(eval(logic_string_2)), "<<<<" if int(eval(logic_string_1)) != int(eval(logic_string_2)) else "")
