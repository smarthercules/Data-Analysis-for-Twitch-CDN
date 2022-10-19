# Data analysis for CDN server population estimation based on CMR model with heterogeneity

## Absract
Data analysis for CDN server population estimation based on CMR model with heterogeneity

Streaming media become more and more popular and important in recent years. Among streaming platforms, Twitch is dominating the game streaming market. In 2021, Twitch had 2,778,000 average concurrent viewers and 105,000 average concurrent streamers.

Similar to other streaming media, Twitch uses Content Delivery Network to provide the service to massive viewers from all around the world. Content Delivery Network (CDN), which is the key part of the streaming system, is crucial for the quality of service.

In the early work, a one-time experiment has been done to survey Twitch's CDN. However, due to the rapid growth of Twitch and the high cost of a detailed scan on CDN, Twitch's CDN remains largely unknown to the public. 

In our previous work, we used the CJS model, which assumes every individual shares the same time-dependent survival rate and capture probability, to estimate the CDN size. However, different servers may have different survival rates and capture probability. If we assume every server has its own survival rate and capture probability, the computation overhead of the CJS model may be too high since there are many parameters needed to estimate. Besides, maximum likelihood estimation would have a large bias if the sample size is too small~\cite{NIST2012}.

In this research, I use the transaction count in hour periods to do clustering on the data from 5 countries and use the CMR model with heterogeneity with these clustering results. Next, I use S\_Dbw score~\cite{989517} to evaluate the clustering results. However, I find a better S\_Dbw score does not lead to have a lower error rate in the MLE-CJS model. Instead, if $ Avg/ Std$ in the number of sample servers larger than 0.3 of a cluster, it will tend to have a larger the estimation error rate. As a result, the clustering results with number of clusters less than 5 tend to have a lower estimation error rate since these clustering results contain less clusters with $ Avg/ Std$ larger than 0.3.


## Complete Video Demonstration
1. Get the data
2. Run CJS model in chapter 5
3. Run .ipynb files for each chapter

## Structure

### ./Presentation: 
My thesis oral presentation, including .pdf file and .ppt file.

### ./Thesis:
The file of my thesis, including .pdf file and latex source file.

### ./Data:
The .md file introduces the Twitch's dataset and data access. One need to follow the instruction to get the data.

### ./Program:
The code I used in my thesis, including .ipynb file and code for the CJS model.
  iPython files (.ipynb): how to get the results of the corresponding chapter in my thesis.
  ./ch5_CJS_Estimation_Error: code and script for runnung the CJS model with clustering results.

### ./Result:
The CJS results of the experiment in my thesis. 
It is divided into p0_cluster_result, p1_capture_history, R_capture_probability, p2_daily_plot, and p2_est_result.

(1) p0_cluster_result: The clustering results I generated by k-means or other algorithms.

(2) p1_capture_history: The capture history for each server. This file is for the input to CJS.R.

(3) R_capture_probability: The capture probability and survival rate caculate by the CJS.R.

(4) p2_daily_plot: The plot of baseline and estimation number of servers on every date.

(5) p2_est_result: The estimation error rate, standard deviation, and the runtime of the CJS model.

### ./Readme:
This file.
