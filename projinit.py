import os,shutil
# Makefile
makefile=input("Would you like to create a makefile? (Y/n) ")
makefile=makefile.capitalize()
mf=makefile
del makefile
if mf=="Y" or mf=="Yes":
    open("Makefile","w")
    print("Made file")
# Git initialization
git=input("Would you like to initialize a git repo? (Y/n) ").capitalize()
if git=="Y" or git=="Yes":
    stream=os.popen("git init")
    print(stream.read())
# Bat script
bat=input("Create a bat file? (Y/n) ").capitalize()
if bat=="Y" or git=="Yes":
    filename=input("Filename: ")
    command=input("Command (if blank, uses make): ")
    if command=="":
        command="make"
    args=[]
    print("Arguements (for -output_dir ./blah_blah type -output_dir and then blah_blah")
    while True:
        arg=input("Arg: ")
        if arg=="":
            break
        args.append(arg+" ")
    fullcommand=command+" "+" ".join(args)
    with open(filename+".bat", "w") as f:
        f.write(fullcommand+"\n")
    print("Wrote")

input("Press any key to continue...")
