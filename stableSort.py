import random
import sys
import time
import timeit

givenRange = int(str(sys.argv[1]))

females = []
males = []

for f in range(0,int(givenRange/2)):
    females.append(str(f))
for m in range(int(givenRange/2),givenRange):
    males.append(str(m))


def randomizeFemales(f:list):
    c = 0
    while c != len(f):
        ran = random.randint(0,len(f) - 1)
        temp = f[c]
        f[c] = f[ran]
        f[ran] = temp
        c += 1
    ans = f.copy()
    return ans
    
def randomizeMales(m:list):
    c = 0
    while c != len(m):
        ran = random.randint(0,len(m) - 1)
        temp = m[c]
        m[c] = m[ran]
        m[ran] = temp
        c += 1
    ans = m.copy()
    return ans

preferences = {}

for pm in males:
    preferences[pm] = randomizeFemales(females)
for pf in females:
    preferences[pf] = randomizeMales(males)

freeList = {}

for flm in males:
    freeList[flm] = -1
for flf in females:
    freeList[flf] = -1

men = []
for list in males:
    men.append(list)


itr = len(men) - 1
nextWoman = 0
#set a counter to the men that are free
while(freeList[men[itr]] == -1 and itr >= 0):
    m = men[itr]
    w = preferences[m][nextWoman]
    if(freeList[w] == -1):
        freeList[m] = w
        freeList[w] = m
        #pop the man off the stack to confirm he is taken
        men.pop(itr)
        itr -= 1
        if(itr == -1):
            break
        nextWoman = 0
    elif(preferences[w].index(m) > preferences[w].index(freeList[w])):
        #setting the guy that got dumped free
        dumped = freeList[w]
        freeList[dumped] = -1
        #assigning the man and woman
        freeList[m] = w
        freeList[w] = m
        #pop the female he already proposed to
        preferences[dumped].pop(0)
        #remove the man that stole the female from the stack
        men.pop(itr)
        #add the man that was dumped back on the stack
        men.append(dumped)
        nextWoman = 0
    else:
        nextWoman += 1
#execution_time = timeit.timeit(Self, number=1)
print(freeList)
#print(execution_time)

def main():
    print("hi")

if __name__=="__main__":
    main()

