from random import randrange
from time import sleep
import sys
from tqdm import tqdm

def disorganizedList(listLength):
  unorgList = []
  for i in range(listLength):
    unorgList.append(i)
  for ix in range(listLength):
    iy = randrange(0,listLength)
    x = unorgList[ix]
    y = unorgList[iy]
    unorgList[ix] = y
    unorgList[iy] = x
  return unorgList

def quickSort(x):
  i = 0
  numTrans = 0
  tempNumTrans = 0
  pbarCheck = tqdm(desc='Check Count', total = (len(x)**2))
  pbarChange = tqdm(desc='Change Count')
  while True:
    if i == (len(x)-1):
      i = 0
      if tempNumTrans != numTrans:
        tempNumTrans = numTrans
      elif tempNumTrans == numTrans:
        break
    if x[i] > x[i+1]:
      y = x[i]
      z = x[i+1]
      x[i] = z
      x[i+1]= y
      numTrans += 1
      pbarChange.update(1)
    i += 1
    pbarCheck.update(1)
  pbarCheck.close()
  pbarChange.close()
  return x



if __name__ == "__main__":
  disorgList = disorganizedList(10000)
  orgList = quickSort(disorgList)