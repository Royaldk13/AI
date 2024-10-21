from collections import deque

# BFS to solve Water Jug Problem
def bfs_water_jug_problem():
    # Jug capacities
    max_jug1 = 3  # 3-gallon jug
    max_jug2 = 4  # 4-gallon jug

    # Initial state (jug1 is 0, jug2 is 0)
    initial_state = (0, 0)

    # Goal: 2 gallons in the 4-gallon jug
    goal_state = (None, 2)

    # To keep track of visited states
    visited = set()

    # Queue for BFS (deque for efficient popping from the left)
    queue = deque([initial_state])

    # Parent dictionary to trace back the solution
    parent = {initial_state: None}

    # Perform BFS
    while queue:
        jug1, jug2 = queue.popleft()

        # If we've reached the goal state
        if jug2 == goal_state[1]:
            return trace_path(initial_state, (jug1, jug2), parent)

        # If the state is already visited, skip it
        if (jug1, jug2) in visited:
            continue

        # Mark the state as visited
        visited.add((jug1, jug2))

        # Generate all possible next states and add to the queue
        next_states = get_next_states(jug1, jug2, max_jug1, max_jug2)

        for state in next_states:
            if state not in visited:
                queue.append(state)
                parent[state] = (jug1, jug2)

    return "No solution found"

# Function to trace the path from the initial state to the goal
def trace_path(start, goal, parent):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path

# Generate all possible next states based on the current jug levels
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
    result = bfs_water_jug_problem()
    if isinstance(result, list):
        print("Solution Path (Jug1, Jug2):")
        for step in result:
            print(step)
    else:
        print(result)