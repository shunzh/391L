function [accuracy] = hw1Classify(inN, outN, M, K)
	% load from file
    load digits.mat;
    
    % unroll each data, save in matrix X
    A = [];
    for i = 1 : inN
        img = trainImages(:,:,1,i);
        A = [A, img(:)];
    end
    
    [m, V] = hw1FindEigendigits(A);
    
    % use only first few eigenvecs
    V_ = V(:, 1:M);
    invV_ = inv(V_' * V_) * V_';
    
    % convert training samples into eigenspace
    trainEigens = [];
    for i = 1 : inN
        I = trainImages(:,:,1,i);
        I = double(I(:)) - m;
        I = invV_ * I;
        
        trainEigens = [trainEigens, I];
    end
    
    % test on test set
    testEigens = [];
    for i = 1 : outN
        I = testImages(:,:,1,i);
        I = double(I(:)) - m;
        I = invV_ * I;
        
        testEigens = [testEigens, I];
    end
    
    results = knn(testEigens', trainEigens', trainLabels, K);

    accuracy = sum(results == testLabels(1:outN)') / outN;
end
