#!/usr/bin/env python3

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy import signal

def get_data_from_file(filename, delimiter=None):
    if not delimiter:
        delimiter = '\t'
    path_to_csv = filename
    data = np.genfromtxt(path_to_csv, delimiter=delimiter)
    print(str(len(data)) + ' values read in from csv.')
    print(data)
    return data

def get_acc_from_file(filename):
    ''' Returns acceleration values extracted from a 'typical' csv file'''
    data = get_data_from_file(filename)
    accelerations = data[:, 2:5]
    return accelerations

def convert_to_csv(filename):
    ''' Convert this data to csv
    '''
    data = get_data_from_file(filename)
    np.savetxt(filename[:-4]+'.csv', data, delimiter=',')

def crop_out_junk(data, output_file):
    print(data)
    print('Writing output to file: ', output_file)
    in1 = input('Enter lower bound: ')
    if in1 == '':
        lower = 0
        upper = len(data)
    elif ' ' in in1:
        (lower, upper) = in1.split(' ')
        lower = int(lower)
        upper = int(upper)
    else:
        lower = int(in1)
        upper = int(input('Enter upper bound: '))
    data = data[lower:upper, :]
    if (os.path.exists(output_file)):
        old_data = np.genfromtxt(output_file, dtype=float, delimiter=',')
        data = np.append(old_data, data, axis=0)
        #fhan = open(OUTPUT_FILE, 'a')
    np.savetxt(output_file, data, delimiter=',')

def plot_this_shi(accelerations):
    ''' Plot these accelerations
    '''
    plt.plot(accelerations)
    plt.ylabel('Acceleration')
    plt.xlabel('Serial data point')
    plt.show()

def do_magic_on_dir(dirname, output_file, iscsv=False):
    d = dirname
    file_list = [os.path.join(d,f) for f in os.listdir(d) if os.path.isfile(os.path.join(d,f))]
    #file_list = os.listdir(dirname)
    for filename in file_list:
        do_magic_on_file(filename, output_file);


def do_magic_on_file(filename, output_file, iscsv=False):
    print('Working on file: ', filename)
    if iscsv:
        data = get_data_from_file(filename, ',')
    else:
        data = get_data_from_file(filename, '\t')
    plot_this_shi(data[:, 2:5])
    convert_to_csv(filename)
    crop_out_junk(data, output_file)
    # TODO: Make a train file out of the magical data

def main():
    ''' Magic: Read tsv, convert to csv, plot, crop excess data
    '''

    # Parse command line arguments
    from argparse import ArgumentParser
    #usage = "%prog [-f credential_file]"
    #parser = ArgumentParser(usage=usage)
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, dest="filename",
                        required=True, help="Specify the input filename")
    parser.add_argument("-o", "--output", type=str, dest="output",
                        default='magical_output.csv',
                        help="Optionally specify the output filename")
    parser.add_argument("-c", "--csv", action='store_true', dest="csv",
                        help="Whether input is csv or tsv")
    #parser.add_argument('otherthings', nargs='*')
    #args, otherthings = parser.parse_known_args()
    #argc = len(otherthings)
    args = parser.parse_args()

    output_file = args.output
    filename = args.filename
    if os.path.isdir(filename):
        do_magic_on_dir(filename, output_file, args.csv)
    elif os.path.isfile(filename):
        do_magic_on_file(filename, output_file, args.csv)

if __name__ == '__main__':
    main()

