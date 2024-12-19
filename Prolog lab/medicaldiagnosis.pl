%Prolog program to implement medical diagnosis
%defining facts
symptom(john,fever).
symptom(john,cough).
symptom(lina,headache).
symptom(lina,legpain).

%defining rules
has_flu(X):-
    symptom(X,fever),
    symptom(X,cough).
has_cold(X):-
    symptom(X,cough),
    symptom(X,headache).
has_legfracture(X):-
    symptom(X,legpain),
    symptom(X,fever).


