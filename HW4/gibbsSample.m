% Gibbs sampling
% 
% Args:
% pa, cpts
% qmask = mask that indicate which are query
% q = a vector indicate the query value
% emask = mask that indicate which are evidence
% e = a vector of evidence
% m = number of iterations
% t = burnin iterations
function [p] = gibbsSample(pa, cpts, qmask, q, emask, e, m, t)
	% there shouldn't be overlap on query and evidence
	assert (any(qmask == emask) == 0);
	assert (m > 0);

	n = size(pa, 2);

	samples = [];
	s = e; % initialize with e fixed and others being 0

	ne = (1 : n)(emask == 0); % nonevidence

	% # of iterations
	for i = 1 : t + m
		% resample each non-evidence variable
		for j = ne
			s(j) = 1; j_pos = gibbsSampleHelper(pa, cpts, s);
			s(j) = 0; j_neg = gibbsSampleHelper(pa, cpts, s);
			j_p = j_pos / (j_pos + j_neg);
			s(j) = rand() < j_p;
		end

		if i > t
			samples = [samples; s];
		end
	end

	pos_m = 0; % number of samples that match the query
	for i = 1 : m
		query = samples(i, :) & qmask;
		if isequal(q, query)
			pos_m += 1;
		end
	end

	p = pos_m / m;
end
