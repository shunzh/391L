% load from file
function [accuracy] = hw1Classify(N, M, K)
    load digits.mat;
    
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
    
    results = knn(testEigens', trainEigens', trainLabels, K);

    accuracy = sum(results == testLabels(1:N)');
end
