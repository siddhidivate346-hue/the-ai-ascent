"""try:
    filename = input("enter file name")
    file=open(filename,"r")
    content = file.read()
    print("\n file content:\n",content)
except  FileNotFoundError:
    print("file not found!please check name")
"""

"""try:
    file=open("data.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file not found,creating new file")

    file=open("data.txt","w")
    file.write("new file created")
    file.close()"""


try:
    filename=input("ENTER FILE NAME: ")
    file=open(filename,"r")
    print("\n FILE CONTENT: \n",file.read())
except FileNotFoundError:
    print("FILE NOT FOUND!")

    request=input(f"DO YOU WANT TO CREATE '{filename}'?(yes/no): " )
    if request.lower() == "yes":
        file=open(filename,"w")
        file.write("FILE CREATED AUTOMATICALLY.")
        file.close()
        print("FILE CREATED SUCCESSFULLY!")
    else:
        print("FILE NOT CREATED.")
finally:
    print("PROGRAM ENDED")