% build a random graph
%
% Args:
% n = number of the nodes
% spar = sparcity
%
% Return:
% pa = parents of nodes
% cpt
function [pa, cpt] = generateGraph(n, spar)
	pa = cell(n, 1);

	% let this node be i
	for i = 1 : n
		% consider its possible parents
		for j = 1 : i - 1
			% determine whether add an edge here
			if rand() > spar
				pa{i} = [pa{i} j];
			end
	
	cpt = cell(n, 1);
	for i = 1 : n
		% it has 2^paNum values
		paNum = size(pa{i}, 2);

end
