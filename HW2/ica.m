% input X: m x t
function [W] = ica(X, n, alpha, maxRun)
	[m t] = size(X);

	% W: n x m, initial guess
	W = rand(n, m);
	counter = 0;

	while counter < maxRun
		% Y: n x t, estimate at this step
		Y = W * X;

		% Z: n x t
		Z = cellfun(@sigmoid, num2cell(Y));

		% one step gradient descent
		W = W + alpha * (eye(n) + (ones(n, t) - 2 * Z) * Y') * W;

		counter = counter + 1;
	end
end
