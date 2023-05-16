""" 
stack from  255-1014
lcl from    1015
tmp from    5-12

push constant i
    @i
    D = A
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push local i
    @R1
    D = M
    @i
    A = D + M
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push argument  i
    @R2
    D = M
    @i
    A = D + M
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push temp i
    @R5
    D = M
    @i
    A = D + M
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push static i
    @i
    D = A
    @[filename].i
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push pointer i
    @i
    D = A
    @R3
    A = A + D
    A = M
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push this 
    @R3
    D = A
    @R0
    A = M
    M = D
    @R0
    M = M + 1
push that
    @R4
    D = A
    @R0
    A = M
    M = D
    @R0
    M = M + 1
pop local i
    @i
    D = A
    @R1
    D = D + M
    @R13
    M = D
    @R0
    M = M - 1
    A = M
    D = M
    @R13
    A = M
    M = D
pop argument i
    @i
    D = A
    @R5
    D = D + M
    @R13
    M = D
    @R0
    M = M - 1
    A = M
    D = M
    @R13
    A = M
    M = D
pop temp i
    @i
    D = A
    @R5
    D = D + M
    @R13
    M = D
    @R0
    M = M - 1
    A = M
    D = M
pop static i
    @R0
    M = M - 1
    A = M
    D = M
    @[filename].i
    M = D 
pop pointer i
    @i
    D = A
    @R3
    D = A + D
    @R13
    M = D
    @R0
    M = M - 1
    A = M
    D = M
    @R13
    A = M
    M = D
pop this
    @R0
    M = M - 1
    A = M
    D = M
    @R3
    M = D
pop that
    @R0
    M = M - 1
    A = M
    D = M
    @R4
    M = D
#region logic    
add
    @R0
    A = M - 1
    D = M
    A  = A - 1
    D = D + M
    A = A + 1
    M = 0
    A = A - 1
    M = D
    @R0
    M = M - 1
sub
    @R0
    A = M - 1
    D = M
    A  = A - 1
    D = D - M
    A = A + 1
    M = 0
    A = A - 1
    M = D
    @R0
    M = M + 1
neg 
    @R0
    A = M - 1
    M = -M
    @R0
eq
    @R0
    A = M - 1
    D = M
    A  = A - 1
    D = D - M
    @equal
    D;JEQ
    @R0
    A = M
    A = A - 1
    M = 0 
    A = A - 1
    M = 0
    @R0
    M = M - 1
    @next
    0;JMP
    (equal) 
    @R0
    A = M
    A = A - 1
    M = 0 
    A = A - 1
    M = 1
    (next)
gt
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = D - M
    @greater
    D;JGT
    @R0
    A = M
    A = A - 1
    M = 0
    A = A - 1
    M = 0
    @next
    0;JMP
    (greater)
    @R0
    A = M
    A = A - 1
    M = 0
    A = A - 1
    M = 1
    (next)
    @R0
    M = M - 1
lt
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = M - D
    @greater
    D;JGT
    @R0
    A = M
    A = A - 1
    M = 0
    A = A - 1
    M = 0
    @next
    0;JMP
    (greater)
    @R0
    A = M
    A = A - 1
    M = 0
    A = A - 1
    M = 1
    (next)
    @R0
    M = M - 1
and
    @R0
    A = M - 1
    D = M
    M = 0
    A = A - 1
    M = D & M
    @R0
    M = M - 1
or
    @R0
    A = M - 1
    D = M
    M = 0
    A = A - 1
    M = D | M
    @R0
    M = M - 1
not
    @R0
    A = M - 1
    M = !M
#endregion

#region branching

goto labelName
    @labelName
    0;JMP
label labelName
    (labelName)
if-goto label
    @R0
    A = M - 1
    D = M
    @label
    D;JNE

function functionName nVars
    (functionName)
        [
            @R0
            A = M
            M = 0
            @R0
            M = M + 1
        ]
call functionName nArgs
    @nArgs
    D = A
    @R0
    D = M - D
    @13 //place holder of new args 
    M = D
    @returnAddress
    D = A
    @R0
    A = M
    M = D
    @R0
    M = M + 1
    @R0
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
    @R2
    D = M
    @R0
    A = M
    M = D
    @13
    D = M
    @R2
    M = D
    @R0
    M = M + 1
    @THIS
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
    @THAT
    D = M
    @R0
    A = M
    M = D
    @R0
    M = M + 1
    D = M
    @R1
    M = D
    (returnAddress) 
return 
    @R1
    D = M
    @13 //endframe temp var
    M = D
    @R0
    A = M - 1
    D = M
    @R2
    A = M
    M = D
    D = A
    @R0
    M = A + 1
    @13
    A = M - 1
    D = M
    @THAT
    M = D
    @2
    D = A
    @13
    D = M - D
    @THIS
    M = D
    @3
    D = A
    @13
    D = M - D
    @R2
    M = D
    @4
    D = A
    @13
    D = M - D
    @R0
    M = D
    @5
    D = A
    @13
    A = M - D
    0;jmp
     
"""
# actual assembler code
import sys


def isLogic(line):
    # if the line starts with a p return False
    logicVals = [
        'add',
        'sub',
        'neg',
        'eq',
        'gt',
        'lt',
        'and',
        'or',
        'not'
    ]
    if line in logicVals:
        return True
    return False


def toAsm(line, filename, i):
    name = filename.split('.')
    type = line.split()
    id = i
    code = []
    logicDict = {
        'add': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'D = D + M\n', 'A = A + 1\n', 'M = 0\n', 'A = A - 1\n', 'M = D\n' '@R0\n', 'M = M -1\n'],
        'sub': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'D = D - M\n', 'A = A + 1\n', 'M = 0\n', 'A = A - 1\n', 'M = D\n'],
        'neg': ['@R0\n', 'A = M - 1\n', 'M = -M\n'],
        'eq': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'D = D - M\n', f'@equal_{id}\n', 'D;JEQ\n', '@R0\n', 'A = M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', 'M = 0\n', f'@next_{id}\n', '0;JMP\n', f'(equal_{id})\n', '@R0\n', 'A=M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', 'M = 1\n',  f'(next_{id})\n', '@R0\n', 'M = M - 1\n'],
        'gt': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'D = D - M\n', f'@greater_{id}\n', 'D;JGT\n', '@R0\n', 'A = M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', 'M = 0\n', '@R0\n', 'M = M - 1\n', f'@next_{id}\n', '0;JMP\n', f'(greater_{id})\n', '@R0\n', 'A=M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', f'(next_{id})\n'],
        'lt': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'D = M - D\n', f'@greater_{id}\n', 'D;JGT\n', '@R0\n', 'A = M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', 'M = 0\n', '@R0\n', 'M = M - 1\n', f'@next_{id}\n', '0;JMP\n', f'(greater_{id})\n', '@R0\n', 'A=M\n', 'A = A - 1\n', 'M = 0\n', 'A = A - 1\n', f'(next_{id})\n'],
        'and': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'M = D & M\n'],
        'or': ['@R0\n', 'A = M - 1\n', 'D = M\n', 'A = A - 1\n', 'M = D | M\n', '@R0\n', 'M = M - 1\n'],
        'not': ['@R0\n', 'A = M - 1\n', 'M = !M\n'],
    }

    if isLogic(line):
        code = logicDict[line.strip('\n')]
    elif line[0] == 'p':
        val = type[2]

        pushDict = {
            'push constant': [f'@{val}\n', 'D = A\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push local': ['@R1\n', 'D = M\n', f'@{val}\n', 'A = D + M\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push argument': ['@R2\n', 'D = M\n', f'@{val}\n', 'A = D + M\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push temp': ['@R5\n', 'D = M\n', f'@{val}\n', 'A = D + M\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push static': [f'@{name[0]}.{val}\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push pointer': [f'@{val}\n', 'D = A\n', '@R3\n', 'A = A + D\n', 'A = M\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push this': ['@R3\n', 'D = A\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
            'push that': ['@R4\n', 'D = A\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n'],
        }

        popDict = {
            'pop local': [f'@{val}\n', 'D = A\n', '@R1\n', 'D = D + M\n', '@R13\n', 'M = D\n', '@R0\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R13\n', 'A = M\n', 'M = D\n'],
            'pop argument': [f'@{val}\n', 'D = A\n', '@R2\n', 'D = D + M\n', '@R13\n', 'M = D\n', '@R0\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R13\n', 'A = M\n', 'M = D\n'],
            'pop temp': [f'@{val}\n', 'D = A\n', '@R5\n', 'D = D + M\n', '@R13\n', 'M = D\n', '@R0\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R13\n', 'A = M\n', 'M = D\n'],
            'pop static': [f'@{val}\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', f'@{name[0]}.{val}\n', 'M = D\n'],
            'pop pointer': [f'@{val}\n', 'D = A\n', '@R3\n', 'D = A + D\n', '@R13\n', 'M = D\n', '@R0\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R13\n', 'A = M\n', 'M = D\n'],
            'pop this': [f'@{val}\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R3\n', 'M = D\n'],
            'pop that': [f'@{val}\n', 'M = M - 1\n', 'A = M\n', 'D = M\n', '@R4\n', 'M = D\n'],
        }

        if type[0] == 'push':
            code = pushDict[type[0] + ' ' + type[1]]
        elif type[0] == 'pop':
            code = popDict[type[0] + ' ' + type[1]]
    else:
        if 'goto' in line:
            code = ['@' + line.strip('\n').split()[1] + '\n', '0;JMP\n']
        if 'label' in line:
            code = ['(' + line.strip('\n').split()[1] + ')\n']
        if 'if-goto' in line:
            code = ['@R0\n', 'A = M - 1\n',
                    'D = M\n', f'@{type[1]}\n', 'D;JNE\n']
        if 'function' in line:
            code = [f'({type[1]})\n']
            for i in range(int(type[2])):
                code.append('@R0\n')
                code.append('A = M\n')
                code.append('M = 0\n')
                code.append('@R0\n')
                code.append('M = M + 1\n')
        if 'call' in line:
            nArgs = type[2]
            funcName = type[1].split('.')[1]
            code = [f'@{nArgs}\n',  'D = A\n', '@R0\n', 'D = M - D\n', '@13\n', 'M = D\n', f'@returnAddress_{type[1]}\n', 'D = A\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@R0\n', 'D = M\n', '@R0\n',  'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@R2\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R13\n',
                    'D = M\n', '@R2\n', 'M = D\n', '@R0\n', 'M = M + 1\n',  '@THIS\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n',  '@THAT\n', 'D = M\n', '@R0\n',   'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', 'D = M\n', '@R1\n', 'M = D\n', f'@{funcName}\n', '0;JMP\n', f'(returnAddress_{type[1]})\n']
        if 'return' in line:
            code = ['@R1\n', 'D = M\n', '@13\n', 'M = D\n', '@R0\n', 'A = M - 1\n', 'D = M\n', '@R2\n' 'A = M\n', 'M = D\n', 'D = A\n', '@R0\n', 'M = A + 1\n', '@13\n', 'A = M - 1\n', 'D = M\n', '@THAT\n', 'M = D\n', '@2\n',  'D = A\n',
                    '@13\n', 'D = M - D\n', '@THIS\n', 'M = D\n', '@3\n', 'D = A\n', '@13\n', 'D = M - D\n', '@R2\n', 'M = D\n', '@4\n', 'D = A\n', '@13\n', 'D = M - D\n', '@R0\n', 'M = D\n', '@5\n',  'D = A\n',  '@13\n', 'A = M - D\n', '0;JMP\n']

    code.append('//' + line + '\n')
    code = code[-1:] + code[:-1]
    code.append('//end of ' + line + '\n')
    return code


def setupAsm():
    sp = ['//setup stack pointer\n', '@256\n', 'D=A\n', '@R0\n', 'M=D\n']
    mainCall = ['//call Main.main 0\n', '@0\n', 'D = A\n', '@R0\n', 'D = M - D\n', '@13\n', 'M = D\n', '@returnAddress_Sys.init\n', 'D = A\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@R0\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@R2\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R13\n', 'D = M\n', '@R2\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@THIS\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', '@THAT\n', 'D = M\n', '@R0\n', 'A = M\n', 'M = D\n', '@R0\n', 'M = M + 1\n', 'D = M\n', '@R1\n', 'M = D\n', '(returnAddress_Main.main)\n', '@init\n', '0;JMP\n', '//end of call Main.main 0\n']


    return sp + mainCall


def fileEnd():
    return ['(END)\n', '@END\n', '0;JMP\n']


def main():
    try:
        outfile, infile = sys.argv[1:]
    except:
        print('The format is incorrect expected 2 input arguments but recieved ' +
              str(len(sys.argv) - 1) + ' arguments')

    filename = 'vmToAsm/test.vm'

    try:
        file = open(filename, 'r')
    except FileNotFoundError as fnfError:
        print('File not found')
        print(fnfError)
        print('Make sure you don\'t have any typos')

    asmInstructions = setupAsm()
    wholefile = file.readlines()
    for i in range(len(wholefile)):
        line = wholefile[i]
        intruction = toAsm(line, filename, i)
        asmInstructions += intruction
    asmInstructions += fileEnd()
    file.close()
    try:
        outfile = open('vmToAsm/test.asm', 'w')
        outfile.writelines(asmInstructions)
        outfile.close()
        print('Assembly successful')
    except FileNotFoundError as fnfError:
        print('File not found')
        print(fnfError)
        print('Make sure you don\'t have any typos')


main()
