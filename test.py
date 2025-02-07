mystery = 0
surprise = 5
guess = 1
print(mystery, surprise, guess)
for i in range(4):
    mystery = guess + surprise
    surprise = mystery - i + guess
    guess = guess * 2
print(mystery, surprise, guess)

print(15/4)

'''my_list = []

for num in range(5):
    my_list += [num*num]

print(my_list)
'''

'''list_of_values = []
for i in range(0,20,2):
    if i % 6 != 0:
        if i % 3 == 0:
            list_of_values += [i]
        elif i % 2 == 0:
            list_of_values += [i]
print(list_of_values)
'''

'''
user_age = [10,15,21,67,12,18,65]
membership_type = ['PART TIME','FULL', 'PART TIME','FULL', 'FULL', 'PART TIME','FULL']
cost = [100, 120, 250, 60, 300, 150, 200]
price = []
discount=[0,0,0,0,0,0,0]
disc_amount=[]
for i in range (7):
    if membership_type[i] == 'FULL':
        if user_age[i] < 16:
            discount[i] = 50		
        elif user_age[i] > 65:
            discount[i] = 25
        else:
            discount[i] = 0
    else:
        if (user_age[i] > 18) and  (user_age[i] < 25):
            discount[i] = 30
        else:
            discount[i] = 0
    disc_amount += [cost[i] * discount[i] / 100]
    price += [cost[i] - cost[i] * discount[i] / 100]
    print('membership will cost you £' + str(cost[i]),'-', disc_amount[i], 'price =' ,price[i],  ' discount was=', discount[i], '% £',disc_amount[i])
'''







'''
sum = 0
average = 0
for count in range(5):
    sum = sum + count
    print(' count=', count, 'sum=',sum)
average = sum/count
print('average=',average)
'''

'''
x = 5
k= 10
sum = 45
print('x=', x, ' k=',k, 'sum=', sum)
while sum < 75 :
    print('sum < 75 - yes')
    sum = sum+k
    
    k= k+x
    print('x=', x, ' k=',k, 'sum=', sum)
print('sum = ', sum)
'''