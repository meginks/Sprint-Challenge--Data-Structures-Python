#***************************************************************************************************************
#**********************ORIGINAL CODE THAT WAS GIVEN*************************************************************
#***************************************************************************************************************
# RUNTIME OF THIS: O(N^2) because of nested for loops - it's going over 10,000 names multiplied by 10,000. EEEK!
#***************************************************************************************************************
#  import time

# start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

#***************************************************************************************************************
#******************************MY OPTIMIZED CODE ***************************************************************
#***************************************************************************************************************
# RUNTIME OF THIS: o(n) because you have to go through the 10000 names once.
#***************************************************************************************************************

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close() 
print(len(names_1), "names one length")
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
print(len(names_2), "names two length")

duplicates = [] 
for i in range(len(names_1)):
    if names_2.count(names_1[i]) == 1:
        duplicates.append(names_1[i])
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

