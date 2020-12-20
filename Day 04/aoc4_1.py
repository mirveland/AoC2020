#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

mandatoryfields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"];
ok = bool(True);
okpassports = 0;
passportdict = {};
passportfields = [];

with open("C:\\Users\\MattiasIrveland\\OneDrive\\Source\\Python\\passports.txt") as passportfile:
    for passportline in passportfile: #Go one step down
        passportline = passportline.strip(); #preprocess line
        if (not passportline):
            #evaluate previous passport
            for mandatoryfield in mandatoryfields:
                if (not mandatoryfield in passportdict
                    or not passportdict[mandatoryfield]):
                    ok = False;
                    print("NOT OK");
                    break;
            
            if (ok): okpassports += 1;
            
            #reset passport data
            ok = True;
            passportdict = {};
        else:
            print(passportline);
            passportfields = passportline.split();
            print(passportfields);
                
            for field in passportfields:
                [key,value] = field.split(':');
                passportdict[key] = value;
                print("Field: ", key, "-",value);
                
#evaluate previous passport
for mandatoryfield in mandatoryfields:
    if (not mandatoryfield in passportdict
        or not passportdict[mandatoryfield]):
        ok = False;
        print("NOT OK");
        break;

if (ok): okpassports += 1;
                

print("Antal pass som är ok: ", okpassports," - det du!")
