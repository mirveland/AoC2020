# Fields in passport
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# Field validation rules
# cid (Country ID) - ignored, missing or not.

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def evaluateYear(fieldkey, year):
    ret = bool(True);
    
    if (fieldkey == "byr"):
        ret = True if (year >= 1920 and year <= 2002) else False;
    elif (fieldkey == "iyr"):
        ret = True if (year >= 2010 and year <= 2020) else False;
    elif (fieldkey == "eyr"):
        ret = True if (year >= 2020 and year <= 2030) else False;
        
    if (ret == False):
        print("Fel årtal i ", fieldkey, " - ", year);
    return ret
    
# hgt (Height) - a number followed by either cm or in:
#    If cm, the number must be at least 150 and at most 193.
#    If in, the number must be at least 59 and at most 76.
def evaluateHeight(value):
    ret = bool(True);
    system = value[-2:];
    heightstr = value[:-2];
    height = int(heightstr);
    
    if (system == "cm"):
        ret = True if (height >= 150 and height <= 193) else False;
    elif (system == "in"):
        ret = True if (height >= 59 and height <= 76) else False;
    else: ret = False;
    
    if (ret == False):
        print("Fel längd: ", value);

    return ret

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def evaluateHairColor(value):
    ret = bool(True);
    ret = ret and value[0] == "#";
    ret = ret and len(value[1:]) == 6;
    ret = ret and value[1:].isalnum();
    
    if (ret == False):
        print("Fel hårfärg: ", value);

    return ret;
    
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def evaluateEyeColor(value):
    ret = bool(True);
    ret = ret and value in("amb", "blu", "brn", "gry", "grn", "hzl", "oth");
    
    if (ret == False):
        print("Fel ögonfärg: ", value);
    
    return ret;
    
# pid (Passport ID) - a nine-digit number, including leading zeroes.
def evaluatePassportId(value):
    ret = bool(True);
    ret = ret and value.isnumeric();
    ret = ret and len(value) == 9;
    
    if (ret == False):
        print("Fel passid: ", value);
        
    return ret;
    

def validateFormat(mandatoryfieldkey, value):
    ret = bool(True);
    
    if (mandatoryfieldkey == "hgt"):
        ret = ret and evaluateHeight(value);
    elif (mandatoryfieldkey in("byr", "iyr", "eyr")):
        ret = ret and evaluateYear(mandatoryfieldkey, int(value));
    elif (mandatoryfieldkey == "hcl"):
        ret = ret and evaluateHairColor(value);
    elif (mandatoryfieldkey == "ecl"):
        ret = ret and evaluateEyeColor(value);
    elif (mandatoryfieldkey == "pid"):
        ret = ret and evaluatePassportId(value);
    
    return ret;
    
mandatoryfields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"];
ok = bool(True);
okpassports = 0;
passportdict = {};
passportfields = [];

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\passports.txt") as passportfile:
    for passportline in passportfile: #Go one step down
        passportline = passportline.strip(); #preprocess line
        
        if (okpassports >= 156):
            print(passportdict);
            
        if (not passportline):
            #evaluate previous passport
            #print(passportdict);
            
            for mandatoryfield in mandatoryfields:
                if (not mandatoryfield in passportdict
                    or not passportdict[mandatoryfield]):
                    ok = False;
                    print("NOT OK - missing field: ",mandatoryfield);
                    break;
                elif (not validateFormat(mandatoryfield, passportdict[mandatoryfield])):
                    ok = False;
                    #print("NOT OK - bad format");
                    break;

            if (okpassports >= 156):
                print(okpassports);
                    
            if (ok): okpassports += 1;
            
            #reset passport data
            ok = True;
            passportdict = {};
        else:
            passportfields = passportline.split();
            if (okpassports >= 156):
                print(passportfields);
                                    
            for field in passportfields:
                [key,value] = field.split(':');
                passportdict[key] = value;
                
if (okpassports >= 156):
    print(okpassports);
    print(passportdict);

#evaluate previous passport
for mandatoryfield in mandatoryfields:
    if (not mandatoryfield in passportdict
        or not passportdict[mandatoryfield]):
        ok = False;
        print("NOT OK - missing field: ",mandatoryfield);
        break;
    elif (not validateFormat(mandatoryfield, passportdict[mandatoryfield])):
        ok = False;
        print("NOT OK - bad format");
        break;        

if (ok): okpassports += 1;
                

print("Antal pass som är ok: ", okpassports," - det du!")
