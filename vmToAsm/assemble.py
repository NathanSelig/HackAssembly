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

"""

#actual assembler code