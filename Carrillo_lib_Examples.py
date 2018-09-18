import Carrillo_lib
print()
print(Carrillo_lib.box_formatter(["This is the most basic output, with all default settings."]))
print()
print(Carrillo_lib.box_formatter(["You can specify the border, too!"], "==|-|=="))
print()
print(Carrillo_lib.box_formatter(["Multiple lines accepted!", "Many customizable options!", "Whether you put multiple lines or not,", "make sure you give the text in list form."], ".o0o.", True, alignment=-1))
print()
print(Carrillo_lib.box_formatter(["", "This box demonstrates", " S I D E   D E C O R A T I O N ", "its pretty cool.", ""], '=', side_decor='|  |', corner_decor='[__]', alignment=0))
print()
if Carrillo_lib.yes_no("Did you find these examples useful? (yes/no) = "):
    print("Thanks!")
else:
    print("k bye")
