function [p] = gibbsSampleHelper(pa, cpts, s)
	p = 1;
	n = size(pa, 2);

	for i = 1 : n
		pi = cptLookUp(s(pa{i}), cpts{i});
		if s(i) == 0
			pi = 1 - pi;
		end
		p = p * pi;
	end
end
