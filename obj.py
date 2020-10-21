class Test():
  def __init__(self,count,value):
    self.count = count
    self.value = value

  def doThing(self):
    for g in range(self.count):
      print(self.value,"\n")