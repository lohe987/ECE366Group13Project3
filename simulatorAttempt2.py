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
        fetch = fetch.replace(" ", "")
        if(fetch[0:3]=="101"):   # init
            #fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5] ,2)
            imm = int(fetch[5:7] ,2)
            if (fetch[6:8] == "11"):
                imm = "-1"
            print("init R"+str(Rx) + ", " + str(imm))
        elif(fetch[0:3]=="000"):   # load
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("load R" + str(Rx) +", R" + str(Ry) + "")
        elif(fetch[0:3]=="001"):   # store
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("store R" + str(Rx) +", R" + str(Ry) + "")
        elif(fetch[0:3]=="010"):   # add
          #  fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("add R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:3]=="111"):   # xor
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("xor R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:3]=="100"):   # slt
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("slt R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:3]=="011"):   # beq
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[3:5],2)
            Ry = int(fetch[5:7],2)
            print("beq R" + str(Rx) +", R" + str(Ry) )
        elif(fetch[0:5]=="11010"):   # jump
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[5:7],2) 
            print("jump R" + str(Rx) )
        elif(fetch[0:5]=="11000"):   # slr
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[5:7],2) 
            print("slr R" + str(Rx) )
        elif(fetch[0:5]=="11001"):   # and
           # fetch = fetch.replace(" ", "")
            Rx = int(fetch[5:7],2) 
            print("and R" + str(Rx) )
        elif(fetch[0:5]=="11011"):   # not
          #  fetch = fetch.replace(" ", "")
            Rx = int(fetch[5:7],2) 
            print("not R" + str(Rx) )
        print()

def assemble(I,Nlines):
    print("ECE366 Fall 2018 ISA Design: Assembler")
    print("")
    
    for i in range(Nlines):
        fetch = I[i]
        print()
        #print(fetch)
        fetch = fetch.replace("R","")
        if (fetch[0:4] == "init"):
            fetch = fetch.replace("init ","")
            fetch = fetch.split(",")
            R = format(int(fetch[0]),"02b")
            imm = format(int(fetch[1]))
            if (imm == "-1"):
                imm = "11"
            elif (imm == "-2"):
                imm = "10"
            else:
                imm = format(int(fetch[1]),"02b")
            op = "101"
            print(op + " " + R + " " + imm)
            
        elif (fetch[0:4] == "add "):
            fetch = fetch.replace("add ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "010"
            print(op + " " + Rx + " " + Ry)

        elif (fetch[0:4] == "xor "):
            fetch = fetch.replace("xor ","")
            fetch = fetch.split(",")      
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "111"
            print(op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "load"):
            fetch = fetch.replace("load ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "000"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:5] == "store"):
            fetch = fetch.replace("store ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "001"
            print ( op + " " + Rx + " " + Ry)
        elif (fetch[0:4] == "slt "):  
            fetch = fetch.replace("slt ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "100"
            print ( op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "beq "):
            fetch = fetch.replace("beq ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            Ry = format(int(fetch[1]),"02b")
            op = "011"
            print(op + " " + Rx + " " + Ry)
            
        elif (fetch[0:4] == "jump"):
            fetch = fetch.replace("jump ","")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]),"02b")
            op = "110 10"
            print(op + " " + Rx)
        elif(fetch[0:4] == "slr "):
            fetch = fetch.replace("slr ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "110 00"
            print(op + " " + Rx)
        elif(fetch[0:4] == "and "):
            fetch = fetch.replace("and ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "110 01"
            print(op + " " + Rx)
        elif(fetch[0:4] == "not "):
            fetch = fetch.replace("not ", "")
            fetch = fetch.split(",")
            Rx = format(int(fetch[0]), "02b")
            op = "110 11"
            print(op + " " + Rx)


def simulate(I,Nsteps): #NEEDS TO BE DONE IN MACHINE CODE!!!
    print("ECE366 Fall 2018 ISA Design: Simulator")
    print()
    PC = 0              # Program-counter
    DIC = 0
    Reg = [0,0,0,0]     # 4 registers, init to all 0
    Memory = [0 for i in range(110)] # data memory, 10 spaces all init to 0.
    
    Memory = ["0000000000001001",
"0000000000010001",
"0000000000000000",
"0000000000000000",
"0000000000000000",
"0000000000000000",
"0000000000000000",
"0000000000000000",
"1111000010000001",
"1111000010000010",
"1111000010000011",
"1111000010000100",
"1111000010000101",
"1111000010000110",
"1111000010000111",
"1111000010001000",
"1111000010001001",
"1111000010001010",
"1111000010001011",
"1111000010001100",
"1111000010001101",
"1111000010001110",
"1111000010001111",
"1111000010010000",
"1111000010010001",
"1111000010010010",
"1111000010010011",
"1111000010010100",
"1111000010010101",
"1111000010010110",
"1111000010010111",
"1111000010011000",
"1111000010011001",
"1111000010011010",
"1111000010011011",
"1111000010011100",
"1111000010011101",
"1111000010011110",
"1111000010011111",
"1111000010100000",
"1111000010100001",
"1111000010100010",
"1111000010100011",
"1111000010100100",
"1111000010100101",
"1111000010100110",
"1111000010100111",
"1111000010101000",
"1111000010101001",
"1111000010101010",
"1111000010101011",
"1111000010101100",
"1111000010101101",
"1111000010101110",
"1111000010101111",
"1111000010110000",
"1111000010110001",
"1111000010110010",
"1111000010110011",
"1111000010110100",
"1111000010110101",
"1111000010110110",
"1111000010110111",
"1111000010111000",
"1111000010111001",
"1111000010111010",
"1111000010111011",
"1111000010111100",
"1111000010111101",
"1111000010111110",
"1111000010111111",
"1111000011000000",
"1111000011000001",
"1111000011000010",
"1111000011000011",
"1111000011000100",
"1111000011000101",
"1111000011000110",
"1111000011000111",
"1111000011001000",
"1111000011001001",
"1111000011001010",
"1111000011001011",
"1111000011001100",
"1111000011001101",
"1111000011001110",
"1111000011001111",
"1111000011010000",
"1111000011010001",
"1111000011010010",
"1111000011010011",
"1111000011010100",
"1111000011010101",
"1111000011010110",
"1111000011010111",
"1111000011011000",
"1111000011011001",
"1111000011011010",
"1111000011011011",
"1111000011011100",
"1111000011011101",
"1111000011011110",
"1111000011011111",
"1111000011100000",
"1111000011100001",
"1111000011100010",
"1111000011100011",
"1111000011100100"]
    print("******** Simulation starts *********")
    finished = False
    while(not(finished)):
        fetch = I[PC]
        DIC += 1
        print(fetch)
        fetch = fetch.split(" ") # Delete all the spaces to make things simpler
        if (fetch[0] == "101"): #init
            #fetch = fetch.replace("init ","") dont need I think
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            if (int(fetch[2] == "11")):
                imm = -1
            elif(int(fetch[2] == "10")):
                imm = -2
            else:
                imm = int(fetch[2],2)
            Reg[Rx] = imm
            PC += 1
        elif (fetch[0] == "010"): #add
            #fetch = fetch.replace("add ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            Reg[Rx] = int(Reg[Rx]) + int(Reg[Ry])
            PC += 1
        elif (fetch[0] == "111"):# xor
            #fetch = fetch.replace("xor ","")
            #fetch = fetch.split(",")      
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            Reg[Rx] = int(Reg[Rx]) ^ int(Reg[Ry])
            PC += 1
        elif (fetch[0] == "000"):# load
            #fetch = fetch.replace("load ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            Reg[Rx] = Memory[Reg[Ry]]
            print(Reg[Rx])
            PC += 1
        elif (fetch[0] == "001"):# store
            #fetch = fetch.replace("store ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            print (Reg[Ry])
            Memory[Reg[Ry]] = Reg[Rx]
            PC += 1
        elif (fetch[0] == "100"):# slt                        
            #fetch = fetch.replace("slt ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            if( Reg[Rx] < Reg[Ry] ):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0] == "011"):# beq
            #fetch = fetch.replace("beq ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[1],2)
            Ry = int(fetch[2],2)
            
            if ( Reg[Rx] == Reg[Ry]):
                PC = PC + 2
            else:
                PC += 1
        elif (fetch[0] == "110" and fetch[1] == "10" ):# jump
            #fetch = fetch.replace("jump ","")
            #fetch = fetch.split(",")
            Rx = int(fetch[2],2)
            if(Reg[Rx] == 0):
                finished = True
            else:
                PC = PC + Reg[Rx]
        elif (fetch[0] == "110" and fetch[1] == "00" ):# slr
            Rx = int(fetch[1],2)
            Reg[Rx] = int(Reg[Rx]) >> 1
            PC = PC + 1
        elif (fetch[0] == "110" and fetch[1] == "01" ):# and
            Rx = int(fetch[2],2)
            Reg[Rx] = int(Reg[Rx]) & 1
            PC = PC + 1
        elif (fetch[0] == "110" and fetch[1] == "11" ):# not
            Rx = int(fetch[2],base=2)
            Reg[Rx] = format(1111111111111111 - int(Reg[Rx]), '016')
            PC = PC + 1
        if ( (DIC % Nsteps) == 0):
            print("Registers R0-R3: ", Reg)
            print("Memory: ",Memory)
            print()
        
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    print("Memory :",Memory)


def main():
    input_file = open("Part2.2.txt","r")#Part2ISACodeWOComments Part2MachineCode
    debug_mode = False  # is machine in debug mode?  
    Nsteps = 1          # How many cycle to run before output statistics
    Nlines = 0          # How many instrs total in input.txt  
    Instruction = []    # all instructions will be stored here
    mode = 1            # 1 = Simulation 
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
