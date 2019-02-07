import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

def big_boi():
    MOY_num = 0
    MOY = [MOY_num]
    genera = [324]
    genera_num = 324

    marker = 0

    for i in range (100):        
        MOY_num += 5.4
        MOY.extend([MOY_num])
        event = random.randint(1,99)

        if genera_num == 0:
            genera_num = 0
        elif genera_num < 1.1:
            genera_num = 0
            plt.title("Complex life went extinct after "+str(round(MOY_num))+" million years.", color='red', fontsize=13)
            marker = 1
        elif genera_num > 100000:
            genera_num = genera_num*0.875
            
        elif event <= 7:
            genera_num = round(genera_num*0.51)
            if event == 1:
                plt.axvline(x = MOY_num, color='r')
            elif event == 2:
                plt.axvline(x = MOY_num, color='purple')
        elif event <= 18:
            genera_num = round(genera_num*0.69)
        elif event <= 42:
            genera_num = round(genera_num*0.875)
        elif event <= 68:
            genera_num = round(genera_num*1.06)
        elif event <= 83:
            genera_num = round(genera_num*1.24)
        elif event <= 88:
            genera_num = round(genera_num*1.42)
        elif event <= 92:
            genera_num = round(genera_num*1.605)
        elif event <= 94:
            genera_num = round(genera_num*1.79)
        elif event <= 97:
            genera_num = round(genera_num*1.97)
        elif event <= 99:
            genera_num = round(genera_num*2.885)

        genera.extend([genera_num])
        
        
        if marker == 1:
            break

    plt.plot(MOY, genera, color='g')
    
class Main(object):
    def clear(self):
        plt.clf()
    def redraw(self):
        self.clear()
        big_boi()
        plt.xlabel('Millions of Years')
        plt.ylabel('Genera')
        plt.suptitle('Diversity over Time')
        plt.draw()
    def on_click(self,event):
        big_boi()    
        self.redraw()        
    def run(self):
        plt.figure()
        plt.connect('button_press_event', self.on_click)
        plt.show() 

m=Main()
m.run()
