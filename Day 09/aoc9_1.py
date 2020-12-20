def getSums(myList,target):
    l_ = len(myList);
    sums = [];
    
    for i in range(len(myList)):
        for item in myList[i:]:
            sums.append((myList[i],item,myList[i]+item));
    return [x for x in sums if x[2]==target];
    
i = 0;
myList = [];
resultList = [];

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\cypher.txt") as cypher:
    for line in cypher: #Go one step down
        line = line.strip().split(); #preprocess line
        eNumber = int(line[0]);
        
        if i >= 25:
            resultList = getSums(myList,eNumber);
            print(resultList);
            
            if not resultList:
                print("Illegal value:", eNumber, "on line",i);
               
                break;
                
            myList.pop(0);
        
        
        myList.append(eNumber);
        print(myList);
        #print(len(myList));

        i += 1;
        
