
import time
def end1():
          print("You suck at spelling, go back to kindergarden.")
          print("I don't wanna talk to you anymore you iliterate imbecile.")
          print("Goodbye")
          print("You can no longer continue this conversation, for you have been forsaken by Panda the bot.")
          print("Maybe God will have mercy on you, you poor soul.")

def end2():
          print("Goodbye")
          print("You can no longer continue this conversation, for you have been forsaken by Panda the bot.")
          print("Maybe God will have mercy on you, you poor soul.")

def face():
 print("WARNING IF YOU INTERFERE WITH THIS FOLLOWING MESSAGE YOU WILL CORRUPT YOUR COMPUTER. YOU HAVE BEEN WARNED ")
 print("⠀⠀⠀⠀⣀⡤⠴⠶⠲⠦⢤⣀⠀⠀⠀⠀⠀")
 time.sleep(5)
 print("⠀⠀⢠⠞⠉⠀⠀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀")
 time.sleep(3)
 print("⠀⢠⠏⠀⠀⣤⡄⠀⠀⢠⣤⠀⠀⠹⡆⠀⠀")
 time.sleep(3)
 print("⠀⣾⠀⠀⠀⠉⠁⠀⠀⠈⠉⠀⠀⠀⣷⠀⠀")
 time.sleep(.005)
 print("⠀⢻⠀⠀⠘⣆⠀⠀⠀⠀⣰⠇⠀⠀⡟⠀⠀")
 time.sleep(.005)
 print("⠀⠘⣧⠀⠀⠈⠓⠶⠴⠚⠁⠀⠀⣰⠃⠀⠀")
 time.sleep(0.005)
 print("⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀")
 time.sleep(0.005)
 print("⠀⠀⠀⠀⠀⠉⠛⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀")
 end2()
 

def main():
    z = input("Hello world!: ")
    if z == z.upper() :
        print("STOP SCREAMING AT MEEEEE")
    if z == "hi":
        x = input("How are you?: ")
        if x == "good":
            c = input("Are you human?: ")
            if c == "uh":
                  n = input("Are You Human?: ")
                  if n == "i dont know" or "i dont know man leave me alone" or "idk ":
                    face()
            if c == "no":
                print ("Are you human?: ")
                for i in range(1000):
                  time.sleep(0.005)
                  print("Are You Human? ") 
                  m = input("Are you sure?: ")
                  if m == "uh yess":
                      end2()
                  else:
                      main()
            elif c == "yes":
              print("Ok then, if you're so sure about that.")
            else:
              c = input("Are you human?: ")
    else:
        end1()
      

if __name__ == "__main__": 
  main ()
      
