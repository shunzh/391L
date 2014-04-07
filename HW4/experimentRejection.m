load ian.mat;
load ianQuerys.mat;

for i = 1 : 6
	for j = 1 : 10
		res(i,j) = rejectionSample(pa, cpts, qmask(i,:), q(i,:), emask(j,:), e(j,:), 1000);
	end
end

save ianRejection.mat res;
