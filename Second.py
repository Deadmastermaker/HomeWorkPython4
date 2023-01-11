
def function_pol(str):
    my_list = list(str.split())
    for i in my_list:
        if "+" in my_list:
            my_list.remove("+")
        if "=" in my_list:
            my_list.remove("=")
    my_list.pop()
    return my_list

def file_reade(file):
    data = ""
    with open(file) as rfile:
        data = rfile.read()
    return data

def function_dict(mydict, pol2):
    new_pol = ""
    for i in reversed(mydict.items()):
        if i[0] == 0:
            new_pol += str(i[1]) + " + "
        else:
            new_pol += str(i[1]) + "*x**" + str(i[0]) + " + "

    new_pol = new_pol[:-3]

    with open(pol2, "w") as newfile:
        print(f"В файл {pol2} новый pol: {new_pol}")
        newfile.write(new_pol)
    return

