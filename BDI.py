from Attitude import Attitude

class BDI():
    def __init__(self, updateBeliefsCB, intentions = [], beliefs = {}, desires = {}):
        self.beliefs = beliefs
        self.desires = desires
        self.intentions = intentions
        self.updateBeliefsCB = updateBeliefsCB

    # def deliberate(self, options):
    #     selectedOptions = self.filter(options)

    #     if(selectedOptions):
    #         return selectedOptions[0]
        
    #     return "error"

    # def filter(self, options: "list[Attitude]") -> "list[Attitude]":
    #     selectedOptions = list(options)
    #     for option in options:
    #         intersect = set((option.getRestrictions().keys())).intersection(self.beliefs.keys())                
    #         for key in intersect:
    #             if option.getRestrictions()[key] != self.beliefs[key]:
    #                 selectedOptions.remove(option)

    #     return selectedOptions        

    def execute(self):
        intent: Attitude = self.peekIntention()
        if intent.checkRestrictions(self.beliefs) and not intent.checkSatisfied(self.beliefs):
            return intent.execute(self.beliefs)
        else:
            return intent

    def popIntention(self) -> Attitude:
        return self.intentions.pop()

    def addIntention(self, intention):
        self.intentions.append(intention)

    def peekIntention(self) -> Attitude:
        return self.intentions[len(self.intentions) - 1]

    def checkCurrentIntention(self):
        idx = -1
        for i, intent in enumerate(self.intentions):
            intent: Attitude
            if intent.checkSatisfied(self.beliefs):
                idx = i
                break
            if not intent.checkRestrictions(self.beliefs):
                idx = i
                break

        if idx != -1:
            for attitude in self.intentions[i:]:
                self.intentions.remove(attitude)

    def update(self):
        self.beliefs = self.updateBeliefsCB()
        self.checkCurrentIntention()
        return self.intentions

    # def getOptions(self):
    #     intent: Attitude = self.intentions[len(self.intentions) - 1]
    #     return intent.getOptions()
        
    #     # if options:
    #     #     return options
    #     # else:
    #     #     return ["executeAction"]

    def start(self):
        # Initialization stuff
        pass
