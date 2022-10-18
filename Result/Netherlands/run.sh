files='0 1 2 3 4 5 6 7 8 9'
n_clusters='2 3 4 5 6 7 8'
periods='0 1'
for period in $periods
do
	echo "start period: $period"
	for n_cluster in $n_clusters
	do
		for loop in $files
		do
			echo "start: n_clusters_$n_cluster, label_$loop"
			python kmeans_phase1.py $period $n_cluster $loop
			Rscript CJS.R ./p1_capture_history/period_$period/n_cluster_$n_cluster/label_$loop.txt ./p1_capture_history/period_$period/n_cluster_$n_cluster/group_label_$loop.txt > ./R_capture_probability/period_$period/n_cluster_$n_cluster/r_$loop.txt
			python cheng_kmeans_phase2.py $period $n_cluster $loop
			done
	done
done
