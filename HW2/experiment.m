function [W, A, diff] = experiment()
	load sounds.mat;

	A = rand(5, 5);

	U = sounds;
	X = A * U;
	n = 5;
	maxRun = 200;
	alpha = 0.00001;

	[W, diff] = ica(X, n, alpha, maxRun);
end
