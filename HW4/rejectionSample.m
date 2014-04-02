% Rejection sampling
% 
% Args:
% pa, cpts
% qmask = mask that indicate which are query
% q = a vector indicate the query value
% emask = mask that indicate which are evidence
% e = a vector of evidence
% m = number of iterations
function [p] = rejectionSample(pa, cpts, qmask, q, emask, e, m)
	% there shouldn't be overlap on query and evidence
	assert (any(qmask == emask) == 0);

	samples = [];

	for i = 1 : m
		s = forwardSample(pa, cpts);

		% if this sample is consistant with the evidence, add to samples
		evidence = s & emask;
		if isequal(e, evidence)
			samples = [samples; s];
		end
	end

	samples

	acc_m = size(samples, 1);

	assert (acc_m != 0); % This is possible.

	pos_m = 0; % number of samples that match the query
	for i = 1 : acc_m
		query = samples(i, :) & qmask;
		if isequal(q, query)
			pos_m += 1;
		end
	end

	p = pos_m / acc_m;
end
