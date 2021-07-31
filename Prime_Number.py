#prime numbers can only be divided by 1 and itself



prime_count = 0

for number in range(0, 1000):
    prime_number = ''
    #0 can not be divided by 0
    if (number == 0):
        prime_number = False
    #for other reasons 1 do not have essential characteristic
    elif (number == 1):
        prime_number = False
    #2 can only be divided by 1 and itself
    elif (number == 2):
        prime_number = True
    else:
        for i in range(2, number):
            if (number % i == 0):
                prime_number = False
                break
            else:
                prime_number = True
    if (prime_number):
        print(number)
        prime_count += 1
print("Total Prime numbers found:", prime_count)

print("Programm ended")



#results: number(n) and prime numbers(p) found //beginning from 0
#n=100          - p=25
#n=1,000        - p=168
#n=10,000       - p=1,229
#n=100,000      - p=9,592
#n=1,000,000    - p=78,498


