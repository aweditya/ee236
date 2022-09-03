import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename    = "results/rn142-iv"
Plot_Title   = "RN142 log(I) vs V Characteristic"
x_axis_label = "Voltage (V)"
y_axis_label = "Current (I)"
number_of_curves_in_plot = 1
is_first_order_derivative = False
#_______________________________________________________________________________________________________________

x_axis_colum_number = 3
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

    diode_readings_y = []
    for column in range(y_axis_column_start, number_of_curves_in_plot + y_axis_column_start):
        diode_readings_y.append(read_file(column, filename))

    #Plot all graphs in single plot
    for column in range(0, number_of_curves_in_plot):
        plt.plot(diode_readings_x , diode_readings_y[column])

    plt.title(Plot_Title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
