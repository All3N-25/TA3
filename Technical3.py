#AI LINK = https://gemini.google.com/share/5b23ebd9d3ff

productionRules = {}
productions = []

# Nagpaoptimize kay GEMINI
def productionRulesParser(userInput: str) -> None : 
    global productionRules, productions
    if userInput == "DONE":
        return
    
    if "->" not in userInput:
        print("Invalid Production Rule")
        return

    # Split by Whitespaces
    tokens = userInput.split()

    # Dictionary Key
    LHS = tokens[0]

    if LHS.islower():
        print("Invalid Generator")
        return
    
    #Initialize Key
    if LHS not in productionRules:
        productionRules[LHS] = []

    RHS = []

    # Skip si "->"
    for token in tokens[2:]:
        if token == "|":
            if RHS:
                productionRules[LHS].append(RHS)
            RHS = []
        else:
            RHS.append(token)

    # Remaining Values
    if RHS:
        productionRules[LHS].append(RHS)

    productions = (list(productionRules.keys()))

# Get the non terminal
def First(symbol: str, visited=None) -> list:

    if visited is None:
        visited = set()           # Empty List
	
    if symbol == "e" or symbol.islower():           # Base Case: Epsilon
        return [symbol]
    
    if symbol in visited:
        return []
    
    visited.add(symbol)
    first = {}

    # Get productions for this Non-Terminal
    # Use .get() to avoid crash if symbol has no rules
    productions = productionRules.get(symbol, [])

    # Loop sa productions
    for RHS in productions:
       for i, token in enumerate(RHS):
           
            token_first = First(token, visited)

            for item in token_first:
                if item != 'e':
                    first[item] = None  # preserves insertion order

           # Check if nag generate ng epsilon
            if 'e' not in token_first:
                break

            if i == len(RHS) - 1:
                first['e'] = None

    visited.remove(symbol)
    return list(first.keys())

# find the non terminal after the given set
#def Follow(symbol):

#MAIN
print("Enter production Rules.")
print("All Tokens Must Be Separated By Space Characters.")
print("Epsilon is \"e\".")
print("Example: X -> z | X Y | e")
print("Type \"DONE\" When Finished Inputting.")

userInput = ""
i = 0

while userInput != "DONE":
    i += 1
    userInput = input(f"Production Rule ({i}): ")
    productionRulesParser(userInput)

for generator in productions:
    first = First(generator)
    print(f"FIRST ({generator}) : {first}")