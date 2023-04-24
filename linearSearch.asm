@i
M = 0
D = M
(loop)
    @i
    D = M
    @R1 
    D = D - M
    @stop
    D;JGE
    @R0 // goto base
    D = M 
    @i
    A = D + M // find location from base


    //stop when M of A = equal to R2 set R3 = 1
    D = M
    @R2
    D = D - M
    @continue
    D;JGT
    @R3
    M = 1

    (continue)
    @i // increase i
    M = M + 1
    @loop
    0;JMP
(stop)
@stop
0;JMP