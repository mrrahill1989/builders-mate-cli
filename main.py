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

def mainmenuselect():
    
    mainmenu = input("Enter selection: ")
    
    while (mainmenu != "1"):
        mainmenu = input("Input wrong, please select from one of the options. ")
        mainmenuselect()
    
    if mainmenu == "1":
        print("Conversions")
        print(" ")
        print(" ")
        print("What trade does your conversions involve?")
        print("1. General")
        
        def converttrades():
            converttradesselect = input("Enter selection: ")
            
            while (converttradesselect != "1"):
                print("Input wrong, please select from one of the options. ")
                converttrades()
                
            if converttradesselect == "1":
                print("The is general conversions.")
        
        converttrades()
        
mainmenuselect()