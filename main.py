import json
 
def opcode(op):
    if op == "0110111" or op == "0010111":
        return 'U'
    elif op == "0010011" or op == "0000011" or op == "1100111" or op == "1110011":
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
        sum += int(b) * (2 ** count)
        count += 1

    return sum 

with open('actions.json', 'r') as file:
    actions = json.load(file)
while True:
    message = input("Please enter the machine code in a 32-bit format (Binary or Hexadeciaml): ").replace(" ", "")
    if len(message) == 32:
        break
    else:
        print("There was an error in the input, please try again")

op = opcode(message[-7:])
rd = -1
rs1 = -1 
rs2 = -1
func3 = -1
func7 = -1
imm = -1

rd = binary2decimal(message[-12:-7])

if op == "U" or op == "J":
    imm = binary2decimal(message[:-12])
else:
    func3 = binary2decimal(message[-15:-12])
    rs1 = binary2decimal(message[-20:-15])
    rs2 = binary2decimal(message[-24:-20])
    func7 = binary2decimal(message[:-25])
    imm = binary2decimal(message[:-20])


print(
    f'func 3 {func3}, func 7 {func7}, rd {rd}, rs1 {rs1}, rs2 {rs2}, op {binary2decimal(message[-7:])}, imm {imm}'
)
if op == "R":
    print(f'{actions[op][str(func3)[0]][str(func7)[0]]} x{rd}, x{rs1}, x{rs2}')

elif op == "J":
     print(f'{actions[op]} x{rd}, {imm}')

elif op == "U":
    print(f'{actions[op][str(binary2decimal(message[-7:]))]} x{rd}, {imm}')

elif op == "S":
    print(f'{actions[op][str(func3)[0]]} x{rs2}, {rd+imm}(x{rs1})')

elif op == "B":
    print(f'{actions[op][str(func3)[0]]} x{rs1}, x{rs2}, {rd+imm}')

elif binary2decimal(message[-7:]) == 103:
    print(f'{actions[op][str(binary2decimal(message[-7:]))]} x{rd}, {imm}(x{rs1})')

elif binary2decimal(message[-7:]) == 19 and func3 == 5:
    print(f'{actions[op][str(binary2decimal(message[-7:]))][str(func3)[0] + "." + message[1]]} x{rd}, x{rs1}, {rs2}')

elif binary2decimal(message[-7:]) == 115:
    print(f'{actions[op][str(binary2decimal(message[-7:]))][str(imm)]}')

else:
    print(f'{actions[op][str(binary2decimal(message[-7:]))][str(func3)[0]]} x{rd}, x{rs1}, {imm}')