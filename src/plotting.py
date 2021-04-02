#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import sys

# Create a function to read the data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename. 
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=5)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(all_data[starting_row:,:], dtype=float)
    return temperature_data

def process_data(temperature_data):
    # Compute a new column by multiplying column number 1 to Kelvin
    temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

    # Append this new column to the existing temperature_data array
    processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
    return processed_temperature_data

def plot_data(processed_temperature_data, plot_filename):
    # Create a figure of the processed data
    temperature_figure = plt.figure()
    temperature_plot = plt.bar (processed_temperature_data[:,0],processed_temperature_data[:,2], width=35, color='blue')

    plt.show(block=True)
    temperature_figure.savefig(plot_filename)


def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json(output_filename)

def plot():
    input_file = "110-tavg-12-12-1950-2020.csv"
    plot_file = "temperature-over-time.pdf"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    

    input_filename = os.path.join(data_directory, input_file)
    plot_filename = os.path.join(data_directory, plot_file)
    json_output_file = os.path.join(data_directory, json_output_file)

    temperature_data = read_data(input_filename, starting_row=5)
    processed_temperature_data = process_data(temperature_data)
    plot_data(processed_temperature_data, plot_filename)
    convert_data(input_filename, json_output_file)

if __name__ == "__main__":
    print(sys.argv)
    plot()