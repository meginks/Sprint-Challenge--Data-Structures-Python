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
   
      self.storage[self.current] = item
      self.current += 1
      if self.current == self.capacity: #NOT AT CAPACITY  #EMPTY
        self.current = 0
      
        # self.storage.insert(-1, item)   
        # self.storage.remove(self.storage[self.current])

        # self.storage.append(item)
        # self.current += 1 #ADD ITEM TO STORAGE


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
    if self.current == self.capacity:
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

for item in buffer.storage:
   print('item', item)