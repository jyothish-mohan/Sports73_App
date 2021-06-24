# Sports73_App
A simple web application which classifies 73 categories of sports.

This is a small web application which predicts the name of the sport when you upload an image of a sport that is unknown to you.

## How did I create this ?
 
Given below are the main libraries and Frameworks that I have used to build this application.

1) Flask Web Framework(It is very easy to build a small application quickly with Flask than Django)
2) Tensorflow (Because I'm better at working with Tensorflow than PyTorch as of now)

## How did I create the ML Model ?

I have leveraged the power of transfer learning to create this classification model. I have trained the model with two pretrained networks MobilenetV2 and InceptionV3, and between these two models InceptionV3 was the winner with about 99.99% accuracy on the training set and 93.4% accuracy on the dev set, but a small downside was this model is a bit slower when prediction than MobilenetV2.

The model was trained on Google Colab GPU Instance.The code for training this model have given above.

## Results when the app is running

![before_pred](https://user-images.githubusercontent.com/56919787/123284282-c32fd780-d529-11eb-84e4-7e089fd55de4.png)
