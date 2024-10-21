# DFS to solve Water Jug Problem
def dfs_water_jug_problem():
    # Jug capacities
    max_jug1 = 3  # 3-gallon jug
    max_jug2 = 4  # 4-gallon jug

    # Initial state (jug1 is 0, jug2 is 0)
    initial_state = (0, 0)

    # Goal: 2 gallons in the 4-gallon jug
    goal_state = (None, 2)

    # To keep track of visited states
    visited = set()

    # Stack for DFS
    stack = [(initial_state, [])]  # Each element is (current_state, path_taken)

    # Perform DFS
    while stack:
        (jug1, jug2), path = stack.pop()

        # If we've reached the goal state
        if jug2 == goal_state[1]:
            return path + [(jug1, jug2)]

        # If the state is already visited, skip it
        if (jug1, jug2) in visited:
            continue

        # Mark the state as visited
        visited.add((jug1, jug2))

        # Generate all possible next states and push to the stack
        next_states = get_next_states(jug1, jug2, max_jug1, max_jug2)

        for state in next_states:
            if state not in visited:
                stack.append((state, path + [(jug1, jug2)]))

    return "No solution found"

# Function to generate all possible next states based on the current jug levels
def get_next_states(jug1, jug2, max_jug1, max_jug2):
    states = []
    
    # Fill the 3-gallon jug
    states.append((max_jug1, jug2))
    
    # Fill the 4-gallon jug
    states.append((jug1, max_jug2))
    
    # Empty the 3-gallon jug
    states.append((0, jug2))
    
    # Empty the 4-gallon jug
    states.append((jug1, 0))
    
    # Pour water from the 3-gallon jug to the 4-gallon jug
    pour_jug1_to_jug2 = min(jug1, max_jug2 - jug2)
    states.append((jug1 - pour_jug1_to_jug2, jug2 + pour_jug1_to_jug2))
    
    # Pour water from the 4-gallon jug to the 3-gallon jug
    pour_jug2_to_jug1 = min(jug2, max_jug1 - jug1)
    states.append((jug1 + pour_jug2_to_jug1, jug2 - pour_jug2_to_jug1))

    return states

# Driver code
if __name__ == "__main__":
    result = dfs_water_jug_problem()
    if isinstance(result, list):
        print("Solution Path (Jug1, Jug2):")
        for step in result:
            print(step)
    else:
        print(result)