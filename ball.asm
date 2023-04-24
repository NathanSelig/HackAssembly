@PIXELS
M = 0
@8192
D = A
@SIZE
M = D
@X_move
M = 1
@Y_move
M = -1
@32
D = A
@width
M = D
(mainLoop)
    
//i is the current word in the screen
    @i 
    M = 0

    (loop)
    // 8192 words in the screen 1 word is 16bit
    // if edge reverse x,y move using -M
        
        @i
        D = M
        @SIZE
        D = D - M
        @reset 
        D;JEQ

//center is (128 * 32) / 2 + 16 so word  + 16
        //calc position of ball x is simple y is times 512
            @X_move
            D = M
            @width
            D = D + M
            @loc
            M = D + M

        //end of loc calc
        




        @SCREEN//go to base
        D = A
        @loc //loc is relitive to base
        A = M + D
        M = -1
        //check if hit wall ifso switch xmove and ymove

        @i 
        M = M + 1
        @loop
        0;JMP
        

    (reset) 
    @KBD
    A = A - 1
    M = 0
    @mainLoop
    0;JMP
(stop)
@stop
0;JMP
//divide function takes input from r0 and r1 ouput r2,r3
(DIV)
    (DIV_loop)
        //check if x < y  
        @R0
        D = M
        @R1
        D = D - M
        @DIV_RTN
        D;JLT
        // take away y from x goto continue
        @R1
        D = M
        @R0
        M = M - D
        @R2 // increase i
        M = M + 1
        @DIV_loop
        0;JMP
(DIV_RTN)
    @R0
    D = M
    @R3
    M = D
    @DIV_CALL
    0;JMP



//product funtion takes in from r0,r1 output r2
(PROD)
    //check if etheir number is negeitve if
    @1_NEG_prod
    M = 0
    @2_NEG_prod
    M = 0


    @R0
    D = M
    @nextCheck_prod
    D;JGT
    @1_NEG_prod
    M = 1

    (nextCheck_prod)
    @R1
    D = M
    @next_prod
    D;JGT
    @2_NEG_prod
    M = 1

    (next_prod)
    //check if both are +
    @1_NEG_prod
    D = M 
    @2_NEG_prod
    D = M & D
    @bothNEG_prod
    M = D
    //check both neg
    @1_NEG_CHECK_prod
    D;JEQ

    @R0
    M = -M
    @R1
    M = -M
    @loop_prod
    0;JMP


    (1_NEG_CHECK_prod)
    //check if only one is negetive
    @1_NEG_prod
    D = M 
    @2_NEG_prod
    D = D - M
    @continueCheck_1_NE_prod
    D;JEQ
    @oneNEG_prod
    M = 1

    //1 neg change
    (continueCheck_1_NEG_prod)
        //if 1_NEG is 1 then continue else jump bottomNEG
        @1_NEG_prod
        D = M
        @bottomNEG_prod
        D;JEQ

        //change top
        @R0
        M = -M
        @loop_prod
        0;JMP

        //cnange bottom
        (bottomNEG_prod)
        @R1
        M = -M



    @i_prod
    M = 0
    D = M
    (loop_prod)
        @i_prod
        D = M
        @R1 
        D = D - M
        @stop_prod
        D;JGE
        @R0
        D = M
        @R2
        M = M + D
        @i_prod // increase i
        M = M + 1
        @loop_prod
        0;JMP


    (stop_prod) 
        @oneNEG_prod
        D = M
        @END_prod
        D;JEQ
        @R2
        M = -M
    (END_prod)
    @PROD_Call
    0;JMP