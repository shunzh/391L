% input X: m x t
function [W] = ica(X, n, alpha, maxRun)
	[m t] = size(X);

	% W: n x m, initial guess
	W = rand(n, m) * .1;
	counter = 0;

	while counter < maxRun
		% Y: n x t, estimate at this step
		Y = W * X;

		% Z: n x t
		Z = Y;
		for index = 1:numel(Z)
			Z(index) = sigmoid(Z(index));
		end

		% one step gradient descent
		W = W + alpha * (eye(n) + (ones(n, t) - 2 * Z) * Y') * W;

		counter = counter + 1;

		if mod(counter, 5000) == 0
			counter / maxRun
		end
	end
end
