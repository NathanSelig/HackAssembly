//check if etheir number is negeitve if
@1_NEG
M = 0
@2_NEG
M = 0

@R0
D = M
@skipIgnore
D;JLT

(skip)
@R1
D = M
@loop
D;JGT

(skipIgnore)
@R0
D = M
@nextCheck
D;JGT
@1_NEG
M = 1

(nextCheck)
@R1
D = M
@next
D;JGT
@2_NEG
M = 1



(next)
//check if both are +
@1_NEG
D = M 
@2_NEG
D = M & D
@bothNEG
M = D

//check both neg
@1_NEG_CHECK
D;JEQ

@R0
M = -M
@R1
M = -M
@loop
0;JMP


(1_NEG_CHECK)
//check if only one is negetive
@1_NEG
D = M 
@2_NEG
D = D - M
@continueCheck_1_NEG
D;JEQ
@oneNEG
M = 1

//1 neg change
(continueCheck_1_NEG)
    //if 1_NEG is 1 then continue else jump bottomNEG
    @1_NEG
    D = M
    @bottomNEG
    D;JEQ

    //change top
    @R0
    M = -M
    @loop
    0;JMP

    //cnange bottom
    (bottomNEG)
    @R1
    M = -M


(loop)
    //check if x < y  
    @R0
    D = M
    @R1
    D = D - M
    @stop 
    D;JLT

    // take away y from x goto continue
    @R1
    D = M
    @R0
    M = M - D

    @R2 // increase i
    M = M + 1
    @loop
    0;JMP


(stop) 
    @oneNEG
    D = M
    @notNEG
    D;JEQ
    @R2
    M = -M

    (notNEG)
    @R0
    D = M
    @R3
    M = D
(END)
@END
0;JMP