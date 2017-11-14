def maxParty(partyCount, budget, parties):
    table = [[-1 for _ in range(0, budget+1)] for _ in range(0, numItems+1)] 

    def mp(currentParty, budgetLeft):
        if table[currentParty][budgetLeft] < 0:
            if budgetLeft < parties[currentParty][0]:
                table[currentParty][budgetLeft] = mp(currentParty-1, budgetLeft)
            else:
                table[currentParty][budgetLeft] = max(mp(currentParty-1, budgetLeft), 
                                                        parties[currentParty][1] + mp(currentParty-1, budgetLeft - parties[currentParty][0]))
        return table[currentParty][budgetLeft]

    return mp(partyCount, budget)

def getNewCase():
    newCase = raw_input().strip().split()
    budget, partyCount = int(newCase[0]), int(newCase[1])
    return budget, partyCount


budget, partyCount = getNewCase()
while partyCount != 0:
    parties = []
    for _ in range(0, partyCount):
        party = raw_input().strip().split()
        parties.append((int(party[0]), int(party[1])))
    #input() # skip emptyline
    print "parties: {}".format(parties)

    print maxParty(partyCount, budget, parties)
    
    budget, partyCount = getNewCase()

