def check_number(num):
    if num % 2 == 0:
        print(f"{num}) is an even number.")
    else:
        print(f"{num} is an odd number.")
        
while True:
    num = int(input("Enter your numer:"))
    check_number(num)