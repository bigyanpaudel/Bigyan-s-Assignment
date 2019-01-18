1.
radius = 5
print("The volume of circle of radius 5 is {}".format((4/3)*(22/7)*radius**3))

2.
cover_price = 240
discount = (40/100)*240
initial_shipping=25
additional_shipping=15
print("The wholesale cost for 60 copies is {}".format((cover_price-discount)*60 + initial_shipping*20 + additional_shipping*40))

3.
v = 25
t = 10
u = 0
a = (v - u)/t
print("The acceleration value is: ", a)

4.
first_name = input("Enter you First Name : ")
last_name = input("Enter you Last Name : ")
print("Hello!", first_name + " " + last_name)

5.
name = input("Enter any string :")
for i in range(0, 10):
    print(i + 1, name)

7.
def disect(l):
    return l[1:-1]
l = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
l = disect(l)
print(l)

