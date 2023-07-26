t=int(input("Enter Number of testcases:"))

year=[2010,2015,2016,2017,2019]

for i in range(t):

    n=int(input("\nEnter the Year:"))

    if n in year:

        print("HOSTED")

    else:

        print("NOT HOSTED")
