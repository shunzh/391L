function [p] = experiment(pa, cpts, qmask, q, emask, e, name)
	results = [];
	maxIter = 1000;

	iterations = 200 : 200 : maxIter;

	for i = iterations
		pg = gibbsSample(pa, cpts, qmask, q, emask, e, i, 200);
		pr = rejectionSample(pa, cpts, qmask, q, emask, e, i);

		results = [results; [pg, pr]];
	end

	results

	plot(iterations, results);
	legend("Gibbs Sampling", "Rejection Sampling");
	xlabel("Iterations");
	ylabel("Probability");
	axis([0 maxIter 0 1]);

	print([name, '.png'], '-S600,500');
end

% experiment(pa, cpts, qmask(1,:), q(1,:), emask(1,:), e(1,:), "ian1")
