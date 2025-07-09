import json 
from pathlab import path 
 
DATA_PATH = path (__file__).resolve().parent.parent /"data"/"todo.json"

def add_task(title:str):
    with open (DATA_PATH,"r") as file:
        tasks = json.load(file)

    #naya task
    task ={
        "id":len(tasks)+ 1,
        "title": title,
        "completed":False
    }


    tasks.append(task)

    with open(DATA_PATH,"W") as file:
        json.dump(tasks,file,indent=4)

