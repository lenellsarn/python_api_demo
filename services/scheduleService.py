
from fakeStorage import data
import datetime

def getTodaysTasks():
    today = datetime.datetime.today()
    tasks = data.getTasks()
    mappings = data.getDailyTasks()
    result = []

    for task in tasks:
        for mapping in mappings:
            if task["id"] == mapping["taskId"] and mapping["date"] == today:
                result.append(task)                
    
    return result

def getFutureTasks():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    tasks = data.getTasks()
    mappings = data.getDailyTasks()
    result = []

    for task in tasks:
        for mapping in mappings:
            if task["id"] == mapping["taskId"] and mapping["date"] == tomorrow:
                result.append(task)        

    
    return result
