import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons

def big_boi():
    MOY = [0]
    MOY_num = 0
    year = 0
    species = [324]
    species_num = 324

    marker = 0

    for i in range (100):        
        MOY_num += 5.4
        MOY.extend([MOY_num])
        year += 5.4
        event = random.randint(1,99)

        if species_num == 0:
            species_num = 0
        elif species_num < 1.1:
            species_num = 0
            plt.title("Complex life went extinct after "+str(round(year))+" million years.", color='red', fontsize=13)
            marker = 1
        elif species_num > 100000:
            species_num = species_num*0.875
            
        elif event <= 7:
            species_num = round(species_num*0.51)
            if event == 1:
                plt.axvline(x = MOY_num, color='r')
            elif event == 2:
                plt.axvline(x = MOY_num, color='purple')
        elif event <= 18:
            species_num = round(species_num*0.69)
        elif event <= 42:
            species_num = round(species_num*0.875)
        elif event <= 68:
            species_num = round(species_num*1.06)
        elif event <= 83:
            species_num = round(species_num*1.24)
        elif event <= 88:
            species_num = round(species_num*1.42)
        elif event <= 92:
            species_num = round(species_num*1.605)
        elif event <= 94:
            species_num = round(species_num*1.79)
        elif event <= 97:
            species_num = round(species_num*1.97)
        elif event <= 99:
            species_num = round(species_num*2.885)

        species.extend([species_num])
        
        
        if marker == 1:
            break

    plt.plot(MOY, species, color='g')
    
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
