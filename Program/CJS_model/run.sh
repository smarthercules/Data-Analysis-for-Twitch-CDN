files='test_1 test_2 test_3'
for loop in $files
do
    echo "start $loop"
    python kmeans_phase1.py 0 3 $loop
	Rscript CJS.R ./p1_capture_history/n_cluster_3/label_$loop.txt ./p1_capture_history/n_cluster_3/group_label_$loop.txt > ./R_capture_probability/n_cluster_3/r_$loop.txt
	python cheng_kmeans_phase2.py 0 3 $loop
	done

#python kmeans_phase1.py 0 3 test_1
#python kmeans_phase1.py 0 3 test_2
#python kmeans_phase1.py 0 3 test_3
#Rscript CJS.R 3 test_1 > ./R_capture_probability/n_cluster_3/r_test_1.txt
#Rscript CJS.R 3 test_2 > ./R_capture_probability/n_cluster_3/r_test_2.txt
#Rscript CJS.R 3 test_3 > ./R_capture_probability/n_cluster_3/r_test_3.txt