import re
import os
import sys
from tqdm import tqdm
from time import sleep

# region A-intruction


def toBin(line):
    binary = bin(int(line.strip('@')))
    return binary


def to16Bit(num):
    num = str(num)
    num = num[2:]
    num = num.zfill(16)
    return num
# endregion

# region C-instruction


def toXBit(num, bits):
    num = str(num)
    num = num[2:]
    num = num.zfill(bits)
    return num


def destBits(line):
    # *Done
    if '=' not in line:
        return '000'

    # m = 1 D = 2 A = 3
    bitVals = {'M': 1, 'D': 2, 'A': 4}
    dest = line.split('=')[0].strip()
    dest.split()
    binVals = [bitVals[val] for val in dest]
    return toXBit(bin(sum(binVals)), 3)


def JMPbits(line):
    # *Done
    jmpVals = {
        'JGT': 1,
        'JEQ': 2,
        'JGE': 3,
        'JLT': 4,
        'JNE': 5,
        'JLE': 6,
        'JMP': 7,
    }

    if not ';' in line:
        return '000'

    # use regex pull out 3 cap letters
    # use dict turn into bits
    regex = r';([A-Z]{3})'
    jump = re.findall(regex, line)[0]
    return toXBit(bin(jmpVals[jump]), 3)


def compBits(line):
    line.replace(' ', '')
    if ';' in line:
        line = line.split(';')[0]
    if '=' in line:
        comp = line.split('=')[1].strip()
    else:
        comp = line.strip()

    comp = comp.replace(' ', '')

    compVals = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        '!D': '0001101',
        '!A': '0110001',
        '-D': '0001111',
        '-A': '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M': '1110000',
        '!M': '1110001',
        '-M': '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101',
    }
    return compVals[comp]

# endregion


def writeToFile(filename, instructions):
    with open(filename, 'w') as file:
        file.writelines(instructions)
        file.close()

def has_letter(inputString):
    return any(str(char).isalpha() for char in inputString)

def initialRun(file):
    reserverRam = {
        'R0': '0',
        'R1': '1',
        'R2': '2',
        'R3': '3',
        'R4': '4',
        'R5': '5',
        'R6': '6',
        'R7': '7',
        'R8': '8',
        'R9': '9',
        'R10': '10',
        'R11': '11',
        'R12': '12',
        'R13': '13',
        'R14': '14',
        'R15': '15',
        'SCREEN': '16384',
        'KBD': '24576',
    }
    labels = {}
    ramSpot = 15
    moveIAmount = 0
    whole_file = file.readlines()
    for i in tqdm(range(len(whole_file)), desc='Initial File Cleaning: '):
        i -= moveIAmount
        line = whole_file[i]
        #make a regex that finds // and replaces // and everything to the right with a \n
        line = line.split('//')[0].replace(' ', '')
            
        if '(' in line and ')' in line and '@' not in line:
            del whole_file[i]
            moveIAmount += 1
            labels[line.replace('(', '').replace(')', '').strip()] = i
            continue
        # check for variables
        if '@' in line and  has_letter(line) and line.replace('@', '').replace(' ', '').strip() not in labels:
            if not line.replace('@', '').replace(' ', '').strip() in reserverRam:
                reserverRam[line.strip('@').replace(' ', '').strip()] = ramSpot
                ramSpot += 1
            whole_file[i] = f'@{ramSpot}\n'
            continue
        
        testDict = reserverRam | labels
        for key in testDict:
            if key in line:
                whole_file[i] = f'@{testDict[key]}\n'
                break
        whole_file[i] = line.replace(' ', '')

    file.close()
    file = open('temp.txt', 'w')
    file.writelines(whole_file)




def main():
    try:
        outfile , infile = sys.argv[1:]
    except:
        print('The format is incorrect expected 2 input arguments but recieved ' + str(len(sys.argv) - 1) + ' arguments')
    
    filename = infile 
    try:
        file = open(filename, 'r')
    except FileNotFoundError as fnfError:
        print('File not found')
        print(fnfError)
        print('Make sure you don\'t have any typos')
    
    initialRun(file)

    instructions = []

    with open('temp.txt', 'r') as file:
        file = file.readlines()
        for i in tqdm(range(len(file)) , desc='Compiling to Binary', ncols=100):
            if '@' in file[i]:
                instructions.append(to16Bit(toBin(file[i])) + '\n')
            else:
                dest = destBits(file[i])
                jmp = JMPbits(file[i])
                comp = compBits(file[i])
                instruction = comp + dest + jmp
                instruction = '111' + instruction
                instructions.append(instruction + '\n')

    writeToFile(outfile, instructions)
    os.remove('temp.txt')


if __name__ == "__main__":
    main()