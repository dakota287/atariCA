#I wake up
#if I a hungry
  #  I eat breakfast

#I leave my house
#if its cloudy
 #   I bring an umbrella
#otherwise
 #   I bring sunglasses

#Im at a restaurant
#if I want meat
  #  I order a steak
#otherwise if I want pasta
  #  I order spaghetti & meatballs
#otherwise
#    I order a salad. 


is_female = True
is_tall = False

if is_female and is_tall: 
    print("You are a female or tall or both!")
else if is_female and not(is_tall):
    print("You are a short female")
else if not(is_female) and is_tall:
    print(" You are a tall male1")
else:
    print("You are neither a female nor tall!")