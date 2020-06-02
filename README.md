
# Regression_Predict_Package
![Image of Yaktocat](https://cdn1.vc4a.com/media/2015/12/Sendy-delivery-900x322.jpg)

# Team 24

Sendy aims to improve the efficiency of businesses by providing faster delivery of their products.

# Quick overview

## Goal of this project

The goal of this project was to have an overview of machine learning. 

We had to build & test models.

The aim of this project is to help Sendy improve their logistics and communicate an accurate arrival time to their customers. This is done through building a prediction model that estimates time of delivery of orders, from the point of driver pickup to the point of arrival at final destination.

The model will enhance customer communication and improve the reliability of Sendy's services; which will ultimately improve customer experience. In addition, the solution from the model will enable Sendy to realise cost savings, and ultimately reduce the cost of doing business, through improved resource management and planning for order scheduling.



### Modelling (second dataset)

- "./code": functions and code used to generate models, tests, benchmarks, clean data...
- "./data": datasets used,


# Focus on the project & methods used

## First part: generate the Data Quality

The first step is an important part of the Data analysis process; we had to make sure it is possible to have insights about the data, to detect problems (missing values, strange values, outliers, etc.) and to make decision about these problems.

For this first assignment, we worked with train.csv, riders.csv..etc dataset; the goal was to predict the salary of a person, considering his age, the job of his parents, his level of education, etc.


## Second part: modelling & predictions

For this second part, we had to work on the models themselves; we had to choose three models and we had to test them with the data, to choose the most appropriate (and try to explain why it was the most appropriate).


### Code output example

```


####################################
### Models Train_RMSE & Test_RMSE###
####################################


 	
4 	multi_linear, Subset 	784.843998 	753.540672 
1 	Least Squares, All 	784.846983 	753.480916
2 	Ridge 	784.842240 	753.536339
3 	LASSO 	784.860396 	753.537426
4 	multi_linear, Subset 	784.843998 	753.540672


```

