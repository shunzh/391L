load ian.mat;
load ianQuerys.mat;

for i = 1 : 6
	for j = 1 : 10
		res(i,j) = gibbsSample(pa, cpts, qmask(i,:), q(i,:), emask(j,:), e(j,:), 1000, 200);
	end
end

save ianGibbs.mat res;
