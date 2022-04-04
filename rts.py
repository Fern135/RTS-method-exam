import json

class RTS:

  def __init__(self):
    print("Thank you for the oportunity")

  def aboveBellow(self, compare, myList=[]):
    above   = 0
    bellow  = 0
      
    for i in myList:
      if i < compare:
        bellow += 1

      elif i > compare:
        above += 1

      else:
        return ("this else statement should not reach here.\nIn theory\nif it does. sorry")

    # wanted to get fancy. un coment this for it to be written in a file
    # self.write(      
    #   {
    #     "above": above,
    #     "bellow": bellow
    #   }
    # )

    return json.dumps(
      {
        "above": above,
        "bellow": bellow
      }
    )

  def rotateRight(self, myString, num):
    return myString[-num:] + myString[:-num]


  def write(self, dict={}): # not needed but it's fancy    
    with open("aboveBellow.json", "w") as f:
      f.write(json.dumps(dict, indent = 4))