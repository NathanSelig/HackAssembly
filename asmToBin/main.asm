@i
M=1 
@sum
M=0 
(loop)
@i 
D=M 
@R0
D=D-M 
@stop
D;JGT
@sum
D=M 
@i
D=D+M 
@sum
M=D 
@i
M=M+1 
@loop
0;JMP
(stop)
@sum
D=M
@R1
M=D
(end)
@end
0;JMP