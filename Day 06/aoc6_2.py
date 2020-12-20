declarationset = set({});
baselineset = set({});
keeperset = set({});

firstperson = bool(True);

result = 0;

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\customsdeclarations.txt") as file:
    for line in file: #Go one step down
        line = line.strip().split(); #preprocess line
        #print(line);
        declarationset.clear();
        
        if (not line):
            #evaluate previous group
            print("result baseline: ",baselineset);
            
            #no of unique question that was answered YES
            result += len(baselineset);
            
            declarationset.clear();
            baselineset.clear()
            keeperset.clear();
            firstperson = True;
        else:
            declaration = line[0];
            
            for letter in declaration:
                declarationset.add(letter);
            
            if (firstperson == True):
                baselineset = declarationset.copy();
                keeperset   = declarationset.copy();
                print("baseline: ",keeperset);
                firstperson = False;
            else:
                print("declaration: ",declarationset);
                for baseline in baselineset:
                    print(baseline);
                    if baseline not in declarationset:
                        keeperset.remove(baseline);
                        print("keepers: ",keeperset);
                                        
                baselineset = keeperset.copy();
                
            #print("baseline: ",baselineset);
            
print("keepers: ",baselineset);
                        
result += len(baselineset);

print("Resultat: ", result," - det du!")
