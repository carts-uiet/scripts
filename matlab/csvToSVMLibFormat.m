%Converts csv file to the format as required by svmtrain used by libsvm
function csvToSVMLibFormat(source_file)

data_read = csvread(source_file);
labels = data_read(:,1);
features = data_read(: ,2:end);
features_sparse = sparse(features);

%Removing file extension
[directory,filename_without_extension]=fileparts(source_file); % test_file(1:size(test_file,2)-4);
%filename = strcat(directory,'/',filename_without_extension, '_expert.train')
filename = strcat(filename_without_extension, '_libsvm.train')

libsvmwrite(filename, labels, features_sparse)

end
