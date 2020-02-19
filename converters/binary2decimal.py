binary_number = "1000000"

#check if there are only numbers
try:
    numbers = list(map(int, binary_number))

except ValueError:
    print("only numbers are allowed (0 or 1)")
    exit(0)    


#check if there are only 0 or 1
cont = 0
error = False

while(cont < len(numbers)):
    if numbers[cont] == 0 or numbers[cont] == 1:
        cont+=1
    
    else:
        error = True
        break

if error:
    print("please type only 0 or 1")
    exit(0)


#calculate the decimal number using positional notation
index = -1
decimal = 0
cont = 0

while(cont < len(numbers)):

    if numbers[index] == 1:
        decimal+=pow(2, cont)
        index-=1
        cont+=1

    else:
        index-=1
        cont+=1

print(decimal)



