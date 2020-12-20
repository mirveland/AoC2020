linesRunSet = set({});
testedLinesSet = set({});
program = list([]);    
acc = 0;
i = 0;
    
def buildProgram(codeLine):
    program.append(codeLine.split());
    
def runProgram():
    ret = bool(False);
    global i;
    global acc;
    global program;
    global testedLinesSet;
    global linesRunSet;
    linesRunSetBackup = set({});
    
    programBackup = program.copy();
    
    lineNum = 0;
    
    while ret == False:
        program = programBackup.copy();
        if (len(linesRunSet)):
            if (not len(linesRunSetBackup)):
                linesRunSetBackup = linesRunSet.copy();
        
            for line in linesRunSetBackup:
                if line not in testedLinesSet:
                    [cmd,value] = program[line];
                    
                    if cmd == "jmp":
                        program[line] = ["nop", value];
                    elif cmd == "nop":
                        program[line] = ["jmp", value];
                    
                    testedLinesSet.add(line);
                    if cmd != "acc": break;
                
        i += 1;
        acc = 0;
        linesRunSet.clear();
        
        ret = runCodeLine(lineNum);
        
        #if i >= 74: break;
        
    print(testedLinesSet);
        
        
def runCodeLine(lineNum):
    global acc;
    global i;
    
    if lineNum >= len(program):
        print("HURRA! - programmet kördes till slutet.");
        print("Linenum is: ",lineNum);
        print("acc variable is: ",acc);
        return True;
        
    elif lineNum in linesRunSet:
        print("Linenum is: ",lineNum);
        print("acc variable is: ",acc);
        
    else:    
        linesRunSet.add(lineNum);
        #print(lineNum);
        [cmd,value] = program[lineNum];
        
        #print(program[lineNum]);
        #print(cmd);
        #print(value);
        #print(acc);
        #print(lineNum);
        #i+=1;
        #if (i >= 36):
        #    return 0;
            
        localLineNum = lineNum;
        
        if cmd == "acc":
            acc += int(value);
            localLineNum += 1;
            
        elif cmd == "jmp":
            localLineNum += int(value);
        elif cmd == "nop":
            localLineNum += 1;
        else:
            print("ERROR - unknown command");
            return False;
            
        return runCodeLine(localLineNum);

    return False;
    
    
with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\program.txt") as file:
    for fileline in file:
        fileline = fileline.strip(); #preprocess line
        buildProgram(fileline);
        
runProgram();
print(linesRunSet);
print("End of program");