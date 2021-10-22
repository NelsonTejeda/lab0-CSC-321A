#!/usr/bin/env python
# Stable Matching
# Created by: Nelson Tejeda
#Date: 11/30/2021
# Purpose: takes as input equal numbers of two types of participants (n men and n women) each participant giving their preference for whom to be matched to among the participants.
#Input: y/n
# Output: people, preferences, realtime prints
import random
import os
import time


females = ["ada", "aja", "aki", "alix", "ally",
           "alma", "amy", "ann", "anna", "ara"]
males = ["pete", "zane", "chet", "che",
         "dane", "guy", "grey", "kai", "van", "jax"]

trueFemales = females.copy()


def randomizeFemales(f: list):
    ans = random.sample(f, len(f))
    return ans


def randomizeMales(m: list):
    ans = random.sample(m, len(m))
    return ans

# for i in randomizeFemales(females):
#     print(i)
# print("SPACE!!!")
# for k in randomizeMales(males):
#     print(k)


preferences = {
    "jax": randomizeFemales(females),
    "van": randomizeFemales(females),
    "kai": randomizeFemales(females),
    "grey": randomizeFemales(females),
    "guy": randomizeFemales(females),
    "dane": randomizeFemales(females),
    "che": randomizeFemales(females),
    "chet": randomizeFemales(females),
    "zane": randomizeFemales(females),
    "pete": randomizeFemales(females),

    "ada": randomizeMales(males),
    "aja": randomizeMales(males),
    "aki": randomizeMales(males),
    "alix": randomizeMales(males),
    "ally": randomizeMales(males),
    "alma": randomizeMales(males),
    "amy": randomizeMales(males),
    "ann": randomizeMales(males),
    "anna": randomizeMales(males),
    "ara": randomizeMales(males)
}

freeList = {
    "pete": 0,
    "zane": 0,
    "chet": 0,
    "che": 0,
    "dane": 0,
    "guy": 0,
    "grey": 0,
    "kai": 0,
    "van": 0,
    "jax": 0,

    "ada": 0,
    "aja": 0,
    "aki": 0,
    "alix": 0,
    "ally": 0,
    "alma": 0,
    "amy": 0,
    "ann": 0,
    "anna": 0,
    "ara": 0
}

truePreferences = preferences.copy()

men = ["pete", "zane", "chet", "che", "dane",
       "guy", "grey", "kai", "van", "jax"]
trueMen = men.copy()
itr = len(men) - 1
nextWoman = 0


def stats():
    print("\n")
    print("Participants:")
    for m in trueMen[::-1]:
        print(m, end=" ")
    print("")
    for f in trueFemales:
        print(f, end=" ")
    print("\n")

    print("Preferences:")
    c = 0
    for k, i in truePreferences.items():
        print("")
        print(k + ":", end=" ")
        for n in i:
            print(n, end=" ")
    print("\n")


stats()

# timer set
start = time.time()
# CPU time
cpuStart = time.process_time()
# set a counter to the men that are free
while(freeList[men[itr]] == 0 and itr >= 0):
    m = men[itr]
    #print("ERROR CATCHER:", freeList)
    w = preferences[m][nextWoman]
    print(m + " proposes to " + w)
    if(freeList[w] == 0):
        freeList[m] = w
        freeList[w] = m
        print(w + " accepts")
        men.pop(itr)
        itr -= 1
        if(itr == -1):
            break
        nextWoman = 0
        print("----------------------------")
    elif(preferences[w].index(m) > preferences[w].index(freeList[w])):
        # setting the guy that got dumped free
        dumped = freeList[w]
        freeList[dumped] = 0
        # assigning the man and woman
        freeList[m] = w
        freeList[w] = m
        # pop the female he already proposed to
        preferences[dumped].pop(0)
        # remove the man that stole the female from the stack
        men.pop(itr)
        # add the man that was dumped back on the stack
        men.append(dumped)
        nextWoman = 0
        print(w + " likes " + m + " more, and dumps " + dumped)
        print("----------------------------")
    else:
        print(w + " rejects " + m)
        nextWoman += 1
# end timer
end = time.time()
cpuEnd = time.process_time() - cpuStart
print("")
print("Pairings:")

for k, i in freeList.items():
    print(k + " -", i)
print("")
print("Elapsed wall clock time: ", end - start)
print("Elapsed CPU time: ", cpuEnd)
print("\n")

runAgain = input("Run Again (y)/(n)?")
if(runAgain == "y"):
    os.system('python3 gs.py')
