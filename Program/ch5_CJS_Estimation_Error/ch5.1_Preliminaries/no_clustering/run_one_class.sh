sample_hours='0 1 2 3'
for hour in $sample_hours
do
	python kmeans_phase1_one_class.py 1 $hour
	Rscript CJS_one_class.R ./p1_capture_history.txt > ./r_no_clustering.txt
	python kmeans_phase2_one_class.py 1 $hour
done
