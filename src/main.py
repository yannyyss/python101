# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def sets():
    #Los sets ignoran valores duplicados, y el orden como sea
    set = {"a","b","c","a","b","c","a","b","c"}
    for s in set:
        print(s)

def diccionarios():
    ejemplo_dic = {"str":"esto es un string", "float":1.540, "int":1}

    for key,val in ejemplo_dic.items():
        print(f"{key} = {val}")

def iterate_fruits():
    x = range(0,6,2)
    for y in x:
        print(y)

    fruits=["apple","orange","banana"]
    for x in fruits:
        print (x)

def iterate():
    for x in range (10):
        print(x)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('Yan')
    #iterate()
    # iterate_fruits()
    diccionarios()
    sets()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
