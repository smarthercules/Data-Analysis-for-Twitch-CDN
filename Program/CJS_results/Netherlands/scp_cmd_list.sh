region = us_period_0, us_period_1, United_Kingdom, Netherlands, France, Germany
path = ~/Desktop/Cheng_Thesis/ch5/ch5.1_Preliminaries
# get file
scp nslab@140.112.42.161:~/Desktop/Jill_test/CJS.R ./

# get results
scp -r nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_1/p2_est_result ./

# send file
scp ./kmeans_phase1.py nslab@140.112.42.161:~/Desktop/Af_Oral_test/us_period_0

# send folder
scp -r ./k_means nslab@140.112.42.161:~/Desktop/Cheng_Thesis/ch5/ch5.1_Preliminaries

# test
scp ./label_test.txt nslab@140.112.42.161:~/Desktop/Af_Oral_test/us
scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/out_test.txt ./
scp nslab@140.112.42.161:~/Desktop/Af_Oral_test/us/p1_capture_history/n_cluster_3/label_test_1.txt ./
