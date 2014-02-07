function [W, A, diff] = experiment()
	load sounds.mat;

	A = rand(5, 5);

	U = sounds;
	X = A * U;
	n = 5;
	maxRun = 20;
	alpha = 0.00001;

	%[W, diff] = icang(X, n, alpha, maxRun);
	[W, diff] = ica(X, n, alpha, maxRun);
end
