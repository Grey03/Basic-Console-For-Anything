import math

#VARS SETUP
global quitconsole
quitconsole = False
global inpt
inpt = ""
# --------------STEPS FOR COMMANDSSSS------------
# 1. GO TO note labeled "1." Then just add your command to the end of the list
# 2. GO TO note labeled "2." Then just add a description for your command
# 3. GO TO note labeled "3." Then just add what your command does

global commands
#               1. (Add ur command at the end)
commands = ["commands",
"quitconsole",
"clearconsole",
"help",
"varexample"]


#               2. (Add a brief desc)
global commanddesc
commanddesc = ["Shows list of all commands",
"Quits the console",
"Clears the console",
"Shows descriptions of commands",
"This is just an example but it takes 2 numbers and adds them and shows you the sum"]


def consolestart():
  print ("Basic Console starting up...")
  #starts the console as a def incase u want a button that runs the console
  global quitconsole
  global commands
  print ("Console started!")
  print ("Enter command below. Type \"commands\" for commands.")
  print ("")
  while quitconsole == False:
    getcommand()
    runcommand()
    

def getcommand():
  global inpt
  inpt = input("> ")

def quit():
  global quitconsole
  quitconsole = True


def runcommand():
  global commands
  global commanddesc
  global quitconsole
  global inpt
  commandnum = -1
  validcommand = False
  for i in range(len(commands)):
    if inpt == commands[i] and validcommand == False:
      validcommand = True
      commandnum = i

  #             3. (add an elif with the # of the spot u put ur new command)
  # Look below for examples of what u could do
  if commandnum == 0:
    print ("----------")
    print ("|Commands |")
    print ("----------")
    for i in range(len(commands)):
      print (commands[i])
  elif commandnum == 1:
    #You can use just funcions
    quit()
  elif commandnum == 2:
    for i in range(200):
      print ("\n")
  elif commandnum == 3:
    print ("Enter the name of the command you want info of")
    whichcommand = input("> ")
    foundit = False
    for i in range(len(commanddesc)):
      if whichcommand == commands[i]:
        print (commanddesc[i])
        foundit = True
    if foundit == False:
      print ("That command name doesnt exist")
  
  elif commandnum == 4:
    #THIS IS A VAR EXAMPLE FOR COMMANDS THAT NEED EXTRA JUNK
    #Just add ur inputs with the command
    print ("Enter First Num")
    x = int(input("> "))
    print ("Enter Second Num")
    y = int(input("> "))
    print ("x + y = " + str(x+y))
  else:
    print ("\"" + str(inpt) + "\" is an invalid command! Just enter the name of the command, nothing more.")
  print ("")

consolestart()
