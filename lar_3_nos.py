
n1 = input("enter number 1")
n2 = input("enter number 2")
n3 = input("enter number 3")

if (n1 >= n2) and (n1 >= n3):
   largest = n1
elif (n2 >= n1) and (n2 >= n3):
   largest = n2
else:
   largest = n3

print("The largest number is", largest)
