def evaluateSum(outLine, inLine, spinLine):
    match = bool(False);
    
    [outVal] = outLine.split()
    [inVal] = inLine.split()
    [spinVal] = spinLine.split()
    
    if (int(outVal) + int(inVal) + int(spinVal) == 2020):
        product = int(outVal) * int(inVal) * int(spinVal);
        print("Produkten av ",outVal," och ",inVal," och ",spinVal," är: ", product," - det du!")
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
                spinnerlineno = 0;
                if (outerlineno != innerlineno):
                    with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\expensereport.txt") as spinnerfile:
                        for spinnerline in spinnerfile:
                            spinnerlineno += 1;
                            spinnerline = spinnerline.strip()
                            
                            if (spinnerlineno != outerlineno and
                                spinnerlineno != innerlineno):
                                    counter += 1;
                                    done = evaluateSum(outerline, innerline, spinnerline)

                                    if (done):
                                        print("Spinner line no: ",spinnerlineno);
                                        break;
                
                if (done):
                    print("Inner line no: ",innerlineno);
                    break;
                
        if (done):
            print("Outer line no: ",outerlineno);
            break;
                
        
print("Antal genomförda beräkningar: ", counter," - det du!")
