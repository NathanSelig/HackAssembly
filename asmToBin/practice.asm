@i
M = 0
D = M
(loop)
    @i
    D = M
    @R1 
    D = D - M
    @stop
    D;JGT
    @R0 // goto base
    D = M 
    @i
    A = D + M // find location from base
    M = -1 // set value to -1
    @i // increase i
    M = M + 1
    @loop
    0;JMP
(stop)
@stop
0;JMP