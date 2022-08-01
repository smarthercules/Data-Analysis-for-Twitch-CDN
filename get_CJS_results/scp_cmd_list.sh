region = us_period_0, us_period_1, United_Kingdom, Netherlands, France, Germany
# get file
scp nslab@140.112.42.161:~/Desktop/Jill_test/CJS.R ./

scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/R_capture_probability/n_cluster_3/label_test.txt ./
scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/out_test_2.txt ./

scp nslab@140.112.42.161:~/Desktop/Jill_test/kmeans_phase2.py ./

# get results
scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_1/p2_est_result ./
scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_1/p2_daily_plot ./

scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom/R_capture_probability ./
scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom/p1_capture_history ./

scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_1/mean_shift ./

scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/France/p1_capture_history/ip_index.txt ./France/p1_capture_history

# send file
scp ./kmeans_phase1.py nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_0
scp ./CJS.R nslab@140.112.42.161:~/Desktop/Af_Oral_test/Netherlands
scp ./cheng_kmeans_phase2.py nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom

scp ./run.sh nslab@140.112.42.161:~/Desktop/Af_Oral_test/Netherlands

scp ./n_cluster_0.csv nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom/p0_cluster_result

scp ./cheng_random_kmeans_phase2.py nslab@140.112.42.161:~/Desktop/Af_Oral_test/Netherlands/random_nc_2to8

scp ./France/kmeans_phase1.py nslab@140.112.42.161:~/Desktop/Af_Oral_test/France



# send folder
scp -r ./p0_cluster_result nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom

scp -r ./p1_capture_history nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom
scp -r ./p2_est_result nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom
scp -r ./p2_daily_plot nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom
scp -r ./R_capture_probability nslab@140.112.42.161:~/Desktop/Af_Oral_test/United_Kingdom

scp -r ./United_Kingdom nslab@140.112.42.161:~/Desktop/Af_Oral_test

scp -r ./no_clustering nslab@140.112.42.161:~/Desktop/Af_Oral_test/France

scp -r ./mean_shift nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_1

scp -r ./random_nc_2to8 nslab@140.112.42.161:~/Desktop/Af_Oral_test/Germany


# test
scp ./label_test.txt nslab@140.112.42.161:~/Desktop/Af_Oral_test/us
scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/out_test.txt ./
scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/p1_capture_history/n_cluster_3/label_test_1.txt ./
