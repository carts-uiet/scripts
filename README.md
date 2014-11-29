# Convert file from TSV to CSV format
# Expected File Format: Anything
$ ./magical_script.py -f inputfile.tsv -o output.csv


# Make feature file using windows from .train file
# Expected file format: csv with columns [-, -, ax, ay, az, idx, -...]
#Using octave 
octave:1> features(filename, windowsize, output_filename)

# Convert it to libsvm .train file format using octave/MATLAB
# Format: Any csv file
octave:1> csvToSVMLibFormat(filename)

# Final asset
Append this new filename_libsvm.train to old train file using
$ cat old_train_file.train new_libsvm.train > new_train_file.train
