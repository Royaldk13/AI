% Initial state representation: (Location, Status_A, Status_B)
% Location: a or b
% Status_A, Status_B: clean or dirty

% Goal state: Both areas are clean
goal_state(clean, clean).

% Transition rules: Actions for moving and cleaning

% If vacuum is in area A and A is dirty, clean A
action((a, dirty, B), clean, (a, clean, B)) :-
    write('Cleaning area A'), nl.

% If vacuum is in area B and B is dirty, clean B
action((b, A, dirty), clean, (b, A, clean)) :-
    write('Cleaning area B'), nl.

% If vacuum is in area A and needs to move to B
action((a, A, B), move_to_b, (b, A, B)) :-
    write('Moving to area B'), nl.

% If vacuum is in area B and needs to move to A
action((b, A, B), move_to_a, (a, A, B)) :-
    write('Moving to area A'), nl.

% Plan to clean both areas from the current state
plan(State) :-
    State = (Location, Status_A, Status_B),
    goal_state(Status_A, Status_B),
    write('Both areas are clean!'), nl.

plan(State) :-
    action(State, Action, NewState),
    plan(NewState).

% Start the vacuum cleaner in an initial state and plan to clean both areas
start_cleaning :-
    Initial_State = (a, dirty, dirty),
    plan(Initial_State).
