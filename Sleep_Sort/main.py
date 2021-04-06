"""
SleepSort (A Horrible, Horrible Algorithm)

Given some integers we want to sort e.g. 3,1,5,4,2

-create a new thread for each integer
-inside the thread, sleep for the integer's value
-add the integer to a resulting collection

Once all the threads done running, the resulting
collection will contain the integers in sorted order.
(Can you explain how they will end up sorted?)

Let's Implement! You're free to look up questions on
Google, StackOverflow, etc.

Imagine this is a normal work day, use all tools
available to you.

Hint: Get a first iteration running, iterate and
improve afterwards.
"""
import asyncio as sync

class SleepSortSystem(object):

  def __init__(self, lst):
    self.lst = lst
    self.sorted_lst = []

  async def runSystem(self):
    lst = [self.runThread(v) for v in self.lst]
    await sync.gather(*lst)

  async def runThread(self, value):
    #sleep value amount
    await sync.sleep(value)
    #print("appending: ", value)
    self.sorted_lst.append(value)

if __name__ == "__main__":
  s = SleepSortSystem([3,1,5,4,2])
  sync.run(s.runSystem())
  print(s.sorted_lst)
  
