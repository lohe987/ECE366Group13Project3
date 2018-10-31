# Authors: Trung Le, Wenjing Rao
# This program is a simulator packed with both assembler and disassembler.
# Simulator has 2 modes:
#            Debug mode:  Execute program every # steps and
#                         output the state of each reg, and PC
#            Normal mode: Execute program all at once

def disassemble(I,Nlines):
    print("ECE366 Fall 2018 ISA Design: Disassembler")
    print("")
    #print(I)

    for i in range(Nlines):
        fetch = I[i]
        print(fetch)
        if(fetch[0:4]=="0101"):   # init
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6] ,2)
            imm = int(fetch[6:8] ,2)
            if (fetch[6:8] == "11"):
                imm = "-1"
            print("init R"+str(Rx) + ", " + str(imm))
        elif(fetch[0:4]=="1000"):   # load
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("load R" + str(Rx) +", R" + str(Ry) + "")
        elif(fetch[0:4]=="0001"):   # store
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("store R" + str(Rx) +", R" + str(Ry) + "")
        elif(fetch[0:4]=="0010"):   # add
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("add R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:4]=="0111"):   # xor
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("xor R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:4]=="1100"):   # slt
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("slt R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:4]=="1011"):   # beq
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8],2)
            print("beq R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:6]=="111010"):   # jump
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[6:8],2) 
            print("jump R" + str(Rx) )
        elif(fetch[0:6]=="011000"):   # slr
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[6:8],2) 
            print("slr R" + str(Rx) )
        elif(fetch[0:6]=="011001"):   # and
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[6:8],2) 
            print("and R" + str(Rx) )
        elif(fetch[0:6]=="111011"):   # not
            fetch = fetch.replace(" ", "")
            Rx = int(fetch[6:8],2) 
            print("not R" + str(Rx) )
        print()

def assemble(I,Nlines):
    print("ECE366 Fall 2018 ISA Design: Assembler")
    print("")
    
    for i in range(Nlines):
        fetch = I[i]
        print()
        print(fetch)
        fetch = fetch.replace("R","")
        if (fetch[0:4] == "init"):
            fetch = fetch.replace("init ","")
            fetch = fetch.split(",")
            R = format(int(fetch[0]),"02b")
            imm = format(int(fetch[1]),"02b")
            if (imm == "-1"):
                imm = "11"
            else:
                imm = imm
            op = "0101"
            print(op + " " + R + " " + imm)
            
        elif (fetch[0:4] == "add "):
            fetch = fetch.replace("add ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0010"
            print(op + " " + Rx + " " + Ry)

        elif (fetch[0:4] == "xor "):
            fetch = fetch.replace("xor ","")
            fetch = fetch.split(",")      
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0111"
            print(op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "load"):
            fetch = fetch.replace("load ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "1000"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:5] == "store"):
            fetch = fetch.replace("store ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "0001"
            print ( op + " " + Rx + " " + Ry)
        elif (fetch[0:4] == "slt "):  
            fetch = fetch.replace("slt ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "1100"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "beq "):
            fetch = fetch.replace("beq ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "1011"
            print(op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            op = "111010"
            print(op + " " + Rx)
        elif(fetch[0:4] == "slr "):
            fetch = fetch.replace("slt ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "011000"
            print(op + " " + Rx)
        elif(fetch[0:4] == "and "):
            fetch = fetch.replace("and ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "011001"
            print(op + " " + Rx)
        elif(fetch[0:4] == "not "):
            fetch = fetch.replace("not ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "111011"
            print(op + " " + Rx)


def simulate(I,Nsteps):
    print("ECE366 Fall 2018 ISA Design: Simulator")
    print()
    PC = 0              # Program-counter
    DIC = 0
    Reg = [0,0,0,0]     # 4 registers, init to all 0
    Memory = [0 for i in range(10)] # data memory, 10 spaces all init to 0.
    print("******** Simulation starts *********")
    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        fetch = fetch.replace("R","")       # Delete all the 'R' to make things simpler
        if (fetch[0:4] == "init"):
            fetch = fetch.replace("init ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = imm
            PC += 1
        elif (fetch[0:4] == "addi"):
            fetch = fetch.replace("addi ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[0:4] == "add "):
            fetch = fetch.replace("add ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "sub "):
            fetch = fetch.replace("sub ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] - Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "xor "):
            fetch = fetch.replace("xor ","")
            fetch = fetch.split(",")      
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "load"):
            fetch = fetch.replace("load ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[0:4] == "stre"):
            fetch = fetch.replace("stre ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[0:4] == "slt0"):  # why "slt0" instead of "sltR0" ? 
                                    # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("slt0 ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0:4] == "bez0"):
            fetch = fetch.replace("bez0 ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            if ( Reg[0] == 0):
                PC = PC + imm
            else:
                PC += 1
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            PC = PC + imm
        elif(fetch[0:6] == "finish"):
            finished = True
        if ( (DIC % Nsteps) == 0):
            print("Registers R0-R3: ", Reg)
            print("Memory: ",Memory)
            print()
        
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    print("Memory :",Memory)


def main():
    input_file = open("Part1MachineCode.txt","r")#Part2ISACodeWOComments Part2MachineCode
    debug_mode = False  # is machine in debug mode?  
    Nsteps = 3          # How many cycle to run before output statistics
    Nlines = 0          # How many instrs total in input.txt  
    Instruction = []    # all instructions will be stored here
    mode = 2            # 1 = Simulation 
                        # 2 = disassembler
                        # 3 = assembler
    for line in input_file:
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.replace("\n","")
        Instruction.append(line)                        # Copy all instruction into a list
        Nlines +=1

    if(mode == 1):   # Check wether to use disasembler or assembler or simulation 
        simulate(Instruction,Nsteps)
    elif(mode == 2):
        disassemble(Instruction,Nlines)
    else:
        assemble(Instruction,Nlines)

    
    
    
if __name__ == "__main__":
    main()
