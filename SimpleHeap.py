import random
from sys import maxint

class SimpleHeap:
  
  def __init__(self,mycmp = lambda x,y:x<y):
    self.mycmp = mycmp
    
  def heapify(self,data,n):
    self.n = n
    self.arr = [x for x in data]
    
    for i in range((self.n-2)/2,-1,-1):
      self.percolateDown(i)

  def pop(self):
    
    res = self.arr[0]
    self.n -= 1

    if self.n>0: 
      self.arr[0] = self.arr[self.n] 
      self.percolateDown(0)

    return res

  def add(self,x):
    self.n += 1
    if self.n>len(self.arr):
      self.arr.append(x)
      if self.n>len(self.arr): 
        print "Arr Error"
    else:
      self.arr[self.n-1] = x

    self.percolateUp(self.n-1)    


  def percolateDown(self,i):
    child = 2*i + 1
    while child<self.n:
      if child+1<self.n and self.mycmp(self.arr[child+1],self.arr[child]):
        child += 1
      if self.mycmp(self.arr[child],self.arr[i]):
        tmp = self.arr[child]
        self.arr[child] = self.arr[i]
        self.arr[i] = tmp
        
      else:
        break
      i = child
      child = i*2 + 1 
      
  def percolateUp(self,i):
    while i>0:
      par = (i-1)/2
      #print i, len(self.arr)
      self.arr[i]
      self.arr[par]
      if self.mycmp(self.arr[i],self.arr[par]):
        tmp = self.arr[par]
        self.arr[par] = self.arr[i]
        self.arr[i] = tmp
       
      else:
        break
      i = par

def simulate(arr,n):
  minV = maxint
  pos = -1
  for i in range(n):
    if arr[i] != -1 and arr[i] < minV:
      minV = arr[i]
      pos = i
  if pos == -1:
    print 'Simulation Error' 
  arr[pos] = -1
  return minV


random.seed()  
for k in range(100):
  N = 32
  n = 64
  data = [random.randint(1,N) for i in range(n)]
  add =  [random.randint(1,N) for i in range(n)]
  hp = SimpleHeap()
  hp.heapify(data,n)

  #print 'First stage:',hp.arr
  res = []
  for i in range(n):
    hp.add(add[i])
    res.append(hp.pop())
  while hp.n>0:
    res.append(hp.pop())


  res2 = []
  data2 = data + add
  for i in range(n):
    res2.append(simulate(data2,i+n+1))
  for i in range(n):
    res2.append(simulate(data2,2*n))

  

  for x,y in zip(res,res2):
    if x != y:
      print '='*50
      print data
      print add
      print "Test fails"
      print res
      print res2
      exit() 

print "Test passes"



