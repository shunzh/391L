% input X: m x t
function [W, diff] = ica(X, n, alpha, maxRun)
	[m t] = size(X);

	% W: n x m, initial guess
	W = rand(n, m) * .1;
	counter = 0;
	diff = [];

	while counter < maxRun
		% Y: n x t, estimate at this step
		Y = W * X;

		% Z: n x t
		Z = Y;
		for index = 1:numel(Z)
			Z(index) = sigmoid(Z(index));
		end

		% one step gradient descent
		detW = alpha * (eye(n) + (ones(n, t) - 2 * Z) * Y') * W;
		W = W + detW;

		counter = counter + 1;

		if mod(counter, 1000) == 0
			diff = [diff; norm(detW)];
			counter / maxRun
		end
	end
end
