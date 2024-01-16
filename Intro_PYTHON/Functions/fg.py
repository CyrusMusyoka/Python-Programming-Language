def main():
    names = ['cyrus','alice','evans','mutua']
    newName = input("Enter new guest: ")
    names.append(newName)

    printNames(names)
    return

def printNames(list):
    for name in list:
        print(name)
    return
