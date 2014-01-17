% load from file
load digits.mat;

N = 1000;
M = 200;
K = 1;

% unroll each data, save in matrix X
A = [];
for i = 1 : N
    img = trainImages(:,:,1,i);
    A = [A, img(:)];
end

[m, V] = hw1FindEigendigits(A);

% use only first few eigenvecs
V_ = V(:, 1:M);

% convert training samples into eigenspace
trainEigens = [];
for i = 1 : N
    I = trainImages(:,:,1,i);
    I = double(I(:)) - m;
    I = V_' * I;
    
    trainEigens = [trainEigens, I];
end

% test on test set
testEigens = [];
for i = 1 : N
    I = testImages(:,:,1,i);
    I = double(I(:)) - m;
    I = V_' * I;
    
    testEigens = [testEigens, I];
end

knnclassify(testEigens', trainEigens', trainLabels, K);

% utilities
