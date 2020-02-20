import os
def error(e):
    print("ERROR:" + str(e))
def help():
    print("1) cd path - walk to directory")
    print("2) ls - show list of files and directories")
    print("3) ls -f - list of files")
    print("4) ls -d - list of directories")
    print("5) mkdir - create a directory")
    print("6) rm -d - remove a directory")
    print("7) rm -f - remove a file")
    print("8) rename - rename file or directory")
    print("9) open - opne file or directory")
os.chdir('.')
#help()
while True:
    cmd = input(os.path.abspath('.') + ": ").split()
    if cmd[0] == 'cd':   
        try:
            os.chdir("./" + cmd[1])
        except Exception as e:
            error(e)

    elif cmd[0] == 'ls':  
        try:
            if cmd[1] == '-f':  # list of files
                for root, dirs, files in os.walk("."):
                    print(len(files))
                    break
            elif cmd[1] == '-d': # list of directories
                for root, dirs, files in os.walk("."):
                    print(len(dirs))
                    break
            else:
                print(os.listdir()) # list of all
        except:
            print(os.listdir()) # list of all
        

    elif cmd[0] == 'mkdir':  # create a directory
        os.mkdir('./' + cmd[1])

    elif cmd[0] == 'rm':    

        if cmd[1] == '-d':   # remove directory
            try:
                os.rmdir("./" + cmd[2])   
            except Exception as e:
                error(e)
        elif cmd[1] == '-f':  # remove file
            try:
                os.remove("./" + cmd[2])
            except Exception as e:
                error(e)
        else:
            print("command not found")
    
    elif cmd[0] == 'rename': # rename file or directory
        try:
            os.rename(cmd[1], cmd[2])
        except Exception as e:
            error(e)
        
    elif cmd[0] == 'open':
        try:
            f = open(cmd[1], cmd[2])
            if cmd[2] == 'r': # read a file
                print(f.read())  
            else:             # write to file
                text = input("Enter text to write:")
                f.write(text + '\n')
            f.close()
        except Exception as e:
            error(e)
    elif cmd[0] == 'help':
        help()