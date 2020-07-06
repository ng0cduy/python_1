import queue

# #FIFO :first in first out
# q =queue.Queue()
# # Dua gia tri vao hang doi
# for i in range (1,6):
#     q.put(i)

# #Lay gia tri tu hang doi
# while not q.empty():
#     print(q.get())

#LIFO
q =queue.LifoQueue()
# Dua gia tri vao hang doi
for i in range (1,6):
    q.put(i)

#Lay gia tri tu hang doi
while not q.empty():
    print(q.get())