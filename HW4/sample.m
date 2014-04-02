% Make a sample by looking up CPT
% 
% Args:
% cpt
% parents = assignment of the parents (0 or 1)
% 
% Return:
% s = sample
function [s] = sample(parents, cpt)
	if (length(parents) == 0)
		% when there is no parent
		% there is only one element in cpt then
		p = cpt(1);
	else
		% determine by looking up cpt
		% reverse it to get the binary representation
		bin = parents(end : -1 : 1);
		key = polyval(bin, 2);

		p = cpt(key + 1);
	end

	if rand() < p
		s = 1;
	else
		s = 0;
	end
end
