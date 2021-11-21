import math

global quitconsole
quitconsole = False
global commands
commands = ["help","quitconsole","clearconsole","varexample"]
global inpt
inpt = ""

def consolestart():
  global quitconsole
  global commands

  while quitconsole == False:
    getcommand()
    commandvalid = False

    for i in range(len(commands)):
      if inpt.startswith(commands[i]) and commandvalid == False:
        commandnum = i
        commandvalid = True
        
    if commandvalid == False:
      print ("Invalid Command")
    else:
      runcommand(commandnum)

def getcommand():
  global inpt
  inpt = input("> ")

def quit():
  global quitconsole
  quitconsole = True


def runcommand(commandnum):
  global commands
  global quitconsole

  if commandnum == 0:
    print ("----------")
    print ("|Commands |")
    print ("----------")
    for i in range(len(commands)):
      print (commands[i])
  elif commandnum == 1:
    quit()
  elif commandnum == 2:
    for i in range(200):
      print ("\n")
  elif commandnum == 3:
    #THIS IS A VAR EXAMPLE FOR COMMANDS THAT NEED EXTRA JUNK
    #Just add ur inputs with the command
    print ("Enter First Num")
    x = int(input("> "))
    print ("Enter Second Num")
    y = int(input("> "))
    print ("x + y = " + str(x+y))
  else:
    print ("something went wrong here")
  print ("")

consolestart()
