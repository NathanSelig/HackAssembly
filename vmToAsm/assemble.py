""" 
stack from  255-1014
lcl from    1015

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

"""