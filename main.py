import json
import re 

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
    
def binary2decimal(bits, f = False):
    sum = 0
    count = 0
    
    for b in reversed(bits[1:]):
        sum += int(b) * (2 ** count)
        count += 1

    if bits[0] == "1" and f == True:
        sum = sum - 2048
    return sum
with open('actions.json', 'r') as file:
    actions = json.load(file)
while True:
    message = input("Please enter the machine code in a 32-bit format (write done to exist): ").replace(" ", "")
    if len(message) == 32 and re.fullmatch("[01]+",message):
        op = opcode(message[-7:])
        func3 = binary2decimal(message[-15:-12])
        rs1 = binary2decimal(message[-20:-15])
        rs2 = binary2decimal(message[-24:-20])
        func7 = binary2decimal(message[:-25])
        imm = binary2decimal(message[:-20], True)

        rd = binary2decimal(message[-12:-7])

        if op == "U":
            imm = binary2decimal(message[:-12],True)
        elif op == "S":
            imm = binary2decimal(message[:-25]+message[-12:-7],True)
        elif op == "B":
            imm = binary2decimal(message[0]+message[-8]+message[1:-25]+message[-12:-8]+"0", True)
        elif op == "J":
            imm = binary2decimal(message[0]+message[-20:-12]+message[-21]+message[1:-21]+"0", True)

        if op == "R":
            print(f'{actions[op][str(func3)[0]][str(func7)[0]]} x{rd}, x{rs1}, x{rs2}')

        elif op == "J":
            print(f'{actions[op]} x{rd}, {imm}')

        elif op == "U":
            print(f'{actions[op][str(binary2decimal(message[-7:]))]} x{rd}, {imm}')

        elif op == "S":
            print(f'{actions[op][str(func3)[0]]} x{rs2}, {imm}(x{rs1})')

        elif op == "B":
            print(f'{actions[op][str(func3)[0]]} x{rs1}, x{rs2}, {imm}')

        elif binary2decimal(message[-7:]) == 103:
            print(f'{actions[op][str(binary2decimal(message[-7:]))]} x{rd}, {imm}(x{rs1})')

        elif binary2decimal(message[-7:]) == 19 and func3 == 5:
            print(f'{actions[op][str(binary2decimal(message[-7:]))][str(func3)[0] + "." + message[1]]} x{rd}, x{rs1}, {rs2}')

        elif binary2decimal(message[-7:]) == 115:
            print(f'{actions[op][str(binary2decimal(message[-7:]))][str(imm)]}')

        else:
            print(f'{actions[op][str(binary2decimal(message[-7:]))][str(func3)[0]]} x{rd}, x{rs1}, {imm}')
    elif message.lower() == "done":
        print("See you again later")
        quit()
    else:
        print("There was an error in the input, please try again")

