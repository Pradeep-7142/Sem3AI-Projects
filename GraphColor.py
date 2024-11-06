colors = ['Red', 'Blue', 'White']
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbours = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
state_color = {}

# Function to paint a state with a valid color
def paintState(myState):
    for color in colors:
        if checkColor(myState, color):
            return color
    return None  # If no color can be assigned

# Function to check if the color can be assigned to the state
def checkColor(state, color):
    for nb in neighbours.get(state):
        nbColor = state_color.get(nb)
        if nbColor == color:
            return False  # Conflict with neighboring state color
    return True  # No conflict, the color can be assigned

# Main loop to assign colors to each state
for state in states:
    state_color[state] = paintState(state)

    if state_color[state] is None:
        print("Not possible to assign further colors")
        exit()

# Display the assigned colors for each state
print(state_color)

# Find the minimum number of colors required
unique_colors = set(state_color.values())
print("Total Number of unique colors needed is", len(unique_colors))
