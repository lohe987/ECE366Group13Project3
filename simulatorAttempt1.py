

def Disassembler
    import collections

    def check_parity_bit(machine_line):
        # Count the number of zeros and ones
        one_zero_dict = collections.Counter(machine_line)
        # Make sure an even number of ones exist in the instructions
        if one_zero_dict["1"] % 2 == 0:
            return True
        return False

    def determine_function(machine_line):
        if machine_line[1:4] == "110":
            return single_register(machine_line)
        elif machine_line[1:4] == "101":
            return imm_value(machine_line)
        else:
            return double_register(machine_line)

    def single_register(machine_line):
        op_code = {"10" : "jump",
                   "00" : "slr",
                   "01" : "and",
                   "11" : "not"}
        # Determine function code
        asm_line = op_code.get(machine_line[4:6], "UNKNOWN")
        # Add register values
        asm_line += " " + registers_bin_text.get(machine_line[6:8], "??")
        return asm_line

    def imm_value(machine_line):
        value = {"11" : "-2",
                 "10" : "-1",
                 "00" : "0",
                 "01" : "1"}
        # Add function word and register
        asm_line = "init" + " " + registers_bin_text.get(machine_line[4:6], "??") + ", "
        # Find imm value in table
        asm_line += value.get(machine_line[6:8], "??")
        return asm_line

    def double_register(machine_line):
        func_code = {"000" : "load",
                     "001" : "store",
                     "010" : "add",
                     "011" : "beq",
                     "100" : "slt",
                     "111" : "xor"}
        # Add function code to begining of assembler line
        asm_line = func_code.get(machine_line[1:4], "UNKNOWN")
        # Update with register values
        asm_line += " " + registers_bin_text.get(machine_line[4:6], "??") + ", " + registers_bin_text.get(machine_line[6:8], "??")
        return asm_line

    def disassemble_file(input_file_name="CTZ_machine_code.txt", output_file_name="CTZ_instructions_decoded.txt"):
        # Open files using default args or user provided
        input_file = open(input_file_name, "r")
        output_file = open(output_file_name, "w")

        # For each line in input file process the function
        for line in input_file:
            # Remove new line for line
            line = line.replace("\n", "")

            comment = ""
            asm_line = ""
            index = line.find("#")
            if index > -1:
                comment = line[index:]
                line = line[0:index]

            if len(line) > 0:
                if check_parity_bit(line):
                    asm_line = determine_function(line)
                else:
                    asm_line = "PARITY ERROR"

            output_file.write(asm_line + " " + comment + "\n")

        input_file.close()
        output_file.close()

    registers_bin_text = {"00" : "R0",
                      "01" : "R1",
                      "10" : "R2",
                      "11" : "R3"}

    if __name__ == "__main__":
        input_file_1 = "project2_group_11_p1_bin.txt"
        output_file_1 = "project2_group_11_p1_asm.txt"
        input_file_2 = "project2_group_11_p2_bin.txt"
        output_file_2 = "project2_group_11_p2_asm.txt"
        disassemble_file(input_file_2, output_file_2)
def Assembler
    import collections

    def instr_load(line):
        # 000 RX RY
        if line[0] != "load":
            return "ERROR LINE CANNOT BE PARSED"
        else:
            return "000" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_store(line):
        # 001 RX RY
        if line[0] != "store":
            return "ERROR LINE CANNOT BE PARSED"
        else:
            return "001" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_add(line):
        # 010 RX RY
        if line[0] != "add":
            return "ERROR LINE CANNOT BE PARSED"
        else:
            return "010" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_branch(line):
        # 011 RX RY
        if line[0] != "beq":
            return "ERROR LINE CANNOT BE PARSED"
        else:
            return "011" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_jump(line):
        # 110 10 RR
        return "110" + "10" + registers.get(line[1], "??")

    def instr_init(line):
        # 101 RR ii
        return "101" + registers.get(line[1], "??") + convert_imm_value(line[2])[-2:]

    def instr_slr(line):
        # 110 00 RR
        return "110" + "00" + registers.get(line[1], "??")

    def instr_and(line):
        # 110 01 RR
        return "110" + "01" + registers.get(line[1], "??")

    def instr_slt(line):
        # 100 RX RY
        return "100" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_xor(line):
        # 111 RR RR
        return "111" + registers.get(line[1], "??") + registers.get(line[2], "??")

    def instr_not(line):
        # 110 11 RR
        return "110" + "11" + registers.get(line[1], "??")

    def add_praity_bit(encoded_line):
        # Adds even parity bit to encoded_line
        # Count the number of zeros and ones in the encoded line
        one_zero_dict = collections.Counter(encoded_line)
        # If number of ones is odd at 1 as the parity bit
        if one_zero_dict["1"] % 2 == 1:
            return "1" + encoded_line
        else:
            return "0" + encoded_line

    def convert_imm_value(number):
        if int(number) < 0:
            number = 0xFFFF - int(number[1:]) + 1
        return format(int(number), "016b")

    def assemble_file(input_file_name="CTZ_instructions.txt", output_file_name="CTZ_machine_code.txt"):
        # Open files using default args or user provided
        input_file = open(input_file_name, "r")
        output_file = open(output_file_name, "w")

        # For each line in input file process the function
        for line in input_file:
            old_line = line
            comment = ""
            func = "?"
            if line.find("#") > -1:
                comment = line[line.find("#"):]
                comment = comment.strip("\n")

            # Remove comments from code
            line = line.strip()
            if line.startswith("#"):
                output_file.write(line + "\n")
            elif len(line) < 1:
                output_file.write("\n")
            else:
                line = line.replace(",", " ")
                line = line.replace("\n", "")
                line = line.replace("\t", " ")
                line = line.split(" ")
                line = list(filter(None, line))
                func = instructions.get(line[0], "?")
                 # Check if function is known if not print error message
                if func == "?":
                    output_file.write("UNKNOWN\n")
                else:
                    # Encode function then add praity bit
                    encoded = add_praity_bit(func(line))
                    output_file.write(encoded + " " + comment + "\n")

        input_file.close()
        output_file.close()



    instructions = {"load" : instr_load,
                   "store" : instr_store,
                   "add" : instr_add,
                   "beq" : instr_branch,
                   "jump" : instr_jump,
                   "init" : instr_init,
                   "and" : instr_and,
                   "slt" : instr_slt,
                   "slr" : instr_slr,
                   "not" : instr_not,
                   "xor" : instr_xor}

    registers = {"R0" : "00",
                 "R1" : "01",
                 "R2" : "10",
                 "R3" : "11",
                 "r0" : "00",
                 "r1" : "01",
                 "r2" : "10",
                 "r3" : "11"}


    if __name__ == "__main__":
        input_file_name = "Program1.txt"
        output_file_name = "project2_group_11_p1_bin.txt"
        assemble_file(input_file_name, output_file_name)
