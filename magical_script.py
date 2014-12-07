#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
from argparse import ArgumentParser

def get_data_from_file(filename, delimiter=None):
    if not delimiter:
        delimiter = '\t'
    path_to_csv = filename
    data = np.genfromtxt(path_to_csv, delimiter=delimiter)
    print(str(len(data)) + ' values read in from csv.')
    return data

def get_acc_from_file(filename):
    ''' Returns acceleration values extracted from a 'typical' csv file'''
    data = get_data_from_file(filename)
    accelerations = data[:, 2:5]
    return accelerations

def convert_to_csv(filename, data=None):
    ''' Convert this data to csv
    '''
    if data == None:
        out_filename = filename[:-4]+'.csv'
    else:
        data = get_data_from_file(filename)
        out_filename = filename[:-4]+'_cropped.csv'
    np.savetxt(out_filename, data, delimiter=',')

def crop_out_junk(data, output_file):
    plot_this_shi(data[:, 2:5])
    in1 = input('Enter bounds <lb ub>: ')
    if in1 == '':   #Press nothing
        lower = 0
        upper = len(data)
    elif ' ' in in1:    #Press both in one line
        (lower, upper) = in1.split(' ')
        lower = int(lower)
        upper = int(upper)
    else:
        lower = int(in1)
        upper = int(input('Enter upper bound: '))
    return (lower, upper)

def append_output(data, output_file, nocrop=False):
    print('Writing output to file: ', output_file)
    if nocrop == False:
        (lower, upper) = crop_out_junk(data, output_file)
    else:
        (lower, upper) = (0, len(data))
    cropped_data = data[lower:upper, :]
    full_data = cropped_data
    if (os.path.exists(output_file)):
        old_data = np.genfromtxt(output_file, delimiter=',')
        full_data = np.append(old_data, full_data, axis=0)
    np.savetxt(output_file, full_data, delimiter=',')
    return cropped_data

def plot_this_shi(accelerations):
    ''' Plot these accelerations
    '''
    plt.plot(accelerations)
    plt.ylabel('Acceleration')
    plt.xlabel('Serial data point')
    plt.show()

def do_magic_on_dir(dirname, output_file, iscsv=False, nocrop=False):
    d = dirname
    file_list = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
    file_list = [f for f in file_list if f[-4:] == '.tsv']
    print('TSV files:\n', file_list)
    #file_list = os.listdir(dirname)
    for filename in file_list:
        do_magic_on_file(filename, output_file, iscsv=iscsv, nocrop=nocrop);


def do_magic_on_file(filename, output_file, iscsv=False, nocrop=False):
    print('Working on file: ', filename)
    if iscsv:
        data = get_data_from_file(filename, ',')
    else:
        data = get_data_from_file(filename, '\t')
    append_output(data, output_file, nocrop=nocrop)
        #cropped_data = crop_out_junk(data, output_file)
        #convert_to_csv(filename, cropped_data)
    # OODO: Make a train file out of the magical data

def main():
    ''' Magic: Read tsv, convert to csv, plot, crop excess data
    '''
    output_filename = 'output_' + time.strftime("%Y%m%d.%H%M") + '.csv'

    # Parse command line arguments
    #usage = "%prog [-f credential_file]"
    #parser = ArgumentParser(usage=usage)
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, dest="filename",
                        required=True, help="Specify the input filename")
    parser.add_argument("-o", "--output", type=str, dest="output",
                        default=output_filename,
                        help="Optionally specify the output filename")
    parser.add_argument("-n", "--no-crop", action='store_true', dest="nocrop",
                        help="To not to crop the input files")
    parser.add_argument("-c", "--csv", action='store_true', dest="csv",
                        help="Whether input is csv or tsv")
    #parser.add_argument('otherthings', nargs='*')
    #args, otherthings = parser.parse_known_args()
    #argc = len(otherthings)
    args = parser.parse_args()

    output_file = args.output
    filename = args.filename
    if os.path.isdir(filename):
        do_magic_on_dir(filename, output_file, iscsv=args.csv,
                nocrop=args.nocrop)
    elif os.path.isfile(filename):
        do_magic_on_file(filename, output_file, iscsv=args.csv,
                nocrop=args.nocrop)

if __name__ == '__main__':
    main()

