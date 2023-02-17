class Attitude():
    def __init__(self, name, restrictions):
        self.name = name
        self.restrictions = restrictions

    def __repr__(self) -> str:
        return repr(self.name)

    def execute(self):
        pass

    def checkSatisfied(self, beliefs):
        pass

    def getRestrictions(self) -> dict:
        return self.restrictions

    def checkRestrictions(self, beliefs: dict) -> bool:
        intersect = set((self.getRestrictions().keys())).intersection(beliefs.keys())                
        for key in intersect:
            if self.getRestrictions()[key] != beliefs[key]:
                return False
        return True

class Desire(Attitude):
    def __init__(self, name, options = list(), restrictions = dict(), satisfied = dict()):
        super().__init__(name, restrictions)
        self.options = options
        self.satisfied = satisfied

    def execute(self, beliefs) -> Attitude:
        return self.deliberate(beliefs)

    def filter(self, beliefs: dict) -> "list[Attitude]":
        selectedOptions = list(self.options)
        print("Options", self.options)
        for option in self.options:
            option: Attitude

            if not option.checkRestrictions(beliefs):
                selectedOptions.remove(option)

        return selectedOptions
        
    def deliberate(self, beliefs):
        filteredOptions = self.filter(beliefs)
        print("Fitlered", filteredOptions)
        if(filteredOptions):
            return filteredOptions[0]
        
        return "error"

    def getSatisfied(self) -> dict:
        return self.satisfied 

    def checkSatisfied(self, beliefs) -> bool:
        intersect = set(self.getSatisfied().keys()).intersection(beliefs)
        for key in intersect:
            if self.getSatisfied()[key] != beliefs[key]:
                return False
        
        return True

    
class Action(Attitude):
    def __init__(self, name, plan, restrictions = dict()):
        super().__init__(name, restrictions)
        self.plan = plan
        self.success = False

    def execute(self, beliefs):
        if(not self.plan):
            return
        
        for step in self.plan:
            step()