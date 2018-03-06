# dirictory_guide Program
import os
import os.path

# Put the searching directory part in this function
def search():
    print "\n"


def main():
    
    # Initialized Variables 
    cwd = os.getcwd()
    con_program = ""    
    
    d_input = raw_input("\nEnter what directory you wish to be put in or Enter d for default: ")
    
    # This loop allows the user to select the directory they want by checking if their input is exsistant in a loop and allowing for a switch if needed
    while True:
        if d_input == "d": # 'd' when looped does not run program after while loop /BUG!!!/ If user accidently puts d program breaks
            break    
        
        try: 
            os.chdir(d_input)
            cwd = os.getcwd() # gets the current directory/ print cwd to show user which directory they are in
            print d_input, "is a directory"
            
        except:
            print "\nError!:", d_input, "is not a directory"
            print cwd, "is your current directory"
            
            
        con_program = raw_input("\nHit Enter to continue or type s to switch directory: ") 
        if not con_program == 's':
            break
        
        elif con_program == "s":
            cwd = os.getcwd()
            d_input = raw_input("\nEnter what directory you wish to be put in: ")
        
    if not con_program == "s":
    
        # Prints out all files in current directory
        print "\nHere are the current files in", cwd
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print f
        
        
        Userinput = raw_input("\nPlease Enter a File name: ")
        file = Userinput.strip() # Strip function gets ride of all whitespace around what the user inputed
        
        # Checks if the file is exsistant
        from pathlib import Path
        my_file = Path(file)
        if my_file.is_file():
            print "File exists!\n"
            
            # Chooses if the user wants to edit file
            write = raw_input("Hit Enter to continue or type q to quit: ")
            if not write == 'q': # If anything other then q is entered it is continued
                
                print "\nThis is currently in your file"
                file_write = open(file, "a+")
                file_write.seek(0) # Fixes bug where file was being read from the end
                print file_write.read(), "\n"
                
                w = raw_input("Type what you want appended into the file: ")  # Allows user to write to file
                file_write.write("\n")
                file_write.write(w)
                
                print "You just wrote", '"' , w, '"' , "to", file
                file_write.close()
                print file_write
            
        else:
            print "File not there!"
            
            write = raw_input("\nHit enter to create a file or type q to quit: ")
            if not write == 'q':
                
                file_new = open(file, "w+")
                w = raw_input("Type what you want writen into the file: ")
                file_new.write(w)
                
                print "You just created", file, "and wrote", '"' , w, '"', "to it"
                file_new.close()
                print file_new  # To check if the file is closed after runing program
                
                # Add a way to catch all user input into another file - Timestap as well
                # Add a way to have a choice between reading, overwriting, or appending to a file
                # Add a way to list all current directorys avaliable
                # Add a way to view directorys once a path is choosen past the while loop
                # Add a way to loop entire program to allow user to either change directory again /or create another file
                # Maybe add a way to delete files as well
                # Whenever q is typed anywhere quit the whole program

main()