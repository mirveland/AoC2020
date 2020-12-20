def evaluatePassword(inLine):
    match = bool(False);
    
    [rule,letterPart,password] = inLine.split()
    
    [minOccStr,maxOccStr] = rule.split('-')
    letter = letterPart.rstrip(':')
    
    minOcc = int(minOccStr)-1
    maxOcc = int(maxOccStr)-1
    
    #numOcc = password.count(letter)
    #print(password[minOcc-1:minOcc-1+1])
    #print(password[maxOcc-1:maxOcc-1+1])
    if (password[minOcc:minOcc+1] == letter):
        match = True;
        
    if (password[maxOcc:maxOcc+1] == letter):
        match = not match;
            
                
    return 1 if match == 1 else 0;

counter = 0

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\passwords.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        counter += evaluatePassword(line)
        
        
print("Antal korrekta lösenord: ", counter," - det du!")
