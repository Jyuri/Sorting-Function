from random import randrange
from time import sleep

import sys
from tqdm import tqdm
import PySimpleGUI as sg


windowWidth=1400
windowHeight=780
numOfIntervals=780
slope = windowHeight/windowWidth
step = windowWidth/numOfIntervals

myGraph = sg.Graph(
  (windowWidth,windowHeight),
  (0,0),
  (windowWidth,windowHeight),
  background_color='White', key='graph')

window = sg.Window('Demo', layout=[[myGraph]], margins=(0,0),location=(0,0)).finalize()
graph = window['graph']

myLines = []
for i in range(0, int(windowWidth/step)+1):
  myLines.append(graph.draw_line(
    (i*step,0),
    (i*step,i*slope*step),
    width=step)
  )

def graphicSwap(startVal, endVal):
  graph.relocate_figure(myLines[startVal], endVal*step, 0)
  graph.relocate_figure(myLines[endVal], startVal*step, 0)

  tempS = myLines[startVal]
  tempE = myLines[endVal]

  myLines[startVal] = tempE
  myLines[endVal] = tempS

  window.finalize()

def graphicShift(startVal, endVal):
  graph.relocate_figure(myLines[startVal], endVal*step, 0)
  window.finalize()

#Function for traditional sorting method of moving the highest value right
def quickSort(x):
  i = 0
  numTrans = 0
  tempNumTrans = 0
  while True:
    if i == (len(x)-1):
      i = 0
      if tempNumTrans != numTrans:
        tempNumTrans = numTrans
      elif tempNumTrans == numTrans:
        break
    if x[i] > x[i+1]:
      graphicSwap(i, i+1)

      y = x[i]
      z = x[i+1]
      x[i] = z
      x[i+1]= y
      numTrans += 1

      #sleep(0.05)
    i += 1
  return x

#Function for sorting by moving the greater value to the right, but compares values moving right and left.
def ForwardAndBackSort(x):
  i = 0
  numTrans = 0
  tempNumTrans = 0
  forwardCondition = True
  while True:
    if i == (len(x)-1):
      i = 0
      if tempNumTrans != numTrans:
        tempNumTrans = numTrans
      elif tempNumTrans == numTrans:
        break

      if forwardCondition == True:
        forwardCondition = False
      elif forwardCondition == False:
        forwardCondition = True

    if forwardCondition == True:
      if x[i] > x[i+1]:
        graphicSwap(i, i+1)

        y = x[i]
        z = x[i+1]
        x[i] = z
        x[i+1]= y
        numTrans += 1

    elif forwardCondition == False:
      iRev = (len(x) - 1 - i)
      if x[iRev] < x[iRev-1]:
        graphicSwap(iRev, iRev-1)

        y = x[iRev]
        z = x[iRev-1]
        x[iRev] = z
        x[iRev-1]= y
        numTrans += 1

    i += 1
  return x

#A semi-sorting function designed to split an array into 4 chunks of similar sizes.
#Meant to work with another sorting function to speed up the sorting process of large arrays
def chunkSorting(x):
  chunkDef = len(x)/4
  chunk1 = [[0,(chunkDef)],[]]
  chunk2 = [[chunkDef,(chunkDef*2)],[]]
  chunk3 = [[(chunkDef*2),(chunkDef*3)],[]]
  chunk4 = [[(chunkDef*3),(chunkDef*4)],[]]
  errChunk = []

  for i in range(0,len(x)):
    if chunk1[0][0] <= x[i] & x[i] < chunk1[0][1]:
      chunk1[1].append([x[i],i])
    elif chunk2[0][0] <= x[i] & x[i] < chunk2[0][1]:
      chunk2[1].append([x[i],i])
    elif chunk3[0][0] <= x[i] & x[i] < chunk3[0][1]:
      chunk3[1].append([x[i],i])
    elif chunk4[0][0] <= x[i] & x[i] < chunk4[0][1]:
      chunk4[1].append([x[i],i])
    else:
      errChunk.append([x[i],i])
  
  global myLines
  x = []
  myNewLines = []
  iT = 0
  for i in range(0,len(chunk1[1])):
    graphicShift(chunk1[1][i][1],iT)
    iT += 1
    myNewLines.append(myLines[chunk1[1][i][1]])
    x.append(chunk1[1][i][0])
  for i in range(0,len(chunk2[1])):
    graphicShift(chunk2[1][i][1],iT)
    iT += 1
    myNewLines.append(myLines[chunk2[1][i][1]])
    x.append(chunk2[1][i][0])
  for i in range(0,len(chunk3[1])):
    graphicShift(chunk3[1][i][1],iT)
    iT += 1
    myNewLines.append(myLines[chunk3[1][i][1]])
    x.append(chunk3[1][i][0])
  for i in range(0,len(chunk4[1])):
    graphicShift(chunk4[1][i][1],iT)
    iT += 1
    myNewLines.append(myLines[chunk4[1][i][1]])
    x.append(chunk4[1][i][0])
  for i in range(0,len(errChunk)):
    graphicShift(errChunk[i][1],iT)
    iT += 1
    myNewLines.append(myLines[errChunk[i][1]])
    x.append(errChunk[i][0])
  myLines = myNewLines

  return x

def varChunkSorting(x, y=4):
  chunkDef = len(x)/y
  chunks = []
  for i in range(0,y):
    chunks.append([[(chunkDef*(i)),(chunkDef*(i+1))],[]])
  chunks.append([['Error Chunk'],[]])

  for i in range(0,len(x)):
    for iC in range(0,len(chunks)):
      if chunks[iC][0][0] == 'Error Chunk':
        pass
      elif chunks[iC][0][0] <= x[i] & x[i] < chunks[iC][0][1]:
        chunks[iC][1].append([x[i],i])
        appended = True
    if appended != True:
      chunks[y][1].append([x[i],i])
    appended = False
    
  
  global myLines
  x = []
  myNewLines = []
  iT = 0
  for iC in range(0,len(chunks)):
    for i in range(0,len(chunks[iC][1])):
      graphicShift(chunks[iC][1][i][1],iT)
      iT += 1
      myNewLines.append(myLines[chunks[iC][1][i][1]])
      x.append(chunks[iC][1][i][0])

  myLines = myNewLines

  return x

if __name__ == "__main__":
  #Initialize array of increasing values
  tempArray = []
  for i in range(0, len(myLines)):
    tempArray.append(i)


  #Random distribution of values from an organized list using randrange
  for iStart in range(0, len(myLines)):
    iEnd = randrange(0, len(myLines))
    graphicSwap(iStart, iEnd)
    
    x = tempArray[iStart]
    y = tempArray[iEnd]
    tempArray[iStart] = y
    tempArray[iEnd] = x

    #sleep(0.1)

  #Traditional sorting method of moving the highest value right
  #quickSort(tempArray)

  #Similar to "Quick Sort" with the exception of scanning left, and then reversing right.
  #tempArray = varChunkSorting(tempArray,8)
  #tempArray = chunkSorting(tempArray)
  ForwardAndBackSort(tempArray)

  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break

window.close()