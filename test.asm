@256
D=A
@R0
M=D
@1015
D=A
@R1
M=D
@2047
D=A
@R2
M=D
@17
D = A
@R0
A = M
M = D
@R0
M = M + 1
@17
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@equal_2
D;JEQ
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@next_2
0;JMP
(equal_2)
@R0
A=M
A = A - 1
M = 0
A = A - 1
M = 1
(next_2)
@R0
M = M - 1
@17
D = A
@R0
A = M
M = D
@R0
M = M + 1
@16
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@equal_5
D;JEQ
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@next_5
0;JMP
(equal_5)
@R0
A=M
A = A - 1
M = 0
A = A - 1
M = 1
(next_5)
@R0
M = M - 1
@16
D = A
@R0
A = M
M = D
@R0
M = M + 1
@17
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@equal_8
D;JEQ
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@next_8
0;JMP
(equal_8)
@R0
A=M
A = A - 1
M = 0
A = A - 1
M = 1
(next_8)
@R0
M = M - 1
@892
D = A
@R0
A = M
M = D
@R0
M = M + 1
@891
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = M - D
@greater_11
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_11
0;JMP
(greater_11)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_11)
@891
D = A
@R0
A = M
M = D
@R0
M = M + 1
@892
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = M - D
@greater_14
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_14
0;JMP
(greater_14)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_14)
@891
D = A
@R0
A = M
M = D
@R0
M = M + 1
@891
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = M - D
@greater_17
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_17
0;JMP
(greater_17)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_17)
@32767
D = A
@R0
A = M
M = D
@R0
M = M + 1
@32766
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@greater_20
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_20
0;JMP
(greater_20)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_20)
@32766
D = A
@R0
A = M
M = D
@R0
M = M + 1
@32767
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@greater_23
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_23
0;JMP
(greater_23)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_23)
@32766
D = A
@R0
A = M
M = D
@R0
M = M + 1
@32766
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
@greater_26
D;JGT
@R0
A = M
A = A - 1
M = 0
A = A - 1
M = 0
@R0
M = M - 1
@next_26
0;JMP
(greater_26)
@R0
A=M
A = A - 1
M = 0
A = A - 1
(next_26)
@57
D = A
@R0
A = M
M = D
@R0
M = M + 1
@31
D = A
@R0
A = M
M = D
@R0
M = M + 1
@53
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D + M
A = A + 1
M = 0
A = A - 1
M = D
@R0
M = M -1
@112
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
D = D - M
A = A + 1
M = 0
A = A - 1
M = D
@R0
A = M - 1
M = -M
@R0
A = M - 1
D = M
A = A - 1
M = D & M
@82
D = A
@R0
A = M
M = D
@R0
M = M + 1
@R0
A = M - 1
D = M
A = A - 1
M = D | M
@R0
A = M - 1
M = !M
(END)
@END
0;JMP
