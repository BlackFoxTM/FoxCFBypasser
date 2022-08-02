import colorama , pyfiglet
import socket , sys , os
if "win" in sys.platform:
  os.system("pip install colorama pyfiglet")
else:
  os.system("pip3 install colorama pyfiglet")

def clear():
  if "linux" in sys.platform:
    os.system("clear")
  else:
    os.system("cls")
clear()

rd = colorama.Fore.RED
mag = colorama.Fore.MAGENTA
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
bl = colorama.Fore.LIGHTBLUE_EX
yl = colorama.Fore.LIGHTGREEN_EX
def banner():
  fg = pyfiglet.Figlet(font="standard").renderText("Fox Flare")
  print (bl + fg)
  print (mag + "B F S T \n[&] Black Fox Security Team")
  print (gn + "[-] New Tools Resolve Cloud Flare Host ")
  print (rd + "[-] CloudFlare bypasser , Get Real IP of website")
  print (mag + "[-] Created By Maximum Radikali")
  print (bl + "Channel : t.me/BlackFoxSecurityTeam" )

banner()
opt = input(gn + "[$] 1) - > single URL\n[$] 2) - > multiple URL (with Text file list)\n\n[%] Select an option\n[#] ->  ")

if opt == "1":
  site = input(mag + "\n\n[&] Please Enter a URL : ")
  if "/" in site:
    url = site.split("/")[2]
    print (url)
    f = open("dom.txt","r")
    print (yl + "Waiting ...")
    for i in f:
      k = i.strip()
      try:
        fs = socket.gethostbyname(k+url)
        print (gn + fs + cv)
        
      except:
        pass
    else:
      f = open("dom.txt","r")
      print (yl + "waiting ...")
      for i in f:
        k = i.strip()
        try:
          fs = socket.gethostbyname(k+site)
          print (gn + fs + cv)
        except:
          pass
  print ("The operation has been successfully :)")
elif opt == "2":
  namefile = input(bl + "please enter a list file name -> ")
  site = open(namefile , "r")
  for t in site:
    s = t.strip("\n")
    if "/" in s:
      url = s.split("/")[2]
      print (rd + url)
      f = open("dom.txt","r")
      print (yl + "Waiting ...")
      for i in f:
        k = i.strip()
        try:
          fs = socket.gethostbyname(k+url)
          print (gn + fs + cv)
          
        except:
          pass
    else:
      print (rd + "site is %s" % s)
      f = open("dom.txt","r")
      print (yl + "waiting ...")
      for i in f:
        k = i.strip()
        try:
          fs = socket.gethostbyname(k+s)
          print (gn + fs + cv)
        except:
          pass
  print ("finished")
  
