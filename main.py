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

def shift(startVal, endVal):
  graph.relocate_figure(myLines[startVal], endVal*step, 0)
  graph.relocate_figure(myLines[endVal], startVal*step, 0)

  tempS = myLines[startVal]
  tempE = myLines[endVal]

  myLines[startVal] = tempE
  myLines[endVal] = tempS

  window.finalize()

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
      shift(i, i+1)

      y = x[i]
      z = x[i+1]
      x[i] = z
      x[i+1]= y
      numTrans += 1

      #sleep(0.05)
    i += 1
  return x

if __name__ == "__main__":
  tempArray = []
  for i in range(0, len(myLines)):
    tempArray.append(i)

  for iStart in range(0, len(myLines)):
    iEnd = randrange(0, len(myLines))
    shift(iStart, iEnd)
    
    x = tempArray[iStart]
    y = tempArray[iEnd]
    tempArray[iStart] = y
    tempArray[iEnd] = x

    #sleep(0.1)

  quickSort(tempArray)
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break

window.close()