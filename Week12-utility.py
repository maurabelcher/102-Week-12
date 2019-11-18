# Maura Belcher
#Csci 102 A
#Week 12 lab A

def PrintOutput(word):
    print("OUTPUT", word)

def LoadFile(string):
    file = open(string, "r+")
    lines = file.read()
    li = lines.split()
    return li

def UpdateString(string1,string2,i):
    list1 = list(string1)
    string3 = ''
    for index in range(len(list1)):
        if index == i:
            list1[i] = string2
        string3 += list1[index]
    return string3
