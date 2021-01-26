# project3
# Project 3
### Contributors: 
#### Michael Bien, Jennifer Darby, Debra Wu, Jinah Porter

### Description of Project:
In light of the recent pandemic, COVID-19, many people are struggling financially due to the loss of their job, lower hours or overtime pay.
Credit Card companies determine an applicant’s risk based upon multiple metrics.  It is important to understand how these factors can predict one’s ability to pay.  
We chose kaggle credit application and used two machine learning models for binary classification. The Logistic regression model returned 0.96, so we serialized the data using Python Pickle module and loaded our results using a flask server to a custom webpage. 


### Tools Used:
Python, pandas, sklearn, pickle: Data Cleaning, Machine Learning
Flask server was used to serve the HTML/CSS and control the routes
HTML/CSS were used to create the web page
Tableau was used to create the interactive web vizualizations

### Observations
1. The Random Forest Machine Learning Model resulted in a score of .71.
2. The Random Forest Machine Learning Model resulted in a score of .96.
3. The number one driver for credit approval is the applicants payment history.
4. The other features served, such as gender and number of children, had a far less influence.

### THANK YOU EVERYONE