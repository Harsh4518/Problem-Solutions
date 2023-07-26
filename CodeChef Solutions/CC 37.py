t=int(input("Enter the no of testcases:"))

for i in range(t):

    h,c,t=map(float, input("\nEnter Parameters:").split())

    grade=0

    if h>50 and c<0.7 and t>5600:

        grade=10

    if h>50 and c<0.7 and t<=5600:

        grade=9

    if h<=50 and c<0.7 and t>5600:

        grade=8

    if h>50 and c>=0.7 and t>5600:

        grade=7

    if (h>50 and c>=0.7 and t<=5600) or (h<=50 and c<0.7 and t<=5600) or (h<=50 and c>=0.7 and t>5600):

        grade=6

    if h<=50 and c>=0.7 and t<=5600:

        grade=5

    print("GRADE OF STEEL:{}".format(grade))

        
    

    
