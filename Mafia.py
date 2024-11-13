import random
import tkinter as tk
import os
# i will be fixing it soon

def add_player(name):
    global chances
    global roles
    default = {"active":True, "name":name}
    for i in roles:
        default[i[0]]=i[2]
    chances.append(default)
    return (f"Player {name} succesfully added")
    
def add_role(name, seats, starting_chances, minimal_chances, maximal_chaances):
    global chances
    global roles
    roles.append([name, seats,starting_chances, minimal_chances, maximal_chaances])
    for i in chances:
        i[name] = starting_chances
    return (f"Role {name} succesfully added")
    
def delete_role(name):
    global chances
    global roles
    for i in chances:
        i.pop(name)
    id = 0
    for i in roles:
        if i[0] == name:
            roles.pop(id)
            break
        id+=1
    return (f"Role {name} succesfully deleted")
        
def suspend_player(name):
    global chances
    global roles
    for i in chances:
        if i['name']==name:
            i['active']=False
            return (f"Player {name} succesfully suspended")
    return("Couldn't suspend the player")
def activate_player(name):
    global chances
    global roles
    for i in chances:
        if i['name']==name:
            i['active']=True
            return (f"Player {name} succesfully activated")
            
def save_game(file):
    file = os.path.join(current_dir, file)
    f = open(file, "w")
    chan = "["
    for i in chances:
        chan+=str(dict(i))
    chan+="]"
    rol = "["
    for i in roles:
        rol+=str(i)
    rol+="]"
    f.write(chan+"\n"+rol)
    f.close()
    return ("Game saved")
    
def read_game(file):
    global chances
    global roles
    file = os.path.join(current_dir, file)
    f = open(file, "r")
    read = f.read()
    f.close()
    chances_read=read.split("\n")[0].replace("[{","}{").replace("}]","}{").split("}{")
    roles_read=read.split("\n")[1].replace("[[","][").replace("]]","][").split("][")
    chances = []
    temporary = {}
    for dic in chances_read:
        temporary = {}
        if len(dic)>0:
            for word in dic.replace(" ","").split(","):
                if word.split(":")[1].find("'")!=-1:
                    temporary[word.split(":")[0].replace("'","")]=str(word.split(":")[1].replace("'",""))
                elif word.split(":")[1]=="False" or word.split(":")[1]=="True":
                    temporary[word.split(":")[0].replace("'","")]=bool(word.split(":")[1])
                else:
                    temporary[word.split(":")[0].replace("'","")]=int(word.split(":")[1])
            chances.append(temporary)
    print(chances)
    roles = []
    temporary = []
    for arr in roles_read:
        temporary = []
        if len(arr)>0:
            for word in arr.split(", "):
                if word.find("'")!=-1:
                    temporary.append(str(word.replace("'","")))
                else:
                    temporary.append(int(word))
            roles.append(temporary)
    
    return ("Game was read")
    
def give_roles():
    overall = 0
    chosen = []
    for i in roles:
        for seats in range(0,i[1]):
            overall = 0
            for e in chances:
                if e['active'] and e['name'] not in chosen:
                    overall+=e[i[0]]
            who = round(random.randint(1,overall))
            overall = 0
            for e in chances:
                if e['active'] and e['name'] not in chosen:
                    overall+=e[i[0]]
                    if who <= overall and who>overall-e[i[0]]:
                        chosen.append(i[0])
                        chosen.append(e['name'])
                        for d in roles:
                            if d[0]==i[0]:
                                e[i[0]]=d[3]
                        break
    chosen2 = []
    for i in roles:
        chosen2.append([i[0]])
    for t in range(0,len(chosen),2):
        for d in chosen2:
            if d[0] == chosen[t]:
                d.append(chosen[t+1])
    max = 0
    for role in chosen2:
        for r in chances:
            if r['name'] not in role and r['active']:
                r[role[0]]=int(r[role[0]]*1.10)
                for d in roles:
                    if d[0]==role[0]:
                        max=d[4]
                if r[role[0]]>max:
                    r[role[0]]=max
    return(chosen2)
def show_roles():
    return (roles)
def show_players(name):
    if name == 'all':
        return str(chances).replace("}, {","}\n{")
    else:
        for dict in chances:
            if dict['name']==name:
                return str(dict)

def add_user_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Add Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the new user")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = add_player(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()

    tk.Button(addUserWindow,text="Add Player", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)

def suspend_user_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Suspend Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the player you want to suspend")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = suspend_player(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()

    tk.Button(addUserWindow,text="Suspend", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def suspend_user_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Suspend Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the player you want to suspend")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = suspend_player(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()

    tk.Button(addUserWindow,text="Suspend", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
def add_role_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Add Role")
    addUserWindow.config(bg=color)
    name = tk.Label(addUserWindow,text ="Name of the role you want to add")
    name.grid(column=0, row=0, padx=5, pady=5) 
    name1 = tk.Entry(addUserWindow)
    name1.grid(column=0, row=1, padx=5, pady=5)
    seats = tk.Label(addUserWindow,text ="How many players will be assigned this role")
    seats.grid(column=0, row=2, padx=5, pady=5)
    seats1 = tk.Entry(addUserWindow)
    seats1.grid(column=0, row=3, padx=5, pady=5)
    starting_chances = tk.Label(addUserWindow,text ="Default starting chances for the role")
    starting_chances.grid(column=0, row=4, padx=5, pady=5)
    starting_chances1 = tk.Entry(addUserWindow)
    starting_chances1.grid(column=0, row=5, padx=5, pady=5)
    minimal_chances = tk.Label(addUserWindow,text ="Minimal chances for the role")
    minimal_chances.grid(column=0, row=6, padx=5, pady=5)
    minimal_chances1 = tk.Entry(addUserWindow)
    minimal_chances1.grid(column=0, row=7, padx=5, pady=5)
    maximal_chances = tk.Label(addUserWindow,text ="Maximal chances for the role")
    maximal_chances.grid(column=0, row=8, padx=5, pady=5)
    maximal_chances1 = tk.Entry(addUserWindow)
    maximal_chances1.grid(column=0, row=9, padx=5, pady=5)

    def btn_add_user():
        rt = add_role(name1.get(), int(seats1.get()), int(starting_chances1.get()), int(minimal_chances1.get()), int(maximal_chances1.get()))
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()

    tk.Button(addUserWindow,text="Add", font=('Times 14'), command=btn_add_user).grid(column=0, row=10, padx=5, pady=5)  
    
def delete_roll_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Suspend Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the role you want to delete")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = delete_role(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()
    tk.Button(addUserWindow,text="Delete", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def activate_user_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Activate Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the player you want to Activate")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = activate_player(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()
    tk.Button(addUserWindow,text="Activate", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def save_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Save Game")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the save file")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.insert(0,"savefile.txt")
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = save_game(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()
    tk.Button(addUserWindow,text="Save", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def read_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Read Game")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the save file")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.insert(0,"savefile.txt")
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = read_game(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()
    tk.Button(addUserWindow,text="Read", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)

def showU_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Show Player")
    addUserWindow.config(bg=color)
    labelAddUser = tk.Label(addUserWindow,text ="Name of the player (all to display all)")
    labelAddUser.grid(column=0, row=0, padx=5, pady=5)
    entryAddUser = tk.Entry(addUserWindow)
    entryAddUser.insert(0,"all")
    entryAddUser.grid(column=0, row=1, padx=5, pady=5)

    def btn_add_user():
        rt = show_players(entryAddUser.get())
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =rt).pack()
    tk.Button(addUserWindow,text="Show", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def showR_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Show Role")
    addUserWindow.config(bg=color)

    def btn_add_user():
        rt = show_roles()
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =str(rt).replace("], [","\n")).pack()
    tk.Button(addUserWindow,text="Show", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
    
def give_window():
    addUserWindow = tk.Toplevel(rt)
    addUserWindow.title("Give Roles")
    addUserWindow.config(bg=color)

    def btn_add_user():
        rt = give_roles()
        addUserSuccess = tk.Toplevel(addUserWindow)
        addUserWindow.config(bg=color)
        tk.Label(addUserSuccess,text =str(rt).replace("], [","\n")).pack()
    tk.Button(addUserWindow,text="Give", font=('Times 14'), command=btn_add_user).grid(column=0, row=2, padx=5, pady=5)
global color
color = "#151716"
current_dir = os.path.dirname(__file__)
global chances
chances = []
global roles
roles = [["Detektyw",1,75,40,150],["Mafia",2,75,40,150]]

rt = tk.Tk()
rt.title("Mafia")
rt.config(bg=color)

path = os.path.join(current_dir, "add-user.png")
img1=tk.PhotoImage(file=path)
adduser = tk.Button(rt, image=img1,command=add_user_window)
adduser.grid(column=0, row=0, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Add Player", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=0, row=1, padx=5, pady=5)

path2 = os.path.join(current_dir, "suspend-user.png")
img2=tk.PhotoImage(file=path2)
adduser = tk.Button(rt, image=img2,command=suspend_user_window)
adduser.grid(column=1, row=0, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Suspend Player", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=1, row=1, padx=5, pady=5)

path3 = os.path.join(current_dir, "add-role.png")
img3=tk.PhotoImage(file=path3)
adduser = tk.Button(rt, image=img3,command=add_role_window)
adduser.grid(column=0, row=2, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Add Role", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=0, row=3, padx=5, pady=5)

path4 = os.path.join(current_dir, "delete-role.png")
img4=tk.PhotoImage(file=path4)
adduser = tk.Button(rt, image=img4,command=delete_roll_window)
adduser.grid(column=1, row=2, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Delete Role", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=1, row=3, padx=5, pady=5)

path5 = os.path.join(current_dir, "activate-user.png")
img5=tk.PhotoImage(file=path5)
adduser = tk.Button(rt, image=img5,command=activate_user_window)
adduser.grid(column=0, row=4, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Acttivate Player", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=0, row=5, padx=5, pady=5)

path6 = os.path.join(current_dir, "save.png")
img6=tk.PhotoImage(file=path6)
adduser = tk.Button(rt, image=img6,command=save_window)
adduser.grid(column=1, row=4, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Save Game", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=1, row=5, padx=5, pady=5)

path7 = os.path.join(current_dir, "read.png")
img7=tk.PhotoImage(file=path7)
adduser = tk.Button(rt, image=img7,command=read_window)
adduser.grid(column=0, row=6, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Read Game", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=0, row=7, padx=5, pady=5)

path8 = os.path.join(current_dir, "show-user.png")
img8=tk.PhotoImage(file=path8)
adduser = tk.Button(rt, image=img8,command=showU_window)
adduser.grid(column=1, row=6, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Show User", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=1, row=7, padx=5, pady=5)

path9 = os.path.join(current_dir, "show-role.png")
img9=tk.PhotoImage(file=path9)
adduser = tk.Button(rt, image=img9,command=showR_window)
adduser.grid(column=0, row=8, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Show Roles", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=0, row=9, padx=5, pady=5)

path10 = os.path.join(current_dir, "give-role.png")
img10=tk.PhotoImage(file=path10)
adduser = tk.Button(rt, image=img10,command=give_window)
adduser.grid(column=1, row=8, padx=5, pady=5)
lbadduser = tk.Label(rt, text="Give Roles", font=('Times 14'), width=(int(rt.winfo_width()/2)))
lbadduser.grid(column=1, row=9, padx=5, pady=5)
rt.mainloop()

