% load from file
load digits.mat;

N = 10;
%K = 2;

% unroll each data, save in matrix X
A = [];
for i = 1 : N
    img = trainImages(:,:,1,i);
    A = [A, img(:)];
end

[m, V] = hw1FindEigendigits(A);
