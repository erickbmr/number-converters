import array as arr

inp_number = "32"

#check if there are only numbers
try:
    decimal_number = int(inp_number)

except ValueError:
    print("only numbers are allowed")
    exit(0)    


aux_divisor = decimal_number
mod = arr.array('i', [])

#calculate the binary number using successive division by 2
while aux_divisor >= 0:
    mod.append(aux_divisor % 2)
    aux_divisor = aux_divisor / 2
    
    if aux_divisor == 1 or aux_divisor == 0:
        mod.append(aux_divisor) 
        break

#inverts the order of the array
print(mod[::-1])