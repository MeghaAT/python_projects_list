print("Hi There, welcome to the tip calculator!!!!")
actual_bill=input("what was the total bill? ")
tip=input("what percentage tip would you like to give? 10, 12 or 15? ")
total_ppl=input("how many people to split the bill ")
a=float(actual_bill)
b=float(tip)
c=float(total_ppl)
#tip_with_bill=(tip/100)*bill+bill
tippy=1+(b/100)
tip_percentage=round((a/c)*tippy,2)
print("each person should pay" + " " + str(tip_percentage))