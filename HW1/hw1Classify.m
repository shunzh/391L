function [accuracy] = hw1Classify(inN, outFrom, outTo, M, K)
	% load from file
    load digits.mat;
    
    % unroll each data, save in matrix X
    A = [];
    for i = 1 : inN
        img = trainImages(:,:,1,i);
        A = [A, img(:)];
    end
    
	% find eigen digits
    [m, V] = hw1FindEigendigits(A);
    
    % use only first few eigenvecs
    V_ = V(:, 1:M);
    invV_ = V_';
    
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
    for i = outFrom : outTo
        I = testImages(:,:,1,i);
        I = double(I(:)) - m;
        I = invV_ * I;
        
        testEigens = [testEigens, I];
    end
    
    results = knn(testEigens', trainEigens', trainLabels(1:inN), K);
    %results = maxLikelihood(testEigens', trainEigens', trainLabels(1:inN), (0:9)');

    accuracy = sum(results == testLabels(outFrom :outTo)') / (outTo - outFrom + 1);
end
