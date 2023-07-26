for i in range(int(input("Enter the No of test Cases:"))):

    total=0

    quantity,price=map(int, input("\nEnter Quantity and Price:").split())
    
    total=total+(quantity*price)

    if quantity>1000:

        total_price=total-(total*0.1)
        print("Total Price:{}".format(total_price))
        
    else:

        print("Total Price:{}".format(total))
