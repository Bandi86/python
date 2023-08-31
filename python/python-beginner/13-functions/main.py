date = 2023
user1 = "Virág"
user2 = "Emese"
user1_age = 18
user2_age = 20

#print(f"Üdv {user1}, {user2}")

def birth(nev,kor):
    return (f"{nev}, {date - kor}-ban/ben született")
szoveg = birth("Péter", 42)
print(szoveg) #Péter 1981-ben született


def wellcome(nev):
    print(f"Üdv {nev}")

wellcome(user1)  #Üdv Virág

print(birth(user1,user1_age)) #Virág 2005-ben született
print(birth(user2, user2_age)) #Emee 2003-ban született
 