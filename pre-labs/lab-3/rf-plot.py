import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filename    = "results/rn142-rf--5"
x_axis_label = "t (us)"
number_of_curves_in_plot = 2
#_______________________________________________________________________________________________________________

x_axis_colum_number = 1
y_axis_column_start = 2

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
    diode_readings_t = read_file(x_axis_colum_number, filename)
    diode_readings_t = [i * 1e6 for i in diode_readings_t]

    diode_readings_v_in = read_file(y_axis_column_start, filename)
    diode_readings_v_out = read_file(y_axis_column_start + 1, filename)

    #Plot all graphs in single plot
    plt.plot(diode_readings_t, diode_readings_v_in, label = r"$V_{in}$")
    plt.plot(diode_readings_t, diode_readings_v_out, label = r"$V_{out}$")
    
    plt.title("RN142 Voltage Transient for DC Bias = -5V")
    plt.xlabel(x_axis_label)
    plt.ylabel("Voltage (V)")
    plt.legend()
    
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()

    diode_readings_i = read_file(y_axis_column_start + 2, filename)
    diode_readings_i = [i * 1e3 for i in diode_readings_i]
    plt.plot(diode_readings_t, diode_readings_i)

    plt.title("RN142 Current Transient for DC Bias = -5V")
    plt.xlabel(x_axis_label)
    plt.ylabel("I (mA)")

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()
