#AI LINK = https://gemini.google.com/share/2e1e5330df8b

productionRules = {
    'A' : ["da", "BC"],
    'B' : ["g", "e"],
    'C' : ["h", "e"],
}

Productions = (list(productionRules.keys()))  #Values = [A, B, C]

#get the non terminal
def First(symbol: str) -> list:
    first = []                  #Empty List
	
    if symbol == "e":           #Base Case: Epsilon
        return ["e"]

    #Loop sa productions
    for RHS in productionRules[symbol]:
        i = 0

        #Loop pang check kung pwede ung katabi
        while i < len(RHS):
            value = RHS[i]
            
            #Generator
            if value.isupper():
                gen = First(value)

                # Add everything except e
                for x in gen:
                    if x != "e":
                        first.append(x)

                # Dahil may epsilon, pwede pa iadd ung sunod.
                if "e" in gen:
                    i += 1
                    if i >= len(RHS):
                        first.append("e")
                        break

            #Terminal symbols
            else:
                first.append(value)
                break

    return first

    
#find the non terminal after the given set
#def Follow(symbol):
    
for generator in Productions:
    first = First(generator)
    print(f"FIRST ({generator}) : {first}")