% find the most likely class by assuming Gaussien distribution
function [classes] = maxLikelihood(testSet, trainSet, trainLabels, labelSet)
	classes = [];

	means = [];
	convs = [];

	for i = 1:size(labelSet)
		% number from 0 to 9
		imgs = trainSet((trainLabels == (i - 1)), :);
		means(:, i) = mean(imgs, 1)';
		covs(:, :, i) = cov(imgs);
	end

	covs

	for testData = testSet(:, :)'
		probs = [];
		for l = 1:size(labelSet)
			probs = [probs, mvnpdf(testData, means(:, l), covs(:, :, l))];
		end

		[maxv, maxi] = max(probs);
		classes = [classes; labelSet(maxi)];
	end
end
