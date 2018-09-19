# 3
# logic_string = "(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)"

# 4
logic_string = "(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))"

divider = '----------'
print(divider*2)
print(logic_string)
print(divider*2)
print("input - output")
print("a b c - Result")
for a in range(2):
    print(divider)
    for b in range(2):
        print()
        for c in range(2):
            print(a, b, c, "-", int(eval(logic_string)))
