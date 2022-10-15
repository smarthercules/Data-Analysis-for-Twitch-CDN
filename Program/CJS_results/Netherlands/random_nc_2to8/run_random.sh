files='12 13 14 15 16 17 18 19'
n_clusters='8'
periods='1'
for period in $periods
do
	echo "start period: $period"
	for n_cluster in $n_clusters
	do
		for loop in $files
		do
			echo "start: n_clusters_$n_cluster, label_$loop"
			python kmeans_random_phase1.py $period $n_cluster $loop
			Rscript CJS.R ./p1_capture_history/period_$period/n_cluster_$n_cluster/label_$loop.txt ./p1_capture_history/period_$period/n_cluster_$n_cluster/group_label_$loop.txt > ./R_capture_probability/period_$period/n_cluster_$n_cluster/r_$loop.txt
			python cheng_random_kmeans_phase2.py $period $n_cluster $loop
			done
	done
done
