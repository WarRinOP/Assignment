

lst = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72]

for num in lst:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")
