def processList(myList):
    currentLevel,lowDiff, highDiff = 0, 0, 1 #highDiff starts on 1 since my device is included.
    print(myList)

    for joltage in sorted(myList):
        diff = joltage - currentLevel
        currentLevel = joltage

        print(joltage, diff)

        if (diff == 1):
            lowDiff += 1
        elif (diff == 3):
            highDiff += 1

    return [lowDiff, highDiff]
    
i = 0
adapterList = []
low, high = 0, 0

with open("C:\\Users\\MattiasIrveland\\Documents\\Source\\Repos\\AdventOfCode2020\\Day 10\\adapters.txt") as adapters:
    for line in adapters: #Go one step down
        line = line.strip().split() #preprocess line
        adapter = int(line[0])
        adapterList.append(adapter)

[low,high] = processList(adapterList)

print("Diff of 1:", low, "Diff of 3:", high)
print("Product is: ", (low * high))
            
        
