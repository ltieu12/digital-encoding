# Author: Lam Tieu
# BannerID: B00859543

import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

binaryString = input("Enter a binary string: ")

top = tk.Tk()
top.geometry("800x800")
top.title("Digital Encoding")

# create a figure to embed the waveform
# Reference: Embed charts in Tkinker GUI - https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
fig = Figure(figsize=(6, 6), dpi=100)

# Function to draw waveform of unipolar scheme
def unipolarWave(binstring):
    # initialize an array to store y-values of the wave
    y_values = []
    for bit in binstring:
        # if the bit in binary string is 1, the y-value is 5 (for 5V)
        if bit == '1':
            y_values.append(5)
        # if the bit in binary string is 0, the y-value is 0 (for 0V)
        elif bit == '0':
            y_values.append(0)
        # otherwise if binary string contains other number than 0 and 1, return error message
        else:
            print("Invalid binary string")
            return

    # create an array to store x-values, representing time of the encoding
    # the time equals to number of bits in the binary string, starting at 0
    # i.e. time 0 is for bit 0, time 1 is for bit 1, etc.
    # Reference: https://realpython.com/how-to-use-numpy-arange/
    x_values = np.arange(len(binstring))

    # adding the subplot on figure
    # Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html
    plt = fig.add_subplot(311, ylim=(0, 10))
    # using step() function to create waves with horizontal line to which the data points will be connected by vertical lines (not diagonal)
    # Reference: https://www.geeksforgeeks.org/matplotlib-pyplot-step-function-in-python/
    plt.step(x_values, y_values, where='post', label='Unipolar')
    plt.set_title("Unipolar Encoding")

# Function to draw waveform of NRZ scheme
def nrzWave(binstring):
    # initialize an array to store y-values of the wave
    y_values = []
    for bit in binstring:
        # if the bit in binary string is 1, the y-value is 5 (for 5V)
        if bit == '1':
            y_values.append(5)
        # if the bit in binary string is 0, the y-value is -5 (for -5V)
        elif bit == '0':
            y_values.append(-5)
        # otherwise if binary string contains other number than 0 and 1, return error message
        else:
            print("Invalid binary string")
            return
    # create an array to store x-values, representing time of the encoding
    x_values = np.arange(len(binstring))
    # adding the subplot on figure
    plt = fig.add_subplot(312, ylim=(-10, 10))
    # using step() function to create waves with horizontal line to which the data points will be connected by vertical lines (not diagonal)
    plt.step(x_values, y_values, where='post', label='NRZ')
    plt.set_title("NRZ Encoding")


# Function to draw waveform of Manchester scheme
def manchesterWave(binstring):
    # initialize an array to store y-values of the wave
    y_values = []
    for bit in binstring:
        # if the bit in binary string is 1, append 2 values -5 and 5, representing going from low to high
        if bit == '1':
            # using extend to add 2 values in to the array
            # Reference: https://www.w3schools.com/python/ref_list_extend.asp
            y_values.extend([-5, 5])
        # if the bit in binary string is 0, append 2 values 5 and -5, representing going from high to low
        elif bit == '0':
            y_values.extend([5, -5])
        # otherwise if binary string contains other number than 0 and 1, return error message
        else:
            print("Invalid binary string")
            return
    # create an array to store x-values, representing time of the encoding
    # because the length of y-values are longer (2 values for each bit), we need to divide the length by 2 to match with number of bits in binary string
    # step=0.5 to represent wave transition done at the middle of the interval
    x_values = np.arange(0, len(y_values) / 2, step=0.5)

    # adding the subplot on figure
    plt = fig.add_subplot(313, ylim=(-10, 10))
    # using step() function to create waves with horizontal line to which the data points will be connected by vertical lines (not diagonal)
    # using pre because the patter (low to high & high to low) starts on the left of the interval
    plt.step(x_values, y_values, where='pre', label='NRZ')
    plt.set_title("Manchester Encoding")


# call each function to create waveforms
unipolarWave(binaryString)
nrzWave(binaryString)
manchesterWave(binaryString)


fig.tight_layout()
# create Tkinker canvas to contain figure
# Reference: https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
canvas = FigureCanvasTkAgg(fig, master=top)
canvas.draw()
canvas.get_tk_widget().pack(side='left', fill='both', expand=1)

top.mainloop()