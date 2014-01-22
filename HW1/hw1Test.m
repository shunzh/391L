% load from file
load digits.mat;

N = 5000;
M = 3;

% unroll each data, save in matrix X
A = [];
for i = 1 : N
    img = trainImages(:,:,1,i);
    A = [A, img(:)];
end

[m, V] = hw1FindEigendigits(A);

% use only first few eigenvecs
V_ = V(:, 1:M);
invV_ = inv(V_' * V_) * V_';

% try reconstruct original figures
map = [];
for i = 1 : 1000
	% changed to training set!!
    I = trainImages(:,:,1,i);
    I = double(I(:)) - m;
    
    W = invV_ * I;
    %O = V_ * W;

    map = [map; double(trainLabels(1, i)), W'];
    
    %I = reshape(I, 28, 28);
    %O = reshape(O, 28, 28);
    %imwrite(I, ['testIn', int2str(i), '.png']);
    %imwrite(O, ['testOut', int2str(K), '_', int2str(i), '.png']);
end

for i = 0 : 9
	mapi = map(map(:,1) == i, :);
	if i > 5
	    scatter(mapi(:, 2), mapi(:, 3), 'x');
	else
	    scatter(mapi(:, 2), mapi(:, 3));
	end

	hold on;
end
