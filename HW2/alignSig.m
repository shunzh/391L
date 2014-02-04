function [Y] = alignSig(X)
	Y = [];

	for i = 1:size(X,1)
		row = X(i,:);

		% normalize
		row = row - min(row);
		row = row / (max(row) - min(row));

		row = row + (i - 1);

		Y = [Y; row];
	end
end
