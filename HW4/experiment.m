function [p] = experiment(pa, cpts, qmask, q, emask, e, m, t)
	results = []

	for i = 20 : 20 : 500
		pg = gibbsSample(pa, cpts, qmask, q, emask, e, m, t);
		pr = rejectionSample(pa, cpts, qmask, q, emask, e, m);

		results = [results; pg, pr];
	end
end
