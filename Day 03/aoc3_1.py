outerlineno = 0
position = 0;
trees = 0;
tree = "#"

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\skislope.txt") as outerfile:
    for outerline in outerfile: #Go one step down
        outerline = outerline.strip() #preprocess line
        
        print("Position: ", position, " ",outerline[position]);
        if (outerline[position] == tree): trees += 1;
        
        position += 3; #go 3 steps to the right
        
        if (position > 30):
            position -= 31; #repeat the line pattern
        
print("Antal träd på vägen ner: ", trees," - det du!")
