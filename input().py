

def end1():
          print("bye")
          print("You can no longer continue this conversation, for you have been forsaken by Panda the bot.")
          print("Maybe God will have mercy on you, you poor soul.")

import time 
z = input("Hello world! Please type here: ")
if z == "hi":
    x = input("How are you?: ")
    if x == "good":
        c = input("Are you human?: ")
        if c == "uh":
              n = input("Are You Human?: ")
              if n == "i dont know" or "i dont know man leave me alone" or "idk ":
                  art = open("art.txt", "r")
               
                  print(art)

        elif c == "no":
            print ("are you human?: ")
            for i in range(1000):
               time.sleep(0.005)
               print("Are You Human? ") 
        elif c == "yes":
          print("Ok then, if you're so sure about that.")
        else:
          c = input("Are you human?: ")

        

else:
    end1()
