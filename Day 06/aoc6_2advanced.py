declarationset = set({});
baselineset = set({});

firstperson = bool(True);

result = 0;

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\customsdeclarations.txt") as file:
    for line in file: #Go one step down
        line = line.strip().split(); #preprocess line
        declarationset.clear();
        
        if (not line):
            #evaluate previous group
            
            #no of unique question that was answered YES
            result += len(baselineset);
            
            declarationset.clear();
            baselineset.clear()
            firstperson = True;
        else:
            declaration = line[0];
            
            for letter in declaration:
                declarationset.add(letter);
            
            if (firstperson == True):
                baselineset = declarationset.copy();
                firstperson = False;
            else:
                baselineset.intersection_update(declarationset);
                
                
            #print("baseline: ",baselineset);
            
print("keepers: ",baselineset);
                        
result += len(baselineset);

print("Resultat: ", result," - det du!")
