1#20220820 SMW
#show score of 4 Harry Potter houses. 
#able to add and remove points from each house

#set initial scores to 0
Gryffindor=482
Slytherin=472
Ravenclaw=426
Hufflepuff=312

#loop until quit selected
end=0
while(end == 0):
    print("\n\n----------------------")
    print("Current House Points")
    print("----------------------")
    print("Gryffindor=",Gryffindor)
    print("Slytherin=",Slytherin)
    print("Ravenclaw=",Ravenclaw)
    print("Hufflepuff=",Hufflepuff)
    print("----------------------")
    print("----------------------")
    print("1) Change Points for Gryffindor")
    print("2) Change Points for Slytherin")
    print("3) Change Points for Ravenclaw")
    print("4) Change Points for Hufflepuff")
    print("5) Declare house winner and quit program")
    selected=input()
    if selected == "1":
        print("\nAdd/Remove how many points to Gryffindor: ")
        points=int(input())
        print("Professor Mcgonagall: ",points," points to Gryffindor")
        Gryffindor+=points
    if selected == "2":
        print("\nAdd/Remove how many points to Slytherin: ")
        points=int(input())
        print("Professor Snape: ",points," points to Slytherin")
        Slytherin+=points
    if selected == "3":
        print("\nAdd/Remove how many points to Ravenclaw: ")
        points=int(input())
        print("Professor Flitwick: ",points," points to Ravenclaw")
        Ravenclaw+=points
    if selected == "4":
        print("\nAdd/Remove how many points to Hufflepuff: ")
        points=int(input())
        print("Professor Sprout: ",points," points to Hufflepuff")
        Hufflepuff+=points    
    if selected == "5":
        if (Gryffindor > Slytherin) and (Gryffindor > Ravenclaw) and (Gryffindor > Hufflepuff):
            print("Professor Mcgonagall: Gryffindor wins the house cup!")
        if (Slytherin > Gryffindor) and (Slytherin > Ravenclaw) and (Slytherin > Hufflepuff):
            print("Professor Snape: Slytherin wins the house cup!")
        if (Ravenclaw > Slytherin) and (Ravenclaw > Gryffindor) and (Ravenclaw > Hufflepuff):
            print("Professor Flitwick: Ravenclaw wins the house cup!")
        if (Hufflepuff > Slytherin) and (Hufflepuff > Gryffindor) and (Hufflepuff > Ravenclaw):
            print("Professor Sprout: Hufflepuff wins the house cup!")
        end=1
