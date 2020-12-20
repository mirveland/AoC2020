def evaluateSum(outLine, inLine):
    match = bool(False);
    
    [outVal] = outLine.split()
    [inVal] = inLine.split()
    
    if (int(outVal) + int(inVal) == 2020):
        product = int(outVal) * int(inVal);
        print("Produkten av ",outVal," och ",inVal," är: ", product," - det du!")
        match = True;
        
    return match;

done = 0
outerlineno = 0
counter = 0;

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\expensereport.txt") as outerfile:
    for outerline in outerfile:
        outerlineno += 1;
        outerline = outerline.strip() #preprocess line
        innerlineno = 0;
        with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\expensereport.txt") as innerfile:
            for innerline in innerfile:
                innerlineno += 1;
                innerline = innerline.strip()
                
                if (outerlineno != innerlineno):
                    counter += 1;
                    done = evaluateSum(outerline, innerline)
                
                if (done):
                    print("Inner line no: ",innerlineno);
                    break;
                
        if (done):
            print("Outer line no: ",outerlineno);
            break;
                
        
print("Antal genomförda beräkningar: ", counter," - det du!")
