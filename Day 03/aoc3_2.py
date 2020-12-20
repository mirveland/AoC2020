slopes = ["1-1","3-1","5-1","7-1","1-2"];

tree = "#";
treesperslope = []

for slope in slopes:
    [right,down] = slope.split('-');
    print("Slope: ", right, "-",down);
    line = 0;
    with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\skislope.txt") as outerfile:
        for outerline in outerfile: #Go one step down
            if (line == 0):
                trees = 0;
                position = 0;
            elif (divmod(line, int(down))[1] == 0):
                position += int(right); #go x steps to the right
                
                if (position > 30):
                    position -= 31; #repeat the line pattern
                
                outerline = outerline.strip() #preprocess line
                if (outerline[position] == tree): trees += 1;
                
            line += 1;

    treesperslope.append(trees);

product = 1;       
for treeresult in treesperslope:
    print("Antal träd på vägen ner: ", treeresult," - det du!")
    product = product * treeresult;
    
print("Produkten är: ", product," - det du!")
