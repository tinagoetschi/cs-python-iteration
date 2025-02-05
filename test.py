user_age = 10
membership_type = 'PART TIME'
cost = 100
if membership_type == 'FULL':
    if user_age < 16:
        discount = 50		
    elif user_age > 65:
        discount = 25
    else:
        discount = 0
else:
    if (user_age > 18) and  (user_age < 25):
        discount = 30
    else:
        discount = 0

cost = cost - cost * discount / 100
print('membership will cost you £' + str(cost))



'''mystery = 0
surprise = 5
guess = 1
for i in range(4):
    mystery = guess + surprise
    mystery = mystery - i + guess
    guess = guess * 2
print(mystery, guess, surprise)
'''






'''sum = 0
average = 0
for count in range(5):
    sum = sum + count
print (sum)
print (count)
average = sum/count
print(average)
'''

