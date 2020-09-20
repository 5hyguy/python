import os
import sys
fruits = ["Apple", " Mango", "Grape", "Orange"]
vegetables = ["Carrot", "Spinach", "Lettuce", "Muchroom"]


while True:
  pick_veg_or_fruits = input ("please what kind of product do you want: fruits or vegetables? : ")
  if pick_veg_or_fruits == "fruits":
      print(" we have: Mango or Orange")
      while True:
        pick_veg_or_fruits = input ("please select one of the fruits (Mango or Orange) or type (cancel) to go back :")
        if pick_veg_or_fruits == "Mango":
          print("Here is information on what to prepare with Mango""\n")
          while True:
            pick_veg_or_fruits = input ("What kind of information do you want: Cooking methods, Storage methods, fruits recipe and ingredients or ways to eat it? : ")
            if pick_veg_or_fruits == "fruits recipe and ingredients":
              print()
              print("INGREDIENTS""\n")
              print()
              print("Mango\nIce cubes\nGinger\nAlmond milk\n")
              print()
              print("RECIPE")

              print("How to make Mango smoothie  \n")
            
              print()
              print("Wash the Mango and peel off the skin. Cut into pieces and pour inside a blender.\nPour in some ice cubes and blend together. Continue blending until it forms fine smoothie.\nThen pour into a glass and serve cold.\nYou can garnish it with a slice of strawberry or cucumber")
            while True:
               pick_veg_or_fruits = input ("Do you want to chose another fruit (yes/no)? :")
               if pick_veg_or_fruits =="yes":
                while True:
                   pick_veg_or_fruits = input ("Select the next fruit : orange? : ")
                   if pick_veg_or_fruits == "orange":
                    print("Here is information on what to prepare with Orange""\n")  
                    while True:
                       pick_veg_or_fruits = input ("What kind of information do you want: Cooking methods, Storage methods, fruits recipe and ingredients or ways to eat it? : ")
                       if pick_veg_or_fruits == "Ways to eat it":
                        print()
                        print("Wash the oranges and peel off the skin. Slice into pieces and eat.\n2. Wash the oranges and put into a juicer to extract the juice.\nServe in a glass.\n3. Wash the orange, peel off the outer and white inner skins. Turn on your oven to about 250 degree for preheating.\nWhile the oven is heating cut into slices of round rings. Spread the ring out on a baking tray. Sprinkle with granulated sugar and put inside the oven. Bake for about 10 minutes.\n Allow to cool. Serve with Yoghurt Ice cream and enjoy the delicacies for a general wellbeing")
                        print()
                        while True:
                           more_choice = input ("In other to maintain a healthy lifestyle we recommend eating other fruits like apples \nWould you like to know more about apples:")
                           if more_choice =="no":
                            print("Goodbye, Thank you")
                            print()
                            os.execl(sys.executable, sys.executable, *sys.argv)

  elif pick_veg_or_fruits == "vegetable":
        while True:
           pick_veg_or_fruits = input ("select one of the available vegetable (Carrot or Mushroom) or type (cancel) to go back to choose correct option :")
           if pick_veg_or_fruits == "Carrot": 
            print("Here is information on what to prepare with Carrot""\n")
            while True:
               pick_veg_or_fruits = input ("What kind of information do you want: Ingredients and Cooking methods/Storage methods/fruits recipe and ingredients/Ways to eat it? : ")
               if pick_veg_or_fruits == "Ingredients and Cooking methods":
                print()
                print("Ingredients""\n")
                print("Carrot\nBrown sugar\nButter\nParsley ")
                print()
                print("Cooking methods")
                print("The first step is to peel and cut your carrots into slices in chunks.\nPour into a cooking pot and fill with water at average level.\nPut on the cooker and simmer the carrots until tender.\nThen pour out in a seive to drain the water.\nInside a heated frying pan put butter, brown suagr and salt. Then pour in the simmered carrots and mix very well.\nSprinkle parley on on top for colour(optional).\nPour in a bowl  plate and serve to enjoy the tasty cooking") 
                while True:
                   more_choice = input("Do you want to continue (yes/no :")
                   if more_choice =="no":
                    print("Thank you, Good bye")
                    os.execl(sys.executable, sys.executable, *sys.argv)
                    
              