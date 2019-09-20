class Node:
  """this is to hold the pointer for the queue in the buffer""" 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 
    def __str__(self): 
        return str(self.data)

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item): # we'd pass in an instance of Node -- , likely node.data here 
    if self.isEmpty(): # AND IS NOT AT CAPACITY 
      

  def get(self):
    pass 

  def isEmpty(self):
    """returns true if buffer is empty""" 
    if self.storage is [None]*self.capacity: 
      return True 
    else:
      return False

  def atCapacity(self): 
    """returns true if buffer is at capacity""" 
    pass
