# Model Zoo

## Introduction  
This directory contains all the models we use, include simple LSTM, simple GRU, Seq2One and one combination of LSTM & GRU.

## Description
Our models:

* LSTM

  * One layer bidirection LSTM

  * Two layers bidirection LSTM

* GRU

  * One layer bidirection GRU

* Combination of LSTM & GRU

  * We have a pre-trained model for this one on google drive, link is https://drive.google.com/open?id=1OU0jZw3SEe6JUumQuW40YaQs9rP6qk-6

* Seq2One

  * Encoder: LSTM and GRU

  * Decoder: Attention mechanism

The training data includes the question that was asked, and whether it was identified as insincere (target = 1). The ground-truth labels contain some amount of noise: they are not guaranteed to be perfect.

## To train a model
The dataset we use is on the kaggle competition: https://www.kaggle.com/c/quora-insincere-questions-classification. To train our models, after downloading the code, you can:

- Upload to your own kaggle kernel and you'll be able to run it. 

- Download the dataset on your own machine and change the path in the code to where you store the dataset.
 Then run the code.

## To use pre-trained model to test your own sentence
- You need to download below four things to one folder
  - pre-trained model(link is above)

  - pre_trained_predict.ipynb 

  - en_core_web_lg-2.2.5 (This is a folder on google drive: https://drive.google.com/open?id=1h8ygWJh1iKfgBBnZCOxHdEYFK5iT2YIl)

  - quora_dict.txt (https://drive.google.com/open?id=17zDlY0jpg0IdSRjv9ersaZPWHu_E3SSi)

- In the pre_trained_predict.ipynb, change the variable s to the sentence you want to test and run it.
