def calcRow(bpass):
    lowest = 0;
    highest = 127;
    i = 0;
    #bpass = bpass.split();
    
    for part in bpass:
        if (i > 6):
            break;
            
        #print("row part: ", part);
        
        if (part == "F"):
            highest = highest - ((divmod(highest - lowest, 2)[0]) +1);
            #print("lowest: ", lowest);
            #print("highest: ", highest);
        elif (part == "B"):
            lowest = lowest + ((divmod(highest - lowest, 2)[0]) + 1);
            #print("lowest: ", lowest);
            #print("highest: ", highest);

        else:
            print("FEL kod: ", part);
            break;
        
        i += 1;
        
    #print("lowest: ", lowest);
    #print("highest: ", highest);
    
    return lowest
  
def calcSeat(bpass):
    lowest = 0;
    highest = 7;
    i = 0;

    
    for part in bpass[7:]:
        if (i > 2):
            break;
              
        #print("seat part: ", part);
        
        if (part == "L"):
            highest = highest - ((divmod(highest - lowest, 2)[0]) +1);
            #print("lowest: ", lowest);
            #print("highest: ", highest);

        elif (part == "R"):
            lowest = lowest + ((divmod(highest - lowest, 2)[0]) +1);
            #print("lowest: ", lowest);
            #print("highest: ", highest);

        else:
            print("FEL kod: ", part);
            break;
        
        i += 1;
        
    #print("lowest: ", lowest);
    #print("highest: ", highest);
    
    return lowest
    
highestSeatId = 0;
occupiedSeatsList = [];

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\boardingpasses.txt") as boardingfile:
    for line in boardingfile: #Go one step down
        line = line.strip().split(); #preprocess line
        boardingpass = line[0];
        
        #print("boardingpass: ", boardingpass);
        row = 0;
        seat = 0;

        row = calcRow(boardingpass);
        seat = calcSeat(boardingpass);
        
        seatId = (row * 8) + seat;
        
        occupiedSeatsList.append(seatId);
        
        highestSeatId = seatId if seatId > highestSeatId else highestSeatId;
        
print("Highest seat id: ", highestSeatId," - det du!")

i = 8;
j = min(highestSeatId, (127*8)-1);
lowerNeighbour = 0;

while i <= j:
    if i in occupiedSeatsList:
        lowerNeighbour = i;
    elif ((i not in occupiedSeatsList) and (i == lowerNeighbour+1)):
        print("free seat: ", i);
        
    i += 1;