function [p] = gibbsSampleHelper(pa, cpts, s)
	p = 1;
	n = size(pa, 2);

	for i = 1 : n
		p = p * cptLookUp(s(pa{i}), cpts{i});
	end
end
