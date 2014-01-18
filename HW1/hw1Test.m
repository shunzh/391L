% load from file
load digits.mat;

N = 2000;
K = 200;

% unroll each data, save in matrix X
A = [];
for i = 1 : N
    img = trainImages(:,:,1,i);
    A = [A, img(:)];
end

[m, V] = hw1FindEigendigits(A);

% use only first few eigenvecs
V_ = V(:, 1:K);
invV_ = inv(V_' * V_) * V_';

% try reconstruct original figures
for i = 1 : 20
    I = testImages(:,:,1,i);
    I = double(I(:)) - m;
    
    O = V_ * (invV_ * I);
    
    I = reshape(I, 28, 28);
    O = reshape(O, 28, 28);
    
    imwrite(I, ['testIn', int2str(i), '.png']);
    imwrite(O, ['testOut', int2str(K), '_', int2str(i), '.png']);
end
