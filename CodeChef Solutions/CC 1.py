amount_withdraw,atm_balance=map(float,input().split())
amount_withdraw=float(amount_withdraw)

if (amount_withdraw%5==0):

    remain_balance=atm_balance-amount_withdraw-0.50

else:

    remain_balance=atm_balance

print('%.2f'%remain_balance)

""" PRECISION HANDLING PYTHON"""

#1-> '%.2f'%a

#2-> round(a,2)

#3-> "{0:.2f}".format(a)
