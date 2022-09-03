import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import EngFormatter

#_______________________________________________________________________________________________________________
filename    = "results/1n4007-voltage-100khz"
Plot_Title   = "1N4007 Voltage Transient at 100 kHz for RRT"
x_axis_label = "t (ms)"
y_axis_label = "V (V)"
number_of_curves_in_plot = 1
LOG_OF_X = False
is_first_order_derivative = False
#_______________________________________________________________________________________________________________

x_axis_colum_number = 1
y_axis_column_start = 2

global readings
global x_readings
global y_readings

x_readings = []
y_readings = []

numbers =['0','1','2','3','4','5','6','7','8','9']

#This function read the file and returns the x and y axis values
def read_file(axis_index, filename):
    axis_readings = []
    readings_file = open(filename, "r")

    # read file line by line
    for x in readings_file:
        if x == "":
            #skip blank lines
            continue
        elif not(x[0] in numbers):
            # skip  lines which do not contain readings
            continue

        # remove new line character from each
        x = x.replace("\n", "")

        # seperate three numbers from line -> Index x_value y_value
        readings = [float(d) for d in x.split()]
        #print("readings-->",readings)
        try:
            axis_readings.append(readings[axis_index])
        except:
            print("________________________________________________________________________________________")
            print("***************Column number mismatch Error*************")
            print("Column number mismatch Error: Number of curves in the given output file are less than number_of_curves_in_plot")
            print("________________________________________________________________________________________")
            exit(0)

    return axis_readings

if __name__ == '__main__':
    #Read file and get x and y axis values in following two arrays
    diode_readings_x = read_file(x_axis_colum_number, filename)
    diode_readings_x = [i * 1000 for i in diode_readings_x]
    # print(diode_readings_x)

    diode_readings_y = read_file(y_axis_column_start, filename)
    # print(diode_readings_y)

    #Plot all graphs in single plot
    plt.plot(diode_readings_x , diode_readings_y, label = "Regular Diode")
    
    plt.title(Plot_Title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
