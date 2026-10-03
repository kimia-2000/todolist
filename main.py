import argparse


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
def delete_task(tasks,index):
    """delete task from list"""
    tasks.pop(index)




#============================================================================================================
def show_task(tasks):
    """show task of list"""
    for task in tasks:
        print(task)
     


#============================================================================================================
parser=argparse.ArgumentParser()
subparsers=parser.add_subparsers(dest="command" , required=True)

add_parser=subparsers.add_parser("add")
add_parser.add_argument("task")

list_parser=subparsers.add_parser("list")

delete_parser=subparsers.add_parser("delet")
delete_parser.add_argument("index",type=int)

args=parser.parse_args()
