preferences_dict = {
    "Wash the Dishes" : ["Cook Dinner","Wash Clothes"],
    "Cook Dinner" : ["Do Ironing", "Clean Windows"],
    "Do Ironing" : ["Wash Clothes", "Wash the Dishes"],
    "Wash Clothes" : ["Cook Dinner", "Clean Windows"],
    "Clean Windows" : ["Wash the Dishes", "Do Ironing"]
    }

def get_preferred_option(task_A, task_B):
        for key in preferences_dict:
                if key == task_A.description and task_B.description in preferences_dict[key]:
                        return task_A.description
                elif task_B not in preferences_dict:
                        self.task1=Task("Wash the Dishes",60)
                        self.task2=Task("Cook Dinner",40)
                        self.task3=Task("Clean Windows",30)
                        self.task4=Task("Do Ironing",10)
                        self.task5=Task("Wash Clothes",30)