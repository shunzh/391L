function [ret] = H(b)
	% classes of b
	X = unique(b);

	ret = 0;
	for x = X'
		p = sum(b == x) / size(b, 1);
		if p ~= 0
			ret = ret - p * log2(p);
		end
	end
end
