EVN ODD

% Rule to check if a number is even
is_even(X) :- 0 is X mod 2.

QUERY:

?- is_even(4).
true.

?- is_even(7).
false.


STUDENT TEACHER 

% Students and the courses they study
studies(charlie, csc135).
studies(olivia, csc135).
studies(jack, csc131).
studies(arthur, csc134).

% Teachers and the courses they teach
teaches(kirke, csc135).
teaches(collins, csc131).
teaches(collins, csc171).
teaches(juniper, csc134).

% Rule to define if X is a professor of Y (X teaches a course C that Y studies)
professor(X, Y) :- teaches(X, C), studies(Y, C).


QUERY:


?- studies(charlie, C).
C = csc135.


?- professor(kirke, Student).
Student = charlie ;
Student = olivia.

