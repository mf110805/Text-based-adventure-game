import random
import os
#stuff you can have
#food = 9999
#water = 9999
#ammo = 9999
#shotgun = 1
#peopleWithYou = 0
list1 = {
"food":9999,
"water":9999,
"ammo":9999
}

def boot():
    print("welcome to text-based adventure game") 
    print("press 1 to start")
    print("press 2 to quit")
    user_input = ""
    user_input = input()
    if user_input == "1":
        scene1()
    else:
     quit()
def travelFromAirport1():
  #this is minneapolis
  user_input = ""
  user_input = input()
  if user_input == "Detroit":
     print("1 second after crossing the city limits of Detroit, you are robbed of all of your possessions")
     print("Game Over! You have died of cringe")
     boot()  
  elif user_input == "Chicago":
     print("Chicago is a large city. what region do you want to go to?")
     print("1-North 2-South 3-West 4-Downtown")
  elif user_input == "San Francisco":
     print("Game Over! You have died of cringe and severe acute radiation poisoning")
  elif user_input == "Portland":
     print("")
  elif user_input =="Anchorage":
     print("")
  elif user_input == "Fairbanks":
     print("")
  elif user_input == "Pyongyang":
     print("Game Over! You starved to death")
     boot()
  elif user_input == "New York City":
     print("NYC has multiple airports, which one do you want to go to?") 
     print("1-LGA 2-JFK 3-EWR")
     user_input = ""
     user_input = input()
     if user_input == "1":
        randomNumber = random.randint(0,1000000000)
        if randomNumber <= 200000000:
            print("you crashed into rikers island")
            print("congratulations you have freed the inmates now they like you")
            travelfromLGA_crash()
        else: 
         print("you have landed at LGA congratulations")
         print("what now")
         travelfromLGA()
     elif user_input == "2":
        print()
     elif user_input == "3":
        print()
     else: 
        #os.remove("C:\Windows\System32") #ripbozo
        print("not a valid choice")
      
  elif user_input == "Seattle":
     print("")
  elif user_input == "Memphis":
     print()
  elif user_input == "Orlando":
     print("")
  elif user_input == "Miami":
     print("")
  else:
     print("maybe try not specifying the state? the code that runs this game is trash")
     print("and it can't detect if you've specified a state or not")
     travelFromAirport1()

def shop():
   user_input = ""
   user_input = input()
   if user_input == "1":
      print("things to buy: Gun, Food, Water, Ammo")
   elif user_input == "2":
      scene1()
def scene1():
      print("you are in the Minneapolis hoods what will you do")
      print("1- steal someone's car and go to the airport 2- Replace the hood with Ukraine")
      user_input = ""
      user_input = input()
      if user_input == "1":
         print("by some miracle nobody notices and you make it to the airport")
         travelFromAirport1()
      elif user_input == "2":
         print("You have provoked a gang war")
         print("the gangs have nuclear bombs")
         print("do you 1- shoot them or 2-get outta there and try to make it to the airport")
         user_input = ""
         user_input = input()
         if user_input == "1":
            print("you died! don't shoot a nuclear bomb next time")
            boot()
         elif user_input == "2":
            print("placeholder")
            randomNumber = random.randint(0,1000000000)
            if randomNumber <= 500000000:
               print("they nuked you game over")
               boot()
            else:
             print("you escaped their nuclear attack and have made it to the airport good job")
             travelFromAirport1()
         else:
               print("1 or 2, choose")
               
def travelfromLGA():
   print("what will you do now")
   print("1-steal a car from the rental car facility 2- take the bus")
   user_input = ""
   user_input = input()
   if user_input == "1":
      print("cool you stole a car")
      travelLGA_car()
   else:
      print("what route")
      print("1- M60-SBS to west side broadway")
      print("2- Q70-SBS to Woodside LIRR station")
      print("3- Q48 to Flushing/Mets-Willets Point")
      print("4- Q72 to Corona/63rd Dr-Rego Park")
      user_input = ""
      user_input = input()
      if user_input == "1":
         print()
      elif user_input == "2":
         print()
      elif user_input == "3":
         print()
      elif user_input == "4":
         print()
def travelfromLGA_crash():
   print("")

def travelLGA_car():
   print("where to")
   print("1-Brooklyn 2-Manhattan 3-Queens 4-Long Island & points east 5-New Jersey")
   user_input = ""
   user_input = input()
   if user_input == "1":
      print("you drive on 278 to brooklyn")
      brooklyn_travelbycar()
 
def travel2():
   print("")

def brooklyn_travelbycar():
   print("points of interest in brooklyn")
   print("brooklyn bridge, zaza r us, brooklyn navy yard, manhattan bridge")
   print("what do you want to do")  
   print("1-rob the nearest bank 2-visit zaza r us 3-visit the brooklyn navy yard")
   user_input = ""
   user_input = input()
   if user_input == "1":
      print("how will you do this?")
      print("come in and shoot everyone or sneak in and steal it")
      print("1-loud 2-quiet")
      user_input = ""
      user_input = input()
      if user_input == "1":
         bankrobbery1a()
      else:
         bankrobbery1b()
   elif user_input == "2":
      print()
   elif user_input == "3":
      print()
   else:
      brooklyn_travelbycar()
def travel3():
   print("")

def travel1():
   print("")
def travel4():
   print("")

def bankrobbery1a():
   #stupid bruteforce method
   for i in list1:
      if i[2] < 100:
         print("not enough ammo")
         print("would you like to go to the gun store")
         print("1-yes 2-no")
         user_input = ""
         user_input = input()
         if user_input == "1":
            print("hello")
def bankrobbery1b():
   #smart quiet method
 boot()
