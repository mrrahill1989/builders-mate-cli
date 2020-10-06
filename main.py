print("*************************************************")
print("**                                             **")
print("**                BUILDER'S MATE               **")
print("** The only tool you'll need to keep building. **")
print("**                                             **")
print("*************************************************")
print(" ")
print(" ")
print("What would you like to do?")
print(" ")
print("1. Conversions")

def mainmenuselection():
    mainmenu = input("Enter selection: ")
    while (mainmenu != "1"):
        mainmenu = input("Input wrong, please select from one of the options.")
    
    if mainmenu == "1":
        print("this is conversions.")
        
mainmenuselection()