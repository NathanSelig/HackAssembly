""" 
stack from 255-2047

push    [int or var]
    D = input
    @R0
    A = M
    M = D
    @R0
    M = M + 1
    
pop     [int or var]
    @R0
    A = M - 1
    output = M
    @R0
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
    A = A + 1
    A = 0 
    @next
    0;JMP
    (equal) 
    A = A + 1
    A = 1 
    (next)
gt
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = D - M
    @greater
    D;JGE
    @R0
    A = M
    A = A + 1
    M = 0
    @next
    0;JMP
    (greater)
    @R0
    A = M
    A = A + 1
    M = 1
    (next)
    A = A + 1
lt
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = M - D
    @greater
    D;JGE
    @R0
    A = M
    A = A + 1
    M = 0
    @next
    0;JMP
    (greater)
    @R0
    A = M
    A = A + 1
    M = 1
    (next)
    A = A + 1
and
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = D & M
    @R0
    A = A + 1
    D = M 
    A = A + 1
or
    @R0
    A = M - 1
    D = M
    A = A - 1
    D = D | M
    @R0
    A = A + 1
    D = M
    A = A + 1
not
    @R0
    A = M - 1
    M = !M
    A = A + 1
"""