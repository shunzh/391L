function [m, V] = hw1FindEigendigits(A)
% Find eigendigits from digits.mat
    % get mean vector
    m = mean(A,2);
    
    % replace X with X - E(X)
    A = double(A) - repmat(m, 1, size(A,2));
    
    % get vec and val
    [vec, val] = eig(A' * A);
    vec = A * vec;
    
    % sort e-vec and e-val
    [val, order] = sort(diag(val), 'descend');
    vec = vec(:, order);
    
    % normalize columns
    V = normc(vec);
end