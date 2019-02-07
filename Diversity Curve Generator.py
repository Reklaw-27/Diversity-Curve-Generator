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
        event = random.randint(1,93)

        if genera_num == 0:
            genera_num = 0
        elif genera_num < 1.1:
            genera_num = 0
            plt.title("Complex life went extinct after "+str(round(MOY_num))+" million years.", color='red', fontsize=13)
            marker = 1
        elif genera_num > 100000:
            genera_num = genera_num*0.875


        elif event <= 1:
            genera_num = round(genera_num*random.uniform(0.563, 0.648))
            plt.axvline(x = MOY_num, color='purple')
        elif event <= 3:
            genera_num = round(genera_num*random.uniform(0.648, 0.734))
            #if event == 2:
            plt.axvline(x = MOY_num, color='r')
        elif event <= 5:
            genera_num = round(genera_num*random.uniform(0.734, 0.819))
        elif event <= 13:
            genera_num = round(genera_num*random.uniform(0.819, 0.904))
        elif event <= 23:
            genera_num = round(genera_num*random.uniform(0.904, 0.989))
        elif event <= 70:
            genera_num = round(genera_num*random.uniform(0.989, 1.074))
        elif event <= 84:
            genera_num = round(genera_num*random.uniform(1.074, 1.159))
        elif event <= 89:
            genera_num = round(genera_num*random.uniform(1.159, 1.245))
        elif event <= 91:
            genera_num = round(genera_num*random.uniform(1.245, 1.330))
        elif event <= 92:
            genera_num = round(genera_num*random.uniform(1.585, 1.670))
        elif event <= 93:
            genera_num = round(genera_num*random.uniform(2.181, 2.267))
            
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
