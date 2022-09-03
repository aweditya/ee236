import matplotlib.pyplot as plt
import numpy as np

filename     = "results/voltage-bat85"

x_axis_column_number = 1
y_axis_column_start = 2

global readings
global x_readings
global y_readings

x_readings = []
y_readings = []

numbers =['0','1','2','3','4','5','6','7','8','9']

#This function read the file and returns the x and y axis values
def read_file(axis_index):
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
    diode_readings_x = read_file(x_axis_column_number)

    diode_readings_y = []
    for column in range(y_axis_column_start, 2 + y_axis_column_start):
        diode_readings_y.append(read_file(column))

    print(len(diode_readings_x))
    print(len(diode_readings_y[0]))

    plt.plot(diode_readings_x, diode_readings_y[0], label=r"$V_{in}$")
    plt.plot(diode_readings_x, diode_readings_y[1], label=r"$V_{out}$")
    plt.title("Transient Characteristics for Bridge Rectifier using BAT85")
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (V)")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig("plots/transient-bat85.png")
    plt.show()

    plt.plot(diode_readings_y[0], diode_readings_y[1])
    plt.title("Transfer Characteristics for Bridge Rectifier using BAT85")
    plt.xlabel(r"$V_{in}$")
    plt.ylabel(r"$V_{out}$")
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.savefig("plots/transfer-characteristics-bat85.png")
    plt.show()

