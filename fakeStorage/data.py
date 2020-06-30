import datetime 

def getTasks():
    tasks = [
        {
            'id': 0,
            'title': 'Clean Bathroom',
            'category': 'Cleaning',
        },
        {
            'id': 1,
            'title': 'Pack for trip',
            'category': 'Misc'
        },
        {
            'id': 2,
            'title': 'Fold cloths',
            'category': 'Laundry'
        },
        {
            'id': 3,
            'title': 'Besikta bilen',
            'category': 'Bilen'
        }
    ]

    return tasks

def getDailyTasks():
    today = datetime.datetime.today()
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    taskDayMap = [
        {
            'taskId': 0,
            'date': today
        },
        {
            'taskId': 1,
            'date': today
        },
                {
            'taskId': 2,
            'date': tomorrow
        },
        {
            'taskId': 3,
            'date': tomorrow
        }
    ]

    return taskDayMap