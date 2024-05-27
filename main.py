print("DISTANCE CALCULATOR ")
while True:
    x1,y1=list(map(int,input("Enter points 1's co-ordinate :").split()))
    x2,y2=list(map(int,input("Enter points 2's co-ordinate :").split()))
    dis=((x2-x1)**2+(y2-y1)**2)**(1/2)
    print("Distance between two points : ",dis)
    a=input("Do you want to continue or exit ?? (y/n)")
    if a=="n":
        print("Thank you!!!")
        break







