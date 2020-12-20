def populateBagDict(inLine):
    match = bool(False);
    bagContentSet = set({});
    inLine = inLine.strip().strip(".");
    [color,inLine] = inLine.split(" contain ")
    bagContentSet = inLine.split(", ");
    
    color = color.rstrip("s");
    
    bagDict[color] = bagContentSet; #Add key value pair of color and the contents
    
    return 1;

def processColor(localColor):
    doContainGoldenStar = bool(False);
    
    #check just to make sure everything is ok
    if not localColor in bagDict:
        print("Missing color: ", localColor);
        rejectedColorsSet.add(localColor);
    else:
        if(localColor not in rejectedColorsSet
            and localColor not in goldenstarSet):
            
            localBagContentSet = bagDict[localColor];

            for contents in localBagContentSet:
                if(contents == "no other bags"):
                    rejectedColorsSet.add(localColor);
                else:
                    contents = contents.rstrip("s");
                    contentColor = contents[2:];
            
                    if(contentColor == goldenstar
                        or processColor(contentColor)):
                        print("HIT!!");
                        doContainGoldenStar = True;
                        break;
                        
        if(doContainGoldenStar):
            goldenstarSet.add(localColor);
        elif localColor in goldenstarSet:
            doContainGoldenStar = True;
        
    return doContainGoldenStar;
                    
    
goldenstar = "shiny gold bag";
bagcounter = 0;
hitcounter = 0;
bagDict = dict({});
bagDictView = set([]);

rejectedColorsSet = set([]);
goldenstarSet = set([]);

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\bags.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        
        bagcounter += populateBagDict(line)
        
for color in bagDict:
    if(processColor(color)):
        goldenstarSet.add(color);
        
print(rejectedColorsSet);
print(goldenstarSet);
hitcounter = len(goldenstarSet);

print("Antal avvisade färger: ", len(rejectedColorsSet))
print("Antal processade färger: ", bagcounter)
print("Antal väskor som Shiny gold bag kan finnas i: ", hitcounter)
