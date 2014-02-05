load icaTest.mat;

A = [ 0.8147    0.0975    0.1576    0.1419    0.6557
	0.9058    0.2785    0.9706    0.4218    0.0357
	0.1270    0.5469    0.9572    0.9157    0.8491
	0.9134    0.9575    0.4854    0.7922    0.9340
	0.6324    0.9649    0.8003    0.9595    0.6787];

U = sounds;
X = A * U;
n = 5;
maxRun = 10000;
alpha = 0.0001;

[W, diff] = ica(X, n, alpha, maxRun);