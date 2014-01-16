%function [] = hw1FindEigendigits()
% Find eigendigits from digits.mat
    % load from file
    load digits.mat;
    
    % unroll each data, save in matrix X
    X = [];
    for i = 1 : 2
        img = testImages(:,:,1,i);
        X = [X, img(:)];
    end
    
    % replace X with X - E(X)
    X = double(X) - repmat(mean(X,2),1,size(X,2));
    
    X
%end
