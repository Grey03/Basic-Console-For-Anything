import math
global quitconsole
quitconsole = False


global functions():
functions = []

def addfunction(a):
  functions.append(a)

#                         ***COMMANDSSS***
#These are your commands just put the name of it here then look below for other info
global basiccommands
basiccommands = ["help","quit","clear"]

#                         ***Interpretor***
#Take your command and searches through command list for it
def commandinterp(a):
  commandfound = False
  global basiccommands
  for i in range(len(basiccommands)):
    if commandfound == False and a.startswith(basiccommands[i] + " "):
        commandfound = True
        return i
  if commandfound == False:
    print ("\" " + str(a) + "\" is an Invalid Command\n")

while (quitconsole != True):
  comipt = ((input("Enter your command > ")).lower() + " ")

  #                    ***COMMAND SECTION***
  #simply make an if for  your command that leads to what you want 
  def commandrun(command):
    if command == 0:
      print (basiccommands)
    if command == 1:
      quitconsole = True
    if command == 2:
      for l in range(0,200):
        print ("")

  commandrun(commandinterp(comipt))