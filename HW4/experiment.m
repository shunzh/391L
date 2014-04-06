function [p] = experiment(pa, cpts, qmask, q, emask, e)
	results = []

	iterations = 50 : 50 : 500;

	for i = iterations
		pg = gibbsSample(pa, cpts, qmask, q, emask, e, i, 200);
		pr = rejectionSample(pa, cpts, qmask, q, emask, e, i);

		results = [results; [pg, pr]];
	end

	plot(iterations, results);
	legend("Gibbs Sampling", "Rejection Sampling");
	xlabel("Iterations");
	ylabel("Probability (answer returned)");
end
