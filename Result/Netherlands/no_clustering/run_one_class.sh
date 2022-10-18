periods='0 1'
for period in $periods
do
	echo "start period: $period"
	python kmeans_phase1_one_class.py $period
	Rscript CJS_one_class.R ../p1_capture_history/period_$period/label_n_cluster_0.txt > ../R_capture_probability/period_$period/r_n_cluster_0.txt
	python kmeans_phase2_one_class.py $period
done
