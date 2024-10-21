MIN MAX

% Rule to find the minimum of two numbers
minimum(X, Y, X) :- X =< Y.
minimum(X, Y, Y) :- X > Y.

% Rule to find the maximum of two numbers
maximum(X, Y, X) :- X >= Y.
maximum(X, Y, Y) :- X < Y.


QUERY:
?- minimum(4, 7, Min).
Min = 4.

?- maximum(4, 7, Max).
Max = 7.


FAMILY

% Define males and females
male(swarit).
male(arnav).
male(ayansh).
male(meet).
female(tirtha).
female(viha).
female(marvi).
female(durva).

% Define parent relationships
parent(swarit, tirtha).
parent(swarit, arnav).
parent(tirtha, marvi).
parent(marvi, durva).
parent(arnav, ayansh).
parent(arnav, meet).
parent(arnav, viha).

% Rule for mother
mother(X, Y) :- parent(X, Y), female(X).

% Rule for father
father(X, Y) :- parent(X, Y), male(X).

% Rule for sibling
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Rule for aunt
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).

% Rule for uncle
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).

% Rule for grandparent
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Rule for cousin
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).

QUERY:

?- parent(swarit, X), female(X).
X = tirtha.


?- mother(X, marvi).
X = tirtha.


?- sibling(marvi, X).
X= no



