from datetime import datetime
import time

class Plant:    #start with class for our Plant, add vitals

    def __init__(self,name):
        self.name = name
        self.birthdate = datetime(2024, 5, 6) # find age in days
    # initial vitals(0 =healthy. 10 = unhealthy)

        self.water = 3
        self.sunlight = 6
        self.nutrients = 5
        self.wilt = 1

        self.asleep = False # sleeps at night
        self.dead = False     # not dead at start, will die due to negligence

    
    def vitals(self): #Check and display plant's levels
        if self.dead:
            print("\033[1m Your plant has died, they no longer have vitals.\033[0m")
            return
        
        print(f"{self.name}'s Current Vitals:")
        print(f"Water Level:{self.water}/10")
        print(f"Sunlight Exposure:{self.sunlight}/10")
        print(f"Soil Nutrients:{self.nutrients}/10")
        print(f"Wilting Level:{self.wilt}/10")
        if self.asleep:
            print('Status: Sleeping')
        else:
            print('Status: Awake')   #will let user know if it's asleep or awake

    def time(self):     #changes to vitals over time 
        if not self.dead:
            if not self.asleep:    #if plant is awake
                self.water+=0.3
                self.nutrients+=0.2
                self.wilt+= 0.2
            else:
                self.sunlight -= 0.3   #if plant is asleep as sunlight decreses at night    


            # vitals cannot exceed 10
            self.water = max(0, min(self.water, 10))
            self.sunlight = max(0,min(self.sunlight, 10))
            self.nutrients = max(0, min(self.nutrients, 10))
            self.wilt = max(0, min(self.wilt, 10))
            
            self.health() #death if vitals hit 10
            
        time.sleep(2)   #changes every 2 seconds

    
    def health(self): #Check plants health and handle death conditions
        if self.water==10:
            print('\033[1mYour plant drowned from overwatering.\033[0m")')
        if self.sunlight ==10 :
            print("\033[1mYour plant has withered away from too much sunlight.\033[0m")
        if self.wilt == 10 :
            print("\033[1mYour plant has wilted away due to neglect.\033[0m")
        if self.nutrients == 10:
            print("\033[1mYour plant has died from lack of nutrients.\033[0m")
            
        if self.water ==10 or self.sunlight==10 or self.wilt==10 or self.nutrients==10:
            self.dead = True
            print("\033[1mI am too weak and tired... I have passed away. Please let me rest in peace.\033[0m")
            return True

        return False

    
    def water_plant(self):    #function to water plant and to decrease water level
        if self.dead:  
            print("\033[1mYour plant can't be watered, they are dead.\033[0m")
            return
        else:
            self.water -= 1
            if self.water < 0:
                self.water = 0
            print(f"\033[1mThank you for watering me! My water level is now {self.water}.\033[0m")
        self.health()

    def give_sunlight(self):      #function to give Zau water and to reduce sunlight
        if self.dead:
            print("\033[1mYour plannt is dead, they can't use sunlight.\033[0m")
            return
    
        if self.asleep:
            print("\033[1mI am asleep, I can't use sunlight right now.\033[0m")
            return
        
        self.sunlight -= 1
        if self.sunlight <0:
            self.sunlight = 0
            
        print(f"\033[1mThank you for putting me in the sun! My sunlight level is now {self.sunlight}. I am photosynthesising!\033[0m")
        self.health()

    def fertilse_soil(self):      #function to put Zau to sleep and to reduce wilt
        if self.dead:
            print("\033[1mFertiliser cannot revive a dead plant..\033[0m")
            return
        
        self.nutrients -= 1
        if self.nutrients < 0:
            self.nutrients = 0
        print(f"\033[1mThank you for fertilising me! My nutrient level is now {self.nutrients}.\033[0m")
        self.health()
    
    def nightime(self):        #function to put plant to 'sleep' at night
        if self.dead:
            print("\033[1mDead plant don't sleep!\033[0m")
        if self.asleep:
            self.asleep = False
            print("\033[1mIt is nighttime, plant is resting!\033[0m")
        else:
            self.asleep = True
            print("\033[1mThe sun has set. Plant is resting.\033[0m")
            
    def daytime(self):        #function to wake plant up during the day
        if self.dead:
            print("\033[1mDead plant don't wake up!\033[0m")
        if not self.asleep:
            self.asleep = True
            print("\033[1mIt is daytime, plant is awake!\033[0m")
        else:
            self.asleep = False
            print("\033[1mThe sun is up. Plant is awake.\033[0m")
        
            
        
    def age(self):     #function to get Zau's age in days, ages normally
        today = datetime.today()
        birthdate = datetime(2023, 5, 6) 
        age_in_days = (today - self.birthdate).days
        print(f"\033[1mI am {age_in_days} days old.\033[0m")
        


def main():      #main function to interact with Zau
    
    print("Hi, what is your name ?!")   #user input for name
    name = input()
    print( f"Hi {name}! Welcome to your virtual plant, GROUT.  Nice to meet you.")
    
    plant_name = "GROUT"  #default name for plant
    plant = Plant(plant_name)  #creates instance for class Plant


    while True:
        if plant.dead:
            print("Grout is dead. You can no longer interact with it.")
            break   #exit loop when grout dies

        plant.time()   #vitals update


        #options for user
        print("What do you want to do? Input number 1-8")
        print("1. Water Grout")
        print("2. Give Grout Sunlight.")
        print("3. Add nutrients!")
        print("4. Check Grout's age!!")
        print("5. Show vitals.")
        print("6. Set Daytime/Afternoon.")
        print("7. Set Nighttime/Evening.")
        print("8. Exit")
        step = input() 
        if step == '1':
            plant.water_plant()
        elif step == '2':
            plant.give_sunlight()
        elif step == '3':
            plant.fertilse_soil()
        elif step == '4':
            plant.age()
        elif step == '5':
            plant.vitals()
        elif step == '6':
            plant.daytime()
        elif step == '7':
            plant.nightime()
        elif step == '8':
            print('Goodbye')
            break
        else:
            print("Invalid choice, please try again")

          #calls main function
if __name__ == "__main__":
    main()