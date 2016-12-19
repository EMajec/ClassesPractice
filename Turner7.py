# Ethan Turner
# 11/15/16
# CS 065
# This is a project that shows how inheritence works between two different classes
# Proposed Points - 15/15 because I was able to create the classes both sub and super, create instances, add attributes,
# and write both accessor and mutator methods, also I called all of the methods at some point in my code.



class Mythical_Beasts: #creates the superclass of Mythical Beasts
    def __init__(self,abilities,texture,age,type): #initializes the Mythical Beasts Class
        self.__abilities = abilities #creates the attribute for abilities
        self.__texture = texture #creates the attribute for texture
        self.__age = age #creates the attribute for age
        self.__type = type #creates the attribute for type
    def set_abilities(self, abilities): #mutator method for abilities
        self.__abilities = abilities
    def set_texture(self,texture): #mutator method for texture
        self.__texture = texture
    def set_age(self, age): #mutator method for age
        self.__age = age
    def set_type(self,type): #mutator method for type
        self.__type = type
    def get_abilities(self): #accessor method for abilities
        return self.__abilities
    def get_texture(self): #accessor method for texture
        return self.__texture
    def get_age(self): #accessor method for age
        return self.__age
    def get_type(self): #accessor method for type
        return self.__type

class Dragons(Mythical_Beasts): #makes Dragons a subclass to Mythical Beasts Class
    def __init__(self,name, abilities,texture,age,type,treasure, XP, HP,): #sets the dragon class
        Mythical_Beasts.__init__(self,abilities,texture,age,type) #passes attributes into Dragon class from Mythical Beasts
        self.__name = name #sets name of the Dragon
        self.__treasure = treasure #sets if the dragon has treasure
        self.__XP = XP #sets the dragons experience points
        self.__HP = HP #sets the dragons health points
    def set_name(self, name): #mutator method for name
        self.__name = name
    def set_treasure(self, treasure): #mutator method for treasure
        self.__treasure = treasure
    def set_XP(self, XP): #mutator method for XP
        self.__XP = XP
    def set_HP(self, HP): #mutator method for HP
        self.__HP = HP
    def get_name(self): #accessor method to name
        return self.__name
    def get_treasure(self): #accessor method to treasure, determines of the dragon has treasure or not
        if self.__treasure == True:
            print("Your dragon has treasure")
        elif self.__treasure == False:
            print("Your dragon does not have treasure")
    def get_HP(self): #accessor method for HP
        return self.__HP
    def get_XP(self): #accessor method for XP
        return self.__XP


def main(): #runs the function that creates instances of each class
    LusterDragon = Dragons("Luster Dragon",'Fly and Breath Dark Souls', 'Scaled',19900, "Flying", True, 3862, 200 ) # Creates an instance of Dragons
    CelestialDragon = Dragons("Celestial", 'Fly and Rain Stars Down', 'Stardust', "unknown", "Flying and Celestial", False, 8052, 3000) #Creates a second instance of Dragons
    print('Your', LusterDragon.get_name(), 'has the ability to', LusterDragon.get_abilities()) #prints the name and ability of the Luster Dragon
    print('The texture of your', LusterDragon.get_name(),' is', LusterDragon.get_texture()) #prints the name and texture of the Luster Dragon
    print('Your', LusterDragon.get_name(), 'is',LusterDragon.get_age(),"years old" ) #prints the name and age of the Luster Dragon
    print("Your", LusterDragon.get_name(), 'is a', LusterDragon.get_type(), "type") #prints the name and type of the Luster Dragon
    print("Your,", LusterDragon.get_name(),"has", LusterDragon.get_XP(),"XP out of 4000") #prints the name and XP of the Luster Dragon
    print("Your,", LusterDragon.get_name(),"has", LusterDragon.get_HP(),"HP") #prints the name and HP of the Luster Dragon
    print(LusterDragon.get_treasure()) #determines if the dragon has treasure or not
    print("")
    print('Your', CelestialDragon.get_name(), 'has the ability to', CelestialDragon.get_abilities()) #prints the name and ability of the Celestial Dragon
    print('The texture of your', CelestialDragon.get_name(), ' is', CelestialDragon.get_texture()) #prints the name and texture of the Celestial Dragon
    print('Your', CelestialDragon.get_name(), 'is', CelestialDragon.get_age(), "years old")  #prints the name and age of the Celestial Dragon
    print("Your", CelestialDragon.get_name(), 'is a', CelestialDragon.get_type(), "type") #prints the name and Type of the Celestial Dragon
    print("Your,", CelestialDragon.get_name(), "has", CelestialDragon.get_XP(), "XP out of 10,000")#prints the name and XP of the Celestial Dragon
    print("Your,", CelestialDragon.get_name(), "has", CelestialDragon.get_HP(), "HP") #prints the name and HP of the Celestial Dragon
    print(CelestialDragon.get_treasure()) #determines if the dragon has treasure or not

main()