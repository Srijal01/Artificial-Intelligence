%Prolog program to implement friendsoffriends
%defining facts
friends(ram,hari).
friends(hari,ravan).
friends(ram,shyam).

%defining rules
friendsoffriends(X,Y):-
    friends(X,CommonFriend),
    friends(CommonFriend,Y).

