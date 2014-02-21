% input X: m x t
function [W, diff] = icang(X, n, alpha, maxRun)
	[m t] = size(X);

	% W: n x m, initial guess
	W = rand(n, m) * .1;
	counter = 0;
	diff = [];

	while counter < maxRun
		for x = X(:,:)
			% Y: n x 1, estimate at this step
			y = W * x;

			% Z: n x 1
			z = y;
			for index = 1:numel(z)
				z(index) = sigmoid(z(index));
			end

			% one step gradient descent
			detW = alpha * ((ones(n, 1) - 2 * z) * x' + inv(W'));
			W = W + detW;

			diff(end)
		end
		
		counter = counter + 1;

		diff = [diff; norm(detW)];
		counter / maxRun
	end
end
