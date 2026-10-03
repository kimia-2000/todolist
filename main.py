# import argparse


tasks=[]
file_path="data/task.txt"


#===========================================================================================================

def load_taskes():
    """read tasks from file to list"""
    with open(file_path,"r",encoding="utf-8") as f:
        return f.read().splitlines()


#===========================================================================================================

def save_taskes():
    """save taskes from list to file"""
    with open(file_path,"w",encoding="utf-8") as f:
        for task in tasks:
            f.write(task)

#===========================================================================================================

def add_task(tasks,task):
    """add task to list"""
    tasks.append(task)



#============================================================================================================
def delet_task(tasks,index):
    """delet task from list"""
    tasks.pop(index)




#============================================================================================================
def show_task(tasks):
    """show task of list"""
    for task in tasks:
        print(task)
     


#============================================================================================================


#فراخوانی
tasks=load_taskes()
for task in tasks:
    print(task)

show_task(tasks)


