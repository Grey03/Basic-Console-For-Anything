import math
global quitconsole
quitconsole = False

#                         ***COMMANDSSS***
#These are your commands just put the name of it here then look below for other info
global commandlist
commandlist = ["help","quit","clear"]

#                         ***Interpretor***
#Take your command and searches through command list for it
def commandinterp(a):
  commandfound = False
  commandrun = -1
  global commandlist
  global quitconsole

  for i in range(len(commandlist)):
    if commandfound == False and a.startswith(commandlist[i] + " "):
      commandfound = True

      if i == 0:
        print (commandlist)
      if i == 1:
        quitconsole = True
      if i == 2:
        for l in range(0,200):
          print ("")



  if commandfound == False:
    print ("\" " + str(a) + "\" is an Invalid Command\n")
  


while (quitconsole != True):
  comipt = ((input("Enter your command > ")).lower() + " ")
  commandinterp(comipt)