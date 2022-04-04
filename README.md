# ESD G09 Team 02 - SafeTravel: Travel Insurance

## Members
Chua Jia Qi Nikki, nikki.chua.2020@scis.smu.edu.sg

Esther Wee Hui Ying, esther.wee.2020@scis.smu.edu.sg 

Heng Wei Shin, wsheng.2019@accountancy.smu.edu.sg

Lim Yong Wei, Calista calista.lim.2020@scis.smu.edu.sg

Stephanie Winata, stephaniew.2020@scis.smu.edu.sg

Tan Li Qi, liqi.tan.2020@scis.smu.edu.sg

## Project Description

In the recent years, Insurtech has gained popularity due to its convenience and growing tech literacy amongst those interested to buy insurance. With the rapid growth for fintech capabilities, almost every industry is expected to get disrupted. Insurance, a greatly people-based business, is no different. 

We aim to offer customers the comfort of having an agent assigned to them, following the traditional model of insurance and preserving the human-touch, and further include the convenience of being able to purchase insurance anytime and anywhere. 

## User Scenario Diagrams

**to be inserted**

## Technical Overview Diagrams

**to be inserted**


# 1. Install Dependencies

## Firebase
We are using firebase for data storage. Firebase allows GET, SET, UPDATE of data via the Firebase API. For Mac, use **pip3** instead

```
pip install firebase_admin
```

## Google
Google API are used for User Authentication, Firebase and Gmail API
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```


# 2. Using Docker

## Prepare YAML File
Please ensure that you replace \<**dockerid**\> in the _docker-compose.yml_ file with your own dockerid

## Start WAMP/MAMP
Before we run the containers, please ensure that WAMP/MAMP is set up.

## Docker Compose
### Build Images, Run Containers
In a CMD window, change directory to the folder containing _docker-compose.yml_ and enter the following command 
```
docker-compose up -d
```
If you list the images with `docker image ls`, you will see that the required images have been built for the containers


