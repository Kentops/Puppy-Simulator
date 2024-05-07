import puppy

'''
Puppy simulator by Kieran Whitney and Priscilla Romero
5/8/2024 - A simulation about playing with a puppy!
Implements the State design pattern
'''

def main():
  '''The main class'''
  cocoa = puppy.Puppy() #my dog's name
  print("Congratulations on your new puppy!")
  user_input = ""
  while user_input != "3":
    print("What would you like to do?")
    print("1. Feed the puppy\n2. Play with the puppy\n3. Quit for now")
    user_input = input("> ")
    print()
    #Check input
    if user_input == "1":
      print(cocoa.give_food())
    elif user_input == "2":
      print(cocoa.throw_ball())
    #code will stop if 3 is inputted, other will repeat

  #Loop is over
  print("You and your puppy decide to rest.")

main()