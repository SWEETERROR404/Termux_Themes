#!/data/data/com.termux/files/usr/bin/python3
import os
import shutil

def logo():
    
    PS1='''\nPS1=\'\[\e[38;5;9m\]\[\e[1m\]┌─[\[\e[38;5;14m\]\[\e[1m\]<———(••\[\e[0m\]\[\e[38;5;9m\] \[\e[3m\]\[\e[1m\]SWEET\[\e[0m\]\[\e[38;5;202m\]\[\e[3m\]\[\e[1m\]ERROR\[\e[0m\]\[\e[38;5;203m\]\[\e[3m\]\[\e[1m\]404\[\e[0m\] \[\e[38;5;14m\]\[\e[1m\]••)———>\[\e[0m\]\[\e[38;5;9m\]]─[\[\e[38;5;46m\]\e[1m\]\e[3m\]\w\[\e[0m\]\[\e[38;5;9m\]\e[1m\]]\n\[\e[38;5;9m\]└──╼ \[\e[38;5;11m\]\$\[\e[0m\] \'\n\n'''

    path = "/data/data/com.termux/files/usr/etc/bash.bashrc"
    with open(path,"r") as bash_file:
        data = bash_file.read()
        count = 0
        index = []
        
        while True:
            f = data.find("PS1=",count)
            index.append(f)
            if f == -1:
                break
            count+=1
        
        index = list(set(index))
        index = max(index)
        
        start = data[index:-1].split("#")[0]    
        data = data.replace(start,PS1)
    
        with open(path,"w") as w:
            w.write(data)
            del count,index,data,start,w,f,bash_file,path,PS1 


def copy(file_name,r,w):
    path = "/data/data/com.termux/files/home/.termux/"
    file = file_name

    if os.path.exists(path+file):
        os.remove(path+file)
  
    if os.path.exists(path+file) == False:
        with open(f"files/{file}",r) as r:
            with open(f"{path}{file}",w) as w:
                w.write(r.read())
    
    del path,file,r,w




logo()
copy("termux.properties","r","w")
copy("colors.properties","r","w")
copy("font.ttf","rb","wb")
os.system("termux-reload-settings")
