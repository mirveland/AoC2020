def getSums(myList,target):
    sum = 0;
    j = 0;
    success = 0;
    lowest = 0;
    highest = 0;
    
    while success == 0 and j <= 1000:
        print(j);
        for item in myList[j:]:
            sum = sum+item; 
            if (lowest == 0 or item < lowest):
                lowest = item;
            
            if (item > highest):
                highest = item;
            
            print(sum);
            if sum > target:
                j += 1;
                sum = 0;
                highest = 0;
                lowest = 0;                
                break;
            elif sum == target:
                print("Disco!");
                print("Sum:",sum);
                print("Low:",lowest);
                print("High:",highest);
                print("Weakness:",lowest+highest);
                success = 1;
                break;
        
    return item;
    
myList = [];

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\cypher.txt") as cypher:
    for line in cypher: #Go one step down
        line = line.strip().split(); #preprocess line
        eNumber = int(line[0]);
        myList.append(eNumber);
        #print(myList);

            

        

print(getSums(myList,257342611));
        
