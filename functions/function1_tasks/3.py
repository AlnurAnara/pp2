def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None  # No solution found

# Example usage
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No solution found.")

'''
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs):
'''