%Prolog program to implment relationships in mahabharat
character(bhishma).
character(pandu).
character(dhritarastra).
character(yudhisthir).
character(bhim).
character(arjun).
character(nakul).
character(sahadev).
character(duryodhan).
character(dussasan).
character(karna).
character(krishna).
character(kunti).
character(gandhari).
character(sakuni).

father(yudhisthir,pandu).
father(bhim,pandu).
father(arjun,pandu).
father(nakul,pandu).
father(sahadev,pandu).
father(duryodhan,dhritarastra).
father(dussasan,dhritrastra).

friend(arjun,krishna).
friend(bhim,krishna).
friend(duryodhan,karna).

rival(yudhisthir,duryodhan).
rival(arjun,karna).

mentor(krishna,arjun).
mentor(bhishma,arjun).

killed(arjun,karna).
killed(bhim,duryodhan).
killed(arjun,bhishma).

is_friend(X,Y):-
    friend(X,Y).
is_mentor(X,Y):-
    mentor(X,Y).
who_killed(X,Y):-
    killed(X,Y).

