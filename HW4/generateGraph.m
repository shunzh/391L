% build a random graph
%
% Args:
% n = number of the nodes
% spar = sparcity of the graph
%
% Return:
% pa = parents of nodes
% cpts
function [pa, cpts] = generateGraph(n, spar)
	pa = cell(n, 1);

	% let this node be i
	for i = 1 : n
		% consider its possible parents
		for j = 1 : i - 1
			% determine whether add an edge here
			if rand() > spar
				pa{i} = [pa{i} j];
			end
		end
	end
	
	cpts = cell(n, 1);
	for i = 1 : n
		% it has 2^paNum values
		% corresponding to 1stParent * 2^0 + 2nd Parent * 2^1 + ..
		% each parent could be 0 or 1
		paNum = size(pa{i}, 2);
		cpts{i} = rand(1, 2^paNum);
	end
end
