#!/usr/bin/python3

#import re
#import sys
#
#tsv = open(sys.argv[1], 'r')
#fileContent =  tsv.read()
#appDesc = re.sub("""(?ism)(,|"|')""", r"\\\1", appDesc) # escape all especial charaters (" ' ,) rfc4180
#fileContent = re.sub("\t", ",", fileContent) # convert from tab to comma
#csv_file = open(sys.argv[2], "w")
#csv_file.write(fileContent)
#csv_file.close()

#import sys
#import csv
#
#tabin = csv.reader(sys.stdin, dialect=csv.excel_tab)
#commaout = csv.writer(sys.stdout, dialect=csv.excel)
#for row in tabin:
#  commaout.writerow(row)

import sys
import numpy as np
import re

def get_data_from_file(content):#filename):
    delimiter = '\t'
    data = np.genfromtxt(content, delimiter=delimiter)
    accelerations=data[:,2:5]
    return accelerations#np.array_str(accelerations)

def replace_delimiter(filename):

    content = ''
    with open(filename, mode='r', encoding='utf-8') as infile:
        content = infile.read()
    re.sub('\t', ',', content)
    with open(filename, mode='w', encoding='utf=8') as infile:
        infile.write(content)

    return content

def write_to_csv_file(tsvfilename, data):

    csvfile = get_csv_filename(tsvfilename)

    np.savetxt(csvfile, data, delimiter=',')
    #csv_file = open(csvfilename, 'w')
    #csv_file.write(data)
    return csvfile

def get_csv_filename(tsvfilename):
    csvfilename = tsvfilename[:-4] + '.csv'
    return csvfilename

def main():
    filename = sys.argv[1]
    print('filename: '+filename)

    data = get_data_from_file(filename)

    csv_file = write_to_csv_file(filename, data)

    #replace_delimiter(csv_file)

#    content = replace_delimiter(filename)
#    print('Replaced delimiter in tsvfile')
#    accelerations = get_data_from_file(content)
#    print('get acc from file')
#    write_to_file(filename)
#    print('write to cs file')
#

if __name__ == '__main__':
    main()
