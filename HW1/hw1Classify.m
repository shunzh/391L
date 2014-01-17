% load from file
load digits.mat;

N = 1000;
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

% convert training samples into eigenspace
trainEigens = [];
for i = 1 : N
    I = trainImages(:,:,1,i);
    I = double(I(:)) - m;
    I = V_' * I;
    
    trainEigens = [trainEigens, I];
end

for i = 1 : N
    I = testImages(:,:,1,i);
    I = double(I(:)) - m;
    I = V_' * I;
    
    dist = trainEigens - repmat(I, 1, size(trainEigens, 2));
    columnSum = sum(dist .^ 2, 1);
    [val, index] = min(columnSum);
    
    if trainLabels(index) == testLabels(i)
        disp('GOT');
    else
        disp('fail');
    end
end;

% utilities
