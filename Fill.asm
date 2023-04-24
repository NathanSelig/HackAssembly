@PIXEL
M = 0
@8192
D = A
@SIZE
M = D
@21845
D = A
@pattern
M = D

(mainLoop)

    @i 
    M = 0
    @SCREEN
    D = A
    @j
    M = D


    @KBD
    D = M
    @white
    D;JEQ 


    (loop)

    // 8192 words in the screen 1 word is 16bit
        
        @i
        D = M
        @SIZE
        D = D - M
        @continue
        D;JEQ



        @pattern
        D = M
        @j
        A = M
        M = D

       
        

        @i 
        M = M + 1
        @j 
        M = M + 1
        @loop
        0;JMP
        

    (white)
    //set screen to white
        @i
        D = M
        @SIZE
        D = D - M
        @continue
        D;JEQ



        @SCREEN
        D = A
        @i
        A = D + M
        M = 0
        

        @i 
        M = M + 1
        @white
        0;JMP
        

    (continue) 
    @mainLoop
    0;JMP
(stop)
@stop
0;JMP