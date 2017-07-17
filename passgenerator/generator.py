from itertools import permutations

def generator(Namepart,Birthdaypart,Charpart):
    elementlist=[Namepart,Birthdaypart,Charpart]
    passlist=permutations(elementlist)
    return passlist
