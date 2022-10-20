sample_hours='0 1 2 3'
for hour in $sample_hours
do
	python kmeans_phase1_mean_shift.py 1 $hour
	Rscript CJS.R ./p1_label.txt ./p1_group_label.txt > ./r_mean_shift.txt
	python cheng_kmeans_phase2_mean_shift.py 1 $hour
done
