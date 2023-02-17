from Attitude import Desire 
from Attitude import Action
import Belief
from BDI import BDI

# BeliefSet

# USE FILTER TO GET RELEVANT REQUIREMENTS
# CREATE REQUIREMENTS TABLE AND ATTACH ATTITUDES

beliefSet = {
    "ready" : True,
    "goal_in_local" : False,
    "lanes" : False,
    "lidar_feed" : False,
    "camera_feed" : False,
    "gps_feed" : False,
    "is_moving" : False,
    "obstacles" : False,
    "dead_man" : False,
    "heading_gwpt" : False,
    "heading_iwpt" : False,
    "goals_complete" : False,
    "at_iwpt" : False,
    "at_gwpt" : False
}

runtime = [
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : True,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : True,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : True,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : True,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : True,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : True,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : True
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False
    },
    {
        "ready" : True,
        "goal_in_local" : False,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : False   
    },
    {
        "ready" : True,
        "goal_in_local" : True,
        "lanes" : True,
        "goals_complete" : False,
        "at_iwpt" : False,
        "at_gwpt" : True
    },
    {
        "ready" : True,
        "goal_in_local" : True,
        "lanes" : True,
        "goals_complete" : True,
        "at_iwpt" : False,
        "at_gwpt" : True
    }
]

# Callbacks
idx = -1
def updateBeliefSet():
    # for key in beliefSet.keys():
    #     beliefSet[key] = eval(input(key + ": "))
    global idx
    # idx = idx + 1    
    # input() 
    # return runtime[idx]
    
    for key, value in beliefSet


def getVfh():
    print(" SUCCESS ")

def getLaneFollow():
    print("Lane Follow")

def getRandom():
    pass

def pubGoal():
    print("Success")
    pass

def pubFree():
    pass

def driveToGlobal():
    pass

# Actions
VFH = Action("VFH", 
    [getVfh],
    restrictions = {
        "ready" : True
    })

Lane_Follow = Action(
    "Lane Follow",
    [getLaneFollow],
    restrictions = {
        "ready": True,
        "lanes": True
    })
    
Random = Action("Random Point", [getRandom])
move_to_free = Action("Move to free", [pubFree])
drive_goal = Action(
    "Drive to goal",
    [driveToGlobal],
    restrictions = {
        "ready" : True,
        "goal_in_local" : True,
    }
    )

drive_wpt = Desire(
    "Find/Drive to Wpt",
    options = [Lane_Follow, VFH, Random],
    restrictions = {
        "ready" : True,
        "goals_complete": False,
        "goal_in_local": False
    },
    satisfied = {
        "at_iwpt" : True
    }
)

drive_gps_wpts = Desire(
    "Drive through gps",
    options = [drive_goal, drive_wpt],
    restrictions = {
        "ready" : True,
        "goals_complete" : False
    },
    satisfied = {
        "goals_complete" : True
    }
)

finish = Desire(
    "drive to finish",
    options = [drive_gps_wpts, move_to_free],
    satisfied = {
        "goals_complete" : True
    }
) 


def main():
    
    desires = []
    beliefs = beliefSet

    bdi: BDI = BDI(updateBeliefSet,  desires = desires, beliefs=beliefs, intentions = [finish])
    # while True:
    # print(bdi.intentions)
    # options = bdi.getOptions()
    # print(options)
    # desire = bdi.deliberate(options)
    # bdi.addIntention(desire)
    # bdi.execute()
    # print("Running")
    # print(bdi.intentions)

    while bdi.intentions:
        print(bdi.intentions)
        if(not bdi.update()):
            break
        desire = bdi.execute()
        print("Desire: ", desire)
        if(desire):
            if (desire != bdi.peekIntention()):
                bdi.addIntention(desire)
        else:
            bdi.popIntention()

    print(bdi.intentions)

main()