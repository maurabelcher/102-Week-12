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

