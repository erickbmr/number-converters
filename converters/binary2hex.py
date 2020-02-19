inp_number = "1000000"

#check if there are only numbers
try:
    binary_number = list(map(int, inp_number))

except ValueError:
    print("only numbers are allowed (0 or 1)")
    exit(0)    


#check if there are only 0 or 1
cont = 0
error = False

while(cont < len(binary_number)):
    if binary_number[cont] == 0 or binary_number[cont] == 1:
        cont+=1
    
    else:
        error = True
        break

if error:
    print("please type only 0 or 1")
    exit(0)

print(binary_number)