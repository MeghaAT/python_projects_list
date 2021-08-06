import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
total_ppl=len(names)
#print(total_ppl)
ran_generator=random.randint(0,total_ppl-1)
name_of_person_pay_bill=names[ran_generator]
print(name_of_person_pay_bill + " is going to pay the bill today!")