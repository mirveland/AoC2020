def evaluatePassword(inLine):
    [rule,letterPart,password] = inLine.split()
    
    [minOccStr,maxOccStr] = rule.split('-')
    letter = letterPart.rstrip(':')
    
    minOcc = int(minOccStr)
    maxOcc = int(maxOccStr)
    
    numOcc = password.count(letter)
    
    if (numOcc <= maxOcc and numOcc >= minOcc):
        return 1
        
    return 0

counter = 0

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\passwords.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        counter += evaluatePassword(line)
        
print("Antal korrekta lösenord: ", counter," - det du!")
