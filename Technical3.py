#AI LINK = https://gemini.google.com/share/2e1e5330df8b

productionRules = {
    'A' : ["da", "BCB"],
    'B' : ["g", "e"],
    'C' : ["h", "e"]
}

Productions = []
Productions.append(list(productionRules.keys()))   #Values = [A, B, C]

#get the non terminal
#Hangang 2 na generator palang kaya.
def First(symbol: str) -> list:
    first = []                  #Empty List
	
    if symbol == "e":           #Base Case: Epsilon
        return ["e"]

    #Loop sa productions
    for RHS in productionRules[symbol]:
        i = 0
        value = RHS[i]

        #Generator
        if value.isupper():
            gen = First(value)
            first.extend(gen)

            if "e" in gen:
                first.pop()     #Alsin ung e
                value = RHS[i + 1]
                gen2 = First(value)
                first.extend(gen2)

        #Terminal
        else:
            first.append(value)

    return first

    
#find the non terminal after the given set
#def Follow(symbol):
    
for generator in Productions:
    first = First("A")
    print(first)