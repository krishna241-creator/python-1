def total_calc(bill_amount, bill_perc):
    bill_tip = bill_amount * bill_perc/100
    bill_amount = bill_amount + bill_tip
    print("your amount is $",bill_amount)
total_calc(150,20)