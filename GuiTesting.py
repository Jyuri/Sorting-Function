import PySimpleGUI as sg 


windowWidth = 1400
windowHeight = 780
myGraph = sg.Graph(
    (windowWidth,windowHeight),
    (0,0),
    (windowWidth,windowHeight),
    background_color='White',
    key="graph",
    expand_x=True,
    expand_y=True)

layout = [[myGraph]]

window = sg.Window("Demo",
    layout,
    margins=(0,0),
    finalize=True,
    location=(0,0))

graph = window['graph']
myLines = []
slope = windowHeight/windowWidth
for i in range(0, int(windowWidth/10)+1):
    myLines.append(graph.draw_line((i*10,0),(i*10,int(i*slope*10)),width=10))

graph.MoveFigure(myLines[10],-30,0)
graph.MoveFigure(myLines[7], 30,0)


#myLine = graph.draw_line((10,10),(10,190),color='black',width=10)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
