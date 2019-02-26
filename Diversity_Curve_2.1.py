import matplotlib.pyplot as plt
import math
import random
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
import scipy.stats

'''This program uses extinction and origination formulas as described by Foote
in his paleobiology paper from 2000

M. Foote. Origination and Extinction Components of Taxonomic Diversity: General Problems. Paleobiology, Vol. 26(4). 2000. pp. 74-102. http://www.jstor.org/stable/1571654'''

'''Data for this program was obtained from the PBDB'''


def big_boi():
    MOY_num = 0
    MOY = [MOY_num]

    start_genera = 324

    genera = [start_genera]
    genera_num = start_genera

    X_bt = genera_num

    value = 1.1
    value_2 = 1.1
    
    def origination_rate(S,N):#S stands for survivors (X_bt), N stands for newbies (X_Ft)
        origination_rate_equation = -math.log((S/(S + N))/(5.6))#the 5.6 comes from the length of time, i.e. 5.6 million years per age

        return origination_rate_equation
        
    def extinction_rate(S,D):#D stands for those that died (X_bL)
        extinction_rate_equation = -math.log((S/(S + D))/(5.6))

        return extinction_rate_equation

    def SR_D(value):#SR_D stands for special rate for death rate
        special = value/(value**2)

        return special

    def SR_O(value_2):#SR stands for special rate for origination rate
        special_2 = value_2/(value_2**2)

        return special_2

    for i in range (97):#97 makes it about 540 million years

        event_2 = random.uniform(0,94)

        MOY_num += 5.6
        MOY.extend([MOY_num])

        X_bL = random.choices([random.randint(0,41), random.randint(41,81), random.randint(81,122), random.randint(122,162), random.randint(162,203),random.randint(203,243),random.randint(243,284),random.randint(284,324),random.randint(324,365),random.randint(365,406),random.randint(406,446),random.randint(446,487),random.randint(487,527),random.randint(527,568),random.randint(608,649),random.randint(649,689),random.randint(689,730),random.randint(770,811)], [11,SR_D(value)*11,SR_D(value)*9,SR_D(value)*14,SR_D(value)*10,SR_D(value)*10,SR_D(value)*3,SR_D(value)*2,SR_D(value)*4,SR_D(value)*6,SR_D(value)*1,SR_D(value)*4,SR_D(value)*1,SR_D(value)*2,SR_D(value)*3,SR_D(value)*1,SR_D(value)*1,SR_D(value)*1])
        X_bL = np.array(X_bL)
        #Number of distinct taxa whos last known appearence occur in this age
        
        #X_Ft = (0.572 * X_bL + 124.8) * (random.randrange(14,350)*0.01)
        X_Ft = random.choices([random.randint(0,51), random.randint(51,103), random.randint(103,154), random.randint(154,205), random.randint(205,257), random.randint(257,308), random.randint(308,359), random.randint(359,411), random.randint(411, 462), random.randint(462,514), random.randint(514,565), random.randint(565,616), random.randint(616,668), random.randint(719,770), random.randint(822,873), random.randint(976,1027)], [6, SR_O(value_2)*10, SR_O(value_2)*15, SR_O(value_2)*12, SR_O(value_2)*12, SR_O(value_2)*13, SR_O(value_2)*4, SR_O(value_2)*5, SR_O(value_2)*5, SR_O(value_2)*4, SR_O(value_2)*2, SR_O(value_2)*1, SR_O(value_2)*1, SR_O(value_2)*1, SR_O(value_2)*2, SR_O(value_2)*1])

        X_Ft = np.around(X_Ft)
        #Number of distinct taxa that first known appearence occur in this age

        #X_bt = X_bt - X_bL + X_Ft
        #X_bt = np.around(X_bt)

        X_bt = (2.905 * X_bL + 1037.614) * (random.randrange(8,290)*0.01)
        
        #Number of distinct taxa who lived through both boundaries of this age

        origination_rate_equation_result = origination_rate(X_bt, X_Ft)

        extinction_rate_equation_result = extinction_rate(X_bt,X_bL)

        combined_rate = (origination_rate_equation_result - extinction_rate_equation_result + 1)
        #combined_rate =  0.4

        if combined_rate <= 0.6:
            plt.axvline(x = MOY_num, color='purple')
        elif combined_rate <= 0.8:
            plt.axvline(x = MOY_num, color='r')

        genera_num = round(genera_num * combined_rate)

        if genera_num <= 1:
           genera_num = 0
           plt.title("Complex life went extinct after "+str(round(MOY_num))+" million years.", color='red', fontsize=13)
           genera.extend([0])
           break
        genera.extend([genera_num])

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

   
big_boi()
