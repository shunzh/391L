%function [] = hw1FindEigendigits()
% Find eigendigits from digits.mat
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
    
    % replace X with X - E(X)
    A = double(A) - repmat(mean(A,2), 1, size(A,2));
    
    % get vec and val
    [vec, val] = eig(A' * A);
    vec = normc(A * vec);
    
    % get new coordinates
    B = vec' * A;
%end
