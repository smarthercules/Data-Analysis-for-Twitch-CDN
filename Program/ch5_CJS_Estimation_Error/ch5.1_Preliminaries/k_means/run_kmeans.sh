sample_hours='0 1 2 3'
for hour in $sample_hours
do
	python kmeans_phase1.py 1 $hour
	Rscript CJS.R ./p1_label.txt ./p1_group_label.txt > ./r_kmeans.txt
	python cheng_kmeans_phase2.py 1 $hour
done
