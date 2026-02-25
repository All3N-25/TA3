# AI LINK = https://gemini.google.com/share/5b23ebd9d3ff

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
    current_productions = productionRules.get(symbol, [])

    # Loop sa productions
    for RHS in current_productions:
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

# --- YOUR PART START ---

# find the non terminal after the given set
followSets = {}

def compute_follow():
    global followSets
    # precompute
    followSets = {nt: [] for nt in productions} 
    
    if not productions:
        return

    # start symbol
    followSets[productions[0]].append("$")

    changed = True
    while changed:
        changed = False
        for lhs in productions:
            for rhs in productionRules[lhs]:
                for i in range(len(rhs)):
                    symbol = rhs[i]
                    
                    # check if non-terminal
                    if symbol.isupper():
                        before_len = len(followSets[symbol])
                        
                        # not last symbol
                        if i + 1 < len(rhs):
                            next_symbol = rhs[i + 1]
                            first_next = First(next_symbol)
                            
                            # Add First(next) except epsilon
                            for x in first_next:
                                if x != "e" and x not in followSets[symbol]:
                                    followSets[symbol].append(x)
                            
                            # if e in first_next, add Follow(LHS)
                            if "e" in first_next:
                                for x in followSets[lhs]:
                                    if x not in followSets[symbol]:
                                        followSets[symbol].append(x)
                        
                        # last symbol
                        else:
                            for x in followSets[lhs]:
                                if x not in followSets[symbol]:
                                    followSets[symbol].append(x)
                        
                        if len(followSets[symbol]) > before_len:
                            changed = True

def Follow(symbol):
    return followSets[symbol]

# --- YOUR PART END ---

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
    if userInput == "DONE":
        break
    productionRulesParser(userInput)

# Run Follow set computation after inputs are done
compute_follow()

print("\n--- FIRST SETS ---")
for generator in productions:
    first = First(generator)
    print(f"FIRST ({generator}) : {first}")

print("\n--- FOLLOW SETS ---")
for generator in productions:
    follow = Follow(generator)
    print(f"FOLLOW ({generator}) : {follow}")
