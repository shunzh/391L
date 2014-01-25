% data and labels come in rows
function [classes] = knn(testSet, trainSet, trainLabels, k)
	classes = [];

	for i = 1:size(testSet, 1)
		testData = testSet(i, :);

        % get distance
		dist = trainSet - repmat(testData, size(trainSet, 1), 1);
		dist = sum(dist .^ 2, 2);
		[dist, order] = sort(dist, 'ascend');

        % find k-nearest labels
		nrstLabels = trainLabels(order);
		nrstLabels = nrstLabels(1:k);

		% choose the most frequent one
		ret = mode(double(nrstLabels));

		classes = [classes; ret];
	end
end
