def nine_lines():   #prints 9 dots in a row on the screen
    def three_lines():  #inner-function to print 3 dots in a row on the screen
        def new_line(): #inner-function to print a dot on the screen
            print('.')
        new_line()
        new_line()
        new_line()
    three_lines()
    three_lines()
    three_lines()  
    
def clear_screen():     #prints 25 dots in a row on the screen
    nine_lines()
    nine_lines()
    def three_lines():  #inner-function to print 3 dots in a row on the screen
        def new_line(): #inner-function to print a dot on the screen
            print('.')
        new_line()
        new_line()
        new_line()
    three_lines()
    three_lines()
    def new_line(): ##inner-function to print a dot on the screen
        print('.')
    new_line()
    
print("Printing nine_lines")
nine_lines()
print("Printing clear_screen")
clear_screen()

