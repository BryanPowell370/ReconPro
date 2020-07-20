#!/usr/bin/python
import optparse
import os
import termcolor
from numpy import random

def main():
    GraphicTitle()
    ProjectFolder()
########################################
    parse = optparse.OptionParser("Usage: ReconPy [-u <Target>] [-p <Photon>] [-a <AMASS>]\nUsage: ReconPy [--dir <Project Name - Output Folder>] \nUsage: ReconPy [--edit  <Edit Commands>]")
    parse.add_option('-u',     dest = 'Target',    type = 'string',       help = 'Target URL'                         )
    parse.add_option('--dir',  dest = 'Name',      type = 'string',       help = 'You need to put the location of the folder to save your output. \nExample: ~/Desktop/Recon/SaveFolder or ~/Documents/Recon/SaveFolder'       )
    parse.add_option('--edit', dest = 'Edit',      type = 'string',       help =  'p <Photon> a <Amass> s <Sublist3r>  n <Nmap> m <Masscan> g <Gobuster>'   )
    # Toggle Tool
    parse.add_option('-p', action = 'store_true',     dest = 'Photon',       default=False,     help = 'Photon'     )
    parse.add_option('-a', action = 'store_true',     dest = 'AMASS',        default=False,     help = 'AMASS'      )
    parse.add_option('-s', action = 'store_true',     dest = 'Sublist3r',    default=False,     help = 'Sublist3r' )  
    parse.add_option('-n', action = 'store_true',     dest = 'Nmap',         default=False,     help = 'Nmap' )     
    parse.add_option('-m', action = 'store_true',     dest = 'Masscan',      default=False,     help = 'Masscan' ) 
    parse.add_option('-g', action = 'store_true',     dest = 'Gobuster',     default=False,     help = 'Gobuster' ) 
   
    (options,args) = parse.parse_args()
########################################   
    # Params
    Target      = options.Target
    NameProject = options.Name
    Edit        = options.Edit
   
    # Toggle Tools
    AMASS       = options.AMASS
    Photon      = options.Photon
    Sublist3r   = options.Sublist3r
    Nmap        = options.Nmap
    Masscan     = options.Masscan
    Gobuster    = options.Gobuster
########################################   
    if(NameProject != None):
        WorkingDirectory(NameProject)
    
    #  Exicute Tool
    if(Target != None):
        if(ExicuteProg(Photon) ):
          PHOTONexe(Target)
        
        elif(ExicuteProg(AMASS) ):
          AMASSexe(Target)
        
        elif(ExicuteProg(Sublist3r) ):
          SUBLIST3Rexe(Target)
      
        elif(ExicuteProg(Nmap) ):
            NMAPexe(Target)
        
        elif(ExicuteProg(Masscan) ):
            MASSCANexe(Target)
        
        elif(ExicuteProg(Gobuster) ):
            GOBUSTERexe(Target)
            
        # All Tools  
        else:
          AllProgramEXE(Target)
       

    if(Edit != None):
        EditCommands(Edit)
        
      
    #if (Target == None):
     #   print(parse.usage)
      #  exit(0)




def GraphicTitle():
    nameImages = ["ReconPro1", "ReconPro2", "ReconPro3", "ReconPro4", "ReconPro5"]
    print( termcolor.colored( str(open("TitleImages/" +nameImages[random.randint(len(nameImages))],"r").read()) , "white") )
#################################################################
    # Branchless return statement.
def ExicuteProg(Prog):
    return Prog


def AllProgramEXE(Target):
   # InfoGather
    PHOTONexe     (Target  )
    AMASSexe      (Target  )
   # Port Scanning
    NMAPexe       (Target  )
    MASSCANexe    (Target  )
    # Domain Enumeration
    SUBLIST3Rexe  (Target  )
    GOBUSTERexe   (Target  )

#################################################################
    # Folder to save output
def WorkingDirectory(NameProject):   
    open("dir.txt","w").write(NameProject)
    os.system( "mkdir " + NameProject)   

def ProjectFolder():
    try:
        return open("dir.txt").read()
    except:
        print("You need to put the location of the folder to save your output. \nExample: ~/Desktop/Recon/SaveFolder or ~/Documents/Recon/SaveFolder" )
        WorkingDirectory(input() )
        

# Were the output should go.

def Output(folder):
    return ProjectFolder() + '/' + folder
 

######################################################################### 
    # The commands to the programs we are using.
def EditCommands(Edit):
    if(Edit == 'p'):
      EditCommandsCode("Photon")
       
    if(Edit == 'a'):
      EditCommandsCode("Amass")
       
    if(Edit == 's'):
      EditCommandsCode("Sublist3r")
      
    if(Edit == 'n'):
      EditCommandsCode("Nmap")
       
    if(Edit == 'm'):
      EditCommandsCode("Masscan")
       
    if(Edit == 'g'):
      EditCommandsCode("Gobuster")
  
def EditCommandsCode(name):
      try:
        HelpMenuForPrograms(name)
        print("Current: " + name  + " " + open(name + 'Config.txt').read())      
      except:
        ConfigFileSubcommands(name)
  

                  
def ConfigFileSubcommands(name):
      p = open(name  + 'Config.txt','w')
      print(name, end=' ')
      p.write(input())
      p.close()

def HelpMenuForPrograms(name):    
      if (name == "Sublist3r" or name == "Photon"):
        os.system(os.system(str(ConfigFileStartCommands(name) + " -h ")  ))   
      else:
        os.system(name.lower() + " -h "  )
######################################################################### 
      # Create the start directory for the python main files.

def ConfigFileStartCommands(name):
    try:
         return open(name + "StartDirectory.txt",'r').read()  
    except:
         CreateConfigFileStartCommands(name)
       
def CreateConfigFileStartCommands(name):
    print(name + " Needs A Start Command. \nExample: cd /Hacking/Photon;python3 photon.py ")
    conf = open(name + "StartDirectory.txt",'w')
    conf.write(input())
    conf.close()
    exit(0)

#########################################################################

        
def CrossFileDiscovery():    
    print()
    
    
    
#################################################################
    # Programms to optimize.


def PHOTONexe(Target):
    exeDir = str(ConfigFileStartCommands("Photon")) # "cd ~/Hacking/Recon/Photon;python3  photon.py  "
    try:
       os.system(exeDir + open('PhotonConfig.txt').read() + " -u " + Target + "  -o "  + Output("Photon")  )
    except:
        print(termcolor.colored("[-]Photon Needs Commands!!!", "red") )
        EditCommands('p')

def AMASSexe(Target):
    os.system("amass db -show -ip  -d " + Target  + "  -dir  " + Output("Amass") )
    os.system("amass enum -v  -brute -min-for-recursive 2  -d " + Target  + "  -dir  " + Output("Amass") )
    os.system("amass viz -d3 -dir  " + Output("Amass") )


def NMAPexe(Target):
    try:
        os.system( "nmap  " + Target + "  " + open('NmapConfig.txt').read()  + " -oA " + Output("NMAP") )
    except:
        print(termcolor.colored("[-]Nmap Needs Commands!!!", "red") )
        EditCommands('n')

def MASSCANexe(Target):
    try:
        os.system("masscan " + Target + "  " + open('MasscanConfig.txt').read() + " -oB " + Output("Masscan"))
    except:
        print(termcolor.colored("[-]Masscan Needs Commands!!!", "red")  )
        EditCommands('m')

def SUBLIST3Rexe(Target):
    try:
        comands = open('Sublist3rConfig.txt').read() + "  -d " + Target + " -o " +  Output("Sublist3r")
        exeDir = str(ConfigFileStartCommands("Sublist3r")) #"cd ~/Hacking/Recon/Sublist3r;python3 sublist3r.py  "
        os.system(exeDir + comands)
    except:
        print(termcolor.colored("[-]Sublist3r Needs Commands!!!", "red") )
        EditCommands('s')


def GOBUSTERexe(Target):
    try:
        os.system("gobuster "+ Target + "  " + open('GobusterConfig.txt').read() + " -o " +  Output("GoBuster"))
    except:
        print(termcolor.colored("[-]Gobuster Needs Commands!!!", "red")  )
        EditCommands('g')








 

if __name__  == '__main__':
    main()

