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
      print('at capacity is false is working!')
      if self.isEmpty() is True: #EMPTY
        print('is empty is true is working!')
        self.storage.insert(self.current, item) #ADD ITEM TO STORAGE
      elif self.isEmpty() is False: #NOT EMPTY 
        print('is empty is false is working!')
        self.storage[self.current+1] = self.storage[self.current] #MOVE ITEM AT CURRENT INDEX TO NEXT ONE
        self.storage[self.current] = item #REASSIGN CURRENT INDEX OF STORAGE TO THE NEW ITEM 
    elif self.atCapacity() is True: 
      print('at capacity is true is working!')
      if self.isEmpty() is False:
        self.storage[-1] = item       

  def get(self):
    return self.storage
      

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
