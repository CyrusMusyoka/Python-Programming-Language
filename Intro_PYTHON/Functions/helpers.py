def getNames():
    names = ['alice', 'cyrus', 'evans']
    newNames = input('Enter last guest :')
    names.append(newNames)
    return names

def printNames(names):
    for name in names:
        print(name)
    return