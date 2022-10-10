import matplotlib.pyplot as plt
import numpy as np

#_______________________________________________________________________________________________________________
filenames    = ["results/iv-10-35", "results/iv-10-45", "results/iv-10-55", "results/iv-10-65", "results/iv-10-75"]
Plot_Title   = "Light I/V Characteristics (10mA)"
x_axis_label = "Voltage (V)"
y_axis_label = "Current (I)"
number_of_curves_in_plot = 1
LOG_OF_X = False
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
    readings_35_x = read_file(x_axis_colum_number, filenames[0])
    readings_45_x = read_file(x_axis_colum_number, filenames[1])
    readings_55_x = read_file(x_axis_colum_number, filenames[2])
    readings_65_x = read_file(x_axis_colum_number, filenames[3])
    readings_75_x = read_file(x_axis_colum_number, filenames[4])

    readings_35_y = []
    readings_45_y = []
    readings_55_y = []
    readings_65_y = []
    readings_75_y = []
    for column in range(y_axis_column_start, number_of_curves_in_plot + y_axis_column_start):
        readings_35_y.append(read_file(column, filenames[0]))
        readings_45_y.append(read_file(column, filenames[1]))
        readings_55_y.append(read_file(column, filenames[2]))
        readings_65_y.append(read_file(column, filenames[3]))
        readings_75_y.append(read_file(column, filenames[4]))

    #Plot all graphs in single plot
    for column in range(0, number_of_curves_in_plot):
        plt.plot(readings_35_x , readings_35_y[column], label = r"$35^{\circ}$C")
        plt.plot(readings_45_x , readings_45_y[column], label = r"$45^{\circ}$C")
        plt.plot(readings_55_x , readings_55_y[column], label = r"$55^{\circ}$C")
        plt.plot(readings_65_x , readings_65_y[column], label = r"$65^{\circ}$C")
        plt.plot(readings_75_x , readings_75_y[column], label = r"$75^{\circ}$C")
    
    plt.title(Plot_Title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig("plots/light-iv-temp.png")
    plt.show()

    for column in range(0, number_of_curves_in_plot):
        plt.plot(readings_35_x , -np.array(readings_35_y[column]) * np.array(readings_35_x), label = r"$35^{\circ}$C")
        plt.plot(readings_45_x , -np.array(readings_45_y[column]) * np.array(readings_45_x), label = r"$45^{\circ}$C")
        plt.plot(readings_55_x , -np.array(readings_55_y[column]) * np.array(readings_55_x), label = r"$55^{\circ}$C")
        plt.plot(readings_65_x , -np.array(readings_65_y[column]) * np.array(readings_65_x), label = r"$65^{\circ}$C")
        plt.plot(readings_75_x , -np.array(readings_75_y[column]) * np.array(readings_75_x), label = r"$75^{\circ}$C")

    plt.title("Power Plot under Light Condition (10mA)")
    plt.xlabel(x_axis_label)
    plt.ylabel(r"Power ($V \times I$)")

    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.savefig("plots/light-iv-temp-power.png")
    plt.show()

    voc_35 = 4.183931e-01
    isc_35 = 9.881474e-03
    power_35 = np.array(readings_35_x) * np.array(readings_35_y[0])
    vmp_35 = readings_35_x[np.argmax(power_35)]
    imp_35 = readings_35_y[0][np.argmax(power_35)]
    print("FF at 35C:", (voc_35 * isc_35)/(vmp_35 * imp_35))

    voc_45 = 3.934860e-01
    isc_45 = 9.864292e-03
    power_45 = np.array(readings_45_x) * np.array(readings_45_y[0])
    vmp_45 = readings_45_x[np.argmax(power_45)]
    imp_45 = readings_45_y[0][np.argmax(power_45)]
    print("FF at 45C:", (voc_45 * isc_45)/(vmp_45 * imp_45))

    voc_55 = 3.685265e-01
    isc_55 = 9.834726e-03
    power_55 = np.array(readings_55_x) * np.array(readings_55_y[0])
    vmp_55 = readings_55_x[np.argmax(power_55)]
    imp_55 = readings_55_y[0][np.argmax(power_55)]
    print("FF at 55C:", (voc_55 * isc_55)/(vmp_55 * imp_55))

    voc_65 = 3.435322e-01
    isc_65 = 9.785861e-03
    power_65 = np.array(readings_65_x) * np.array(readings_65_y[0])
    vmp_65 = readings_65_x[np.argmax(power_65)]
    imp_65 = readings_65_y[0][np.argmax(power_65)]
    print("FF at 65C:", (voc_65 * isc_65)/(vmp_65 * imp_65))

    voc_75 = 3.185299e-01
    isc_75 = 9.708296e-03
    power_75 = np.array(readings_75_x) * np.array(readings_75_y[0])
    vmp_75 = readings_75_x[np.argmax(power_75)]
    imp_75 = readings_75_y[0][np.argmax(power_75)]
    print("FF at 75C:", (voc_75 * isc_75)/(vmp_75 * imp_75))
