#!/usr/bin/env python3
#
#  tar_backup.py - zips the folder passed as first argument in a unique tar file
#
#  Copyright (c) 2014 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os,sys,tarfile,time

def create_tgz(filename_suffix,folder_list,dest_folder='',compression='gz'):
    # Add suffix
    # Compression additions
    dest_ext = ''
    dest_cmp = ''
    if compression:
        dest_ext ='.' + compression
        dest_cmp = '|' + compression

    arcname = filename_suffix;  #XXX
    for folder in folder_list:
        if os.path.basename(folder) == '':
            folder = folder[:-1];   #Remove the trailing '/' #.replace('/','');
        arcname = os.path.basename(folder) + filename_suffix
        dest_name = '%s.tar%s' % (arcname, dest_ext)
        dest_path = os.path.join(dest_folder, dest_name)

        out = tarfile.TarFile.open(dest_path, 'w' +dest_cmp)

        print('Creating',dest_path);
        out.add(folder);    # out.add(folder_to_backup, arcname)
        out.close()
    return dest_path

def main(argv):
    folder_in = os.path.basename(os.path.realpath(os.path.curdir));  #XXX
    if len(argv) >= 2:
        folder_in = argv[1:];
    # Unique name as the current time
    unique_name = time.strftime("%Y%m%d%H%M");   ## "%d/%m/%Y"  ## dd/mm/yyyy format
    filename_suffix = unique_name
#     folder_dirs = [ name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name)) ]
#     if not folder_dirs:
    folder_list = folder_in;
    create_tgz(filename_suffix,folder_list);
    return;

if __name__ == '__main__':
    main(sys.argv);
