@i
M = 0
D = M
@R2 //set min to zero
M = 0
@R3 //set max to zero
M = 0

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
    D = A
    @tempAdress // take location and store it in tempAdress
    M = D

    //check if first pass
    @i
    D = M - 1
    @first 
    D;JEQ
//* not first pass

    @tempAdress // move to index of array
    A = M
    D = M // set D as value at index


    
    //check if larger then max
    @R3 // if + then D is larger then M
    D = D - M
    @checkSmall
    D;JLT
    (larger) // set new max
    @tempAdress
    A = M
    D = M // set D as value at index
    @R3
    M = D
    @continue
    0;JMP

    (checkSmall) 
    @tempAdress // move to index of array
    A = M
    D = M // set D as value at index
    //check if smaller then min
    @R2 // if + then D is smaller then R2 
    D = M - D
    @continue //continue if not smaller
    D;JLT
    @tempAdress
    A = M
    D = M // set D as value at index
    @R2
    M = D
    @continue
    0;JMP


    (first)
    @R0 // goto base because first pass
    A = M // moves to first adress
    D = M 
    @R2
    M = D
    @R3
    M = D
    @continue
    0;JMP


    (continue)
    @i // increase i
    M = M + 1
    @loop
    0;JMP

(stop)
@stop
0;JMP