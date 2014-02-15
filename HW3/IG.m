% data A, on attribute #i, with output b
function [ret] = IG(A, b, i)
	X = unique(A(:,i));
	
	ret = H(b);

	% for each possible value of attribute #i
	for x = X'
		idx = A(:,i) == x;
		bi = b(idx);
		pi = sum(A(:,i) == x) / size(b, 1);

		ret = ret - pi * H(bi);
	end
end
