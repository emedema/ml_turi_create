# ml_turi_create
An iOS application developed in order to learn turi create.

Development of this application followed the tutorial found [here](https://heartbeat.fritz.ai/training-a-core-ml-model-with-turi-create-to-classify-dog-breeds-d10009bd30b6)

## Implementation

This app was developed in XCode using Python and Swift. 

## How to Install

First ensure that you have python installed. You can do this by checking the version:

```
python --version
```
So long as you are above Python 2.7 this will work.

You will also need to download the Turi Create library if you have not already. With Turi Create you can build classification, detection, regression, and other types of models

```
pip install turicreate
```

You will also need the dataset(s) we will be using.

## Classifying Dog Breeds

For this simple model we will be using the [Stanford University's Dog Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/). This is a comprehensive dataset of dog pictures of hundreds of different breeds (great for machine learning and casual browsing!).

### Organizing the data

For simplicity, we are only going to download five breeds and organize those files so that each breed has its own file.
