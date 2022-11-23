#import everything in file needs to be added to __Main__
import matplotlib.pyplot as plt
import numpy as np

parsedinput = []
xField = []
yField = []

def inputFunct():
    intpt = input("Please enter the string you wish to be converted to a graph.")
    return(intpt)


def mainfunct(inpet):
    x = np.linspace(start=0,stop=100,num=100)
    counter = 0
    for t in inpet:
        numtrans = ord(t)
        parsedinput.append((numtrans,x[counter]))
        counter+=1
    for tw in parsedinput:
        xw = tw[0]
        yw = tw[1]
        xField.append(xw)
        yField.append(yw)
    x = np.asarray(xField)
    y = np.asarray(yField)
    fig, ax = plt.subplots()
    ax.plot(xField,yField)
    plt.show()


def Runnerfunc():
    inpet = inputFunct()
    mainfunct(inpet)


if __name__ == '__main__':
    Runnerfunc()
