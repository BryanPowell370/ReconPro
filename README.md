# ReconPro
It's an optimization tool for running multiple pen-testing tools at once.

## Requirements
```bash
pip install os-sys
pip install optparse-pretty
pip install numpy
pip install termcolor
```
## Installation
```bash
git clone https://github.com/LaphingMan/ReconPro.git
```
## Usage
```bash
cd ReconPro
python ReconPro.py 
python3 ReconPro.py
```

```python
          _____                    _____                    _____                   _______                   _____                    _____                    _____                   _______         
         /\    \                  /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \                 /::\    \        
        /::\    \                /::\    \                /::\    \               /::::\    \               /::\____\                /::\    \                /::\    \               /::::\    \       
       /::::\    \              /::::\    \              /::::\    \             /::::::\    \             /::::|   |               /::::\    \              /::::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \            /::::::\    \           /::::::::\    \           /:::::|   |              /::::::\    \            /::::::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /::::::|   |             /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \    
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \       /:::/    \:::\    \       /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \   
   /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \     /:::/    / \:::\    \     /:::/ |::|   |           /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \  
  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \   /:::/____/   \:::\____\   /:::/  |::|   | _____    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\ 
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \ |:::|    |     |:::|    | /:::/   |::|   |/\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |
/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/____/     \:::\____\|:::|____|     |:::|    |/:: /    |::|   /::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    |
\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\:::\    \      \::/    / \:::\    \   /:::/    / \::/    /|::|  /:::/    /\::/    \:::\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / 
 \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \:::\    \      \/____/   \:::\    \ /:::/    /   \/____/ |::| /:::/    /  \/_____/\:::\/:::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /  
       |:::::::::/    /    \:::\   \:::\    \       \:::\    \                \:::\    /:::/    /            |::|/:::/    /            \::::::/    /         |:::::::::/    /     \:::\    /:::/    /   
       |::|\::::/    /      \:::\   \:::\____\       \:::\    \                \:::\__/:::/    /             |::::::/    /              \::::/    /          |::|\::::/    /       \:::\__/:::/    /    
       |::| \::/____/        \:::\   \::/    /        \:::\    \                \::::::::/    /              |:::::/    /                \::/____/           |::| \::/____/         \::::::::/    /     
       |::|  ~|               \:::\   \/____/          \:::\    \                \::::::/    /               |::::/    /                  ~~                 |::|  ~|                \::::::/    /      
       |::|   |                \:::\    \               \:::\    \                \::::/    /                /:::/    /                                      |::|   |                 \::::/    /       
       \::|   |                 \:::\____\               \:::\____\                \::/____/                /:::/    /                                       \::|   |                  \::/____/        
        \:|   |                  \::/    /                \::/    /                 ~~                      \::/    /                                         \:|   |                   ~~              
         \|___|                   \/____/                  \/____/                                           \/____/                                           \|___|                                   
                                                                                                                                                                                                        

Usage: ReconPy [-u <Target>] [-p <Photon>] [-a <AMASS>] [-s <Sublist3r>] [-n <Nmap>] [-m <Masscan>] [-g <Gobuster>]
Usage: ReconPy [--dir <Project Name - Output Folder>] 
Usage: ReconPy [--edit  <Edit Commands>]

Options:
  -h, --help   show this help message and exit
  -u TARGET    Target URL
  --dir=NAME   You need to put the location of the folder to save your output.
               Example: ~/Desktop/Recon/SaveFolder or
               ~/Documents/Recon/SaveFolder
  --edit=EDIT  p <Photon> a <Amass> s <Sublist3r>  n <Nmap> m <Masscan> g
               <Gobuster>
  -p           Photon
  -a           AMASS
  -s           Sublist3r
  -n           Nmap
  -m           Masscan
  -g           Gobuster
  ```

## Start Notes
When you first start the program it will ask you to create a main directory folder such as ~/Desktop/Recon/Target or ~/Desktop/(Where Ever You Want Your Output). 
If you want to change directory you can either use the ```--dir ~/SaveFolder``` to change this will also be where your outputs will be saved. 
When you first start a program it will not have any commands so you can simply add all of the commands you want to use in the begining or just ise the ```--edit``` command to change the commands. **You don't have to enter the target or output.** 

## Implimentation Map
Amass doesn't currently support configuration **It needs to.**
Needs more tools that to different things such as java parser, get file.extintion, and file editing.
GUI interface for ReconPro in the paid viersion.
GUI should have a modular tool implimentation.
