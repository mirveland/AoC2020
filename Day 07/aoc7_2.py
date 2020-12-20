goldenstar = "shiny gold bag";
bagcounter = 0;
globalPrefix = "";
bagDict = dict({});

totalNumberOfBags = 0;
containNoOfBags = 0;

def populateBagDict(inLine):
    match = bool(False);
    bagContentSet = set({});
    inLine = inLine.strip().strip(".");
    [color,inLine] = inLine.split(" contain ")
    bagContentSet = inLine.split(", ");
    
    color = color.rstrip("s");
    
    bagDict[color] = bagContentSet; #Add key value pair of color and the contents
    
    return 1;

def countBagsInColor(localColor):
    doContainGoldenStar = bool(False);
    colorTotalNumberOfBags = 0;
    localBagContentSet = bagDict[localColor];
    global globalPrefix;
    globalPrefix = globalPrefix + "----";
    print(globalPrefix,localColor," ",localBagContentSet);
    
    for contents in localBagContentSet:
        contentBags = 0;
        
        if(contents != "no other bags"):
            contents = contents.rstrip("s");
            contentBags = int(contents[0]);
            contentColor = contents[2:];
            #print(globalPrefix,contentColor," ",contentBags);
            returnValue = countBagsInColor(contentColor);
            
            if(returnValue):
                print(globalPrefix,"adding ",(contentBags * returnValue)," for ",  contentColor);
                colorTotalNumberOfBags += (contentBags * returnValue) + contentBags;
            else:
                print(globalPrefix,"adding ",contentBags," for ",  contentColor);
                colorTotalNumberOfBags += contentBags;
    
    globalPrefix = globalPrefix[:len(globalPrefix)-4];
    print(globalPrefix,"Total: ", colorTotalNumberOfBags," in bags with color: ",localColor);
    return colorTotalNumberOfBags;
                    
    
with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\bags.txt") as file:
    for line in file:
        line = line.strip() #preprocess line
        
        bagcounter += populateBagDict(line);
        
totalNumberOfBags = countBagsInColor(goldenstar);

print("Antal väskor som en Shiny gold bag innehåller: ", totalNumberOfBags)
