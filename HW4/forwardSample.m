% Forward sampling
function [s] = forwardSample(pa, cpts)
	n = size(pa, 2);
	s = [];

	for i = 1 : n
		parents = s(pa{i});
		p = cptLookUp(parents, cpts{i});
		s(i) = rand() < p;
	end
end
