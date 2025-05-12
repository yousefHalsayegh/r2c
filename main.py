
import math 
def opcode(op):
    if op == "0110111" or op == "0010111":
        return 'U'
    elif op == "0010011" or op == "0000011" or "1100111":
        return 'I'
    elif op == "1101111":
        return 'J'
    elif op == "0100011":
        return 'S'
    elif op == "1100011":
        return "B"
    elif op == "0110011":
        return "R"
    else:
        print("The entered Opcode is wrong re-enter the code")
    
def binary2decimal(bits):
    sum = 0
    count = 0
    for b in reversed(bits):
        sum = int(b) * math.exp(2, count)
        count += 1
    return sum 

while True:
    message = input("Please enter the machine code in a 32-bit format: ").replace(" ", "")
    if len(message) == 32:
        break
    else:
        print("There was an error in the input, please try again")

op = opcode(message[-7:-1])
rd = 0
rs1 = 0 
rs2 = 0
#encoding = [message[i*4: (i+1)*4] for i in range(0, 8)]
if op == "S" or op == "B":
    pass
else:
    rd = binary2decimal(message[-12:-7])
