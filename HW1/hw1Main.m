% load from file
load digits.mat;

N = 5000;
%K = 2;

% unroll each data, save in matrix X
A = [];
for i = 1 : N
    img = trainImages(:,:,1,i);
    A = [A, img(:)];
end

[m, V] = hw1FindEigendigits(A);

% use only first 50 eigenvecs
V_ = V(:, 1:100);

% test
for i = 1 : 20
    I = testImages(:,:,1,i);
    I = double(I(:)) - m;
    O = V_ * (V_' * I);
    
    I = reshape(I, 28, 28);
    O = reshape(O, 28, 28);
    
    imwrite(I, ['testIn', int2str(i), '.png']);
    imwrite(O, ['testOut', int2str(i), '.png']);
end