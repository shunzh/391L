% find the most likely class by assuming Gaussien distribution
function [classes] = maxLikelihood(testSet, trainSet, trainLabels, labelSet)
	classes = [];

    means = [];
	convs = [];

	for i = 1:size(labelSet)
		imgs = trainSet((trainLabels == i), :);
		means(:, i) = mean(imgs, 1)';
		covs(:, :, i) = cov(imgs); % each ROW taken as a datum for cov
	end

	for i = 1:size(testSet, 1)
		testData = testSet(i, :);

		probs = [];
		for l = 1:size(labelSet)
			probs = [probs, mvnpdf(testData', means(:, l), covs(:, :, l))];
		end

		[maxv, maxi] = max(probs);
		classes = [classes; labelSet(maxi)];
	end
end
