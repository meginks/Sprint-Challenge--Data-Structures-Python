class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    previous_item = None #create placeholder for previous item
    current_item = self.head #set current item to self.head 
    while(current_item is not None): #when we have an item at the current_item run code on lines 50-53
      next_item = current_item.next_node #create placeholder called next_item and set it to the next_node on current_item
      current_item.next_node = previous_item #set the next node on the current item to the item in our previous_item placeholder (first time it will be none)
      previous_item = current_item #set previous item to current item
      current_item = next_item #set current item to next item 
    self.head = previous_item #when we get to the end of the list, set the self.head to the previous_item, effectively reversing the list

