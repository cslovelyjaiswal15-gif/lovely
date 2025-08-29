''' ASSINGMENT_2'''
# Q1 check if a number is even or odd

no= int(input("Enter a number: "))

if no % 2 == 0:
    print(f" this is a even number {no}")

else:
    print(f" this is a odd number {no}")



# Q2  for loop () iteration 


add = sum(range(1,51))

for i in range(1,51):
    print(i)
print(f"Sum of numbers from 1 to 50 is: {add}")
