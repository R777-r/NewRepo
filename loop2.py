import random

WC=["INDIA","New ZEALAND","ENGLAND","NEPAL","AUSTRALIA","SOUTH AFRICA"]
random.shuffle(WC)
print(WC)
print()
print()
team=random.choice(WC)
for team in WC:
    
    if team == "NEPAL":
        print(f"{team} is not in WC2023")
        print()
        print("**Not Qualified**")
        print("----------")
        print()
        break #continue
    print(f"{team} is in WC2023")
    print()
    print("#ATB#")
    print("-----")