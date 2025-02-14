# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

a=int(input("Enter first digit: "))
b=int(input("Enter second digit: "))
c=a
count=0
while(a%b==0):
    a//=b
    count+=1
if(count !=0):
    print(f"{c} is divisible by {b}-- {count} times")
else:
    print(f"{a} is not divisible by {b} at all!")
    