function features(filename, windowsize, output_filename)

	data = csvread(filename);
	X = data(:,3);
	Y = data(:,4);
	Z = data(:,5);
	idx = data(:,6);

	abs_acc = ((X.^2).+(Y.^2).+(Z.^2)).^(1/2);
	windowStart = 1;

	% Initialize

	featureVectors =[];
	while (windowStart+windowsize-1 <= length(X))   %The end of this window must exist
		energyWin = [];
		dcComp = [];
		out = [];

		nextWindow = windowStart + windowsize;
		block = abs_acc(windowStart:nextWindow - 1);     %nextWindow is currentWindowEnd + 1
		idxBlock = round(mean(idx(windowStart:nextWindow - 1)));

		out = abs(fft([block]));
		dcComp = [dcComp; out(1)];

	% dc Component is not to be included in calculations
		energyWin = [energyWin; sum( (out(2:size(out),1).^2) ) /  (windowsize-1)];
		windowStart = nextWindow;

		featureVectors = [featureVectors; idxBlock, mean(block),std(block), dcComp, energyWin];		%In fft, first component is mean of rest of the values

	end
featureVectors
%featureVectors = [featureVectors, features_yz, entropy, dcComp, energyWin];  %In fft, first component is mean of rest of the values
csvwrite(output_filename, featureVectors);
end


