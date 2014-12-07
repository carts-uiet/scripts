Scripts used for CARTS UIET project so far
------------------------------------------

* Convert file from TSV to CSV format  
  Expected File Format: Anything  
  ```bash
      $ ./magical_script.py -f inputfile.tsv -o output.csv
  ```
  You can do the following for a folder  
  ```bash
      $ ./magical_script.py -f folder/ -o output.csv
  ```
  If you don't want to crop any files you may add  
  ```bash
      $ ./magical_script.py -f FILE/FOLDER -n
  ```


* Make feature file using windows from .train file  
  Expected file format: csv with columns [-, -, ax, ay, az, idx, -...]  
  Using octave  
  ```matlab
      octave:1> features(filename, windowsize, output_filename)
  ```

* Convert it to libsvm .train file format using octave/MATLAB  
  Format: Any csv file  
  ```matlab
      octave:1> csvToSVMLibFormat(filename)
  ```

* Final asset  
  Append this new filename_libsvm.train to old train file using  
  ```bash
  $ cat old_train_file.train new_libsvm.train > new_train_file.train
  ```

#### Other tasks that these scripts can do

* Plot a tsv file  
  ```bash
      $ ./magical_script.py -f inputfile.tsv -p
  ```

