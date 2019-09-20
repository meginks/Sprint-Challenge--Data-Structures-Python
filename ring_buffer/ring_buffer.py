# class Item:
#   """this is to hold the pointer for the queue in the buffer""" 
#   def __init__(self, data=None): 
#     self.data = data 
#     self.next = None 
#   def __str__(self): 
#     return str(self.data)

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item): # we'd pass in an instance of the Item class here -- , likely item.data here 
    if self.atCapacity() is False: #NOT AT CAPACITY 
      if self.isEmpty() is True: #EMPTY
        self.storage.append(item) #ADD ITEM TO STORAGE
      elif self.isEmpty() is False: #NOT EMPTY 
        self.storage.append(item)
        self.storage.remove(self.storage[self.current]) 
    elif self.atCapacity() is True: 
      if self.isEmpty() is False:
        self.storage.append(item)   
        self.storage.remove(self.storage[self.current])  

  def get(self): 
    holding_cell = [] 
    for i in range(0, len(self.storage)): 
      if self.storage[i] == None: 
        pass 
      else: 
        holding_cell.append(self.storage[i])
    return holding_cell
      

  def isEmpty(self):
    """returns true if buffer is empty""" 
    if self.storage is [None]*self.capacity: 
      return True 
    else:
      return False

  def atCapacity(self): 
    """returns true if buffer is at capacity""" 
    if self.storage[self.current] == self.storage[-1]:
      return False 
    else: 
      return True 


#IMPLEMENT TESTS TO TRY TO SEE WHAT'S WRONG AND USE PRINT
buffer = RingBuffer(5)
print("INITIALIZE", buffer)
buffer.append('a')
print("AFTER A", buffer) 
buffer.append('b')
print("AFTER B", buffer) 
buffer.append('c')
print("AFTER C", buffer) 
buffer.append('d')
print("AFTER D", buffer) 
print("buffer get", buffer.get())