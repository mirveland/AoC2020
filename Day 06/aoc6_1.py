declarationset = set({});

result = 0;

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\customsdeclarations.txt") as file:
    for line in file: #Go one step down
        line = line.strip().split(); #preprocess line
        #print(line);
        
        if (not line):
            #evaluate previous group
            print(declarationset);
            
            #no of unique question that was answered YES
            result += len(declarationset);
            
            declarationset = set({});
        else:
            declaration = line[0];
            
            for letter in declaration:
                declarationset.add(letter);
            #print(declarationset);
            
print(declarationset);
                        
result += len(declarationset);

print("Resultat: ", result," - det du!")
