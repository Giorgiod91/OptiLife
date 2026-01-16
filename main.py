

class Task(self,name:str, weekly_hours:float, deadline_day:int, priority:int, start_date:int):
    self.name = name
    self.weekly_hours = weekly_hours
    self.deadline_day =deadline_day
    self.priority = priority



    # will do calculation of amount of sress the task adds to the person depending on 
    #priority and how far aweay the deadlin day is and also how many hours will be spend
    if deadline_day - start_date <7:
        amount:int = 65


class Day(self,name:str, energy:int, stress:int):
    self.name = name
    self.energy = energy
    self.stress = stress



    # function to add to the stress lvl
    def addStress(stress:int, task:Task):
        #variables for the maximum amount of stress i choose 100 
        max_stress:int = 100
        # variable to indicate that stress is pretty high (want thise for plot later)
        high_stress_lvl:int = 80
        # moderate lvl of stress
        moderate_stress_lvl:int = 50
        # easy going if greater 0 and below 30
        easyy_going:int = stress >0 and <30
        #increase stress by amount
        # create amount and later decide which amount all those task give to the stress lvl
        amount:int  = 0

        if(stress >0 and <100):
            stress += amount
        
