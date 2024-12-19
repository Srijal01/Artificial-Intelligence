%Prolog program to implement family relationship.
female(sita).
female(gita).
female(parbati).

male(ram).
male(shyam).
male(hari).

parent(sita,ram).
parent(gita,shyam).
parent(parbati,hari).
parent(sita,hari).
parent(gita,ram).

mother(Mother,Child):-
    parent(Mother,Child),
    female(Mother).
father(Father,Child):-
    parent(Father,Child),
    male(Father).
has_child(parent):-
    parent(Parent,_).
husband(Husband,Wife):-
    parent(Husband,Child),
    parent(Wife,Child),
    male(Husband),
    female(Wife).

