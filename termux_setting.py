#!/data/data/com.termux/files/usr/bin/python3

import os
import shutil
import time


def backup(file):
    path = os.popen("cd $PREFIX && pwd").read().replace("\n","")+"/share/.mubeen"
    os.mkdir(path)

def selection(func):
    selection_path = os.path.join("files",func)
    
    selection_list = {}
    keys = []

    for i in os.listdir(selection_path):
        selection_list.update({i.split("_")[0]:i.split("_")[1]})
    
        keys.append(int(i.split("_")[0]))
    
    keys = sorted(keys)
    os.system("clear")
    
    def _lists():
        for i in keys:
            print(f"[*] {i} {selection_list.get(str(i)).capitalize()}")
    

    total = max(keys)
    _lists()
    
    while (True):
        try:
            
            user_input = int(input(f"Select {func} No :- "))
            if type(user_input) == int:
                if (user_input) > int(total) or (user_input) <= 0:
                    print("Wronge Input")
                    time.sleep(1)
                    os.system("clear")
                    _lists()
                else:
                    break
        
        except ValueError:
            print("Wronge Input")
            time.sleep(1)
            os.system("clear")
            _lists()
    
    p1 = f"{selection_path}"
    p2 = f"{user_input}_{selection_list.get(str(user_input))}"
    return os.path.join(p1,p2)

def copy(path,file_name,r,w):
    
    termux_path = "/data/data/com.termux/files/home/.termux/"
    
    if os.path.exists(os.path.join(termux_path,file_name)):
        os.remove(os.path.join(termux_path,file_name))

    path = os.path.join(path,file_name)
    with open(path,r) as r:
        with open(termux_path+file_name,w) as w:
            w.write(r.read())





def change_keys():
    path="/data/data/com.termux/files/home/.termux/"
    
    if os.path.exists(os.path.join(path,"termux.properties")):
        os.remove(os.path.join(path,"termux.properties"))
    
    if os.path.exists(os.path.join(path,"termux.properties"))==False:
        shutil.copy("files/keys/termux.properties",path)
        os.system("clear")
        print("Keys are Add Sucessfully")
        print("Please Close and Reopen the Termux")
        time.sleep(2)
        os.system("clear")

def select_func():
    os.system("clear")

    msg = """
\033[38;5;9m[*]\033[0m Press \033[38;5;220mT\033[0m for Change Themes
\033[38;5;9m[*]\033[0m Press \033[38;5;220mF\033[0m for Change Fonts
\033[38;5;9m[*]\033[0m Press \033[38;5;220mK\033[0m for Change Task Bar Keys
\033[38;5;9m[*]\033[0m Press \033[38;5;220mQ\033[0m for Quit
"""
    while 1:
        user = input(msg).lower()
    
        if user == "t":
            copy(selection("colors"),"colors.properties","r","w")
            os.system("termux-reload-settings")
            os.system("clear")
        
        elif user == "f":
            copy(selection("fonts"),"font.ttf","rb","wb")
            os.system("termux-reload-settings")
            os.system("clear")

        elif user == "k":
            change_keys()


        elif user == "q":
            break

        else:
            print("Invalid")
            time.sleep(1)
            os.system("clear")


def mount():
    rt=os.popen("cd $PREFIX && pwd").read().replace("\n","")+"/bin"
    
    for i in os.listdir(rt):
        if i=="nh":
            f=os.path.join(rt,i)
            backup(f)
            with open(f) as f:
                x=f.read()
                index=x.find("-b /dev \\")
                edit="\t-b /sdcard \\"+x[index+9:]
                edit=x[:index+9]+"\n"+edit
                


#mount()

select_func()
