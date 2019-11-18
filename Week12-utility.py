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
def FindWordCount(lst,string):
    count = 0
    for i in range(len(lst)):
        if lst[i] == string:
            count += 1
    return count
def ScoreFinder(list1,list2,string):
    for i in range(len(list1)):F
        if list1[i] == string:
            print("OUTPUT",string,"got a score of", list2[i])
            return
    print("OUTPUT player not found")
    
def Union(list1,list2):
    joinedlist = list1 + list2
    return joinedlist
def Intersection(list1,list2):
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list3.append(list1[i])
    return list3
