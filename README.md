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


# 3. Using the Web Application

## 3.1) Sign In Page (signin.html)

Sign in via Google on the Sign In Page (_/signin.html_) 

**insert screenshot**

Users will be automatically redirected to the _signin.html_ page if the browser does not detect Customer ID - i.e the user's unique Google ID

## 3.2a) Home Page - New User / No Outstanding Payments (index.html)

Upon successful login via Google, users will be automatically redirected to _index.html_ which will showcase the policies catalog available for purchase

**insert screenshot**

## 3.2b) Home Page - ERROR HANDLING for Outstanding Payments

If there is an outstanding payment, our business disallows users from browsing and purchasing new policies. A pop-up will appear, and users will be redirected to _payment.html_ to make payment first. [(See Section 3.4)](#makepayment)

**insert screenshot**


## 3.3) Purchase a New Policy

### Click Sign Up
Click on the Sign Up button of the desired Region.

**insert screenshot**

### Fill Details
Fill up the required details such as Specific Country and Start/End Date

**insert screenshot**

### Confirm Sign Up
Select sign up button to confirm sign up of policy. Users will be redirected to the _payment.html_ page to make payment for their purchased policy.

**insert screenshot**


## 3.4) My Policies Page (payment.html)

### View Policies
Users can view a list of active policies here. 

**insert screenshot**

<a name="makepayment"></a>
### Make Payment
PayPal button will appear if there is an outstanding payment to be made. Since business logic disables new signups if there are outstanding payments, users will only make payment for the latest policy that they have purchased (1-1 relationship for Payment-Policy).

**insert screenshot**


Upon successful payment via PayPal, page will refresh and indicate payment status as "Paid". Users will be able to browse and purchase new policies.

**insert screenshot**

### Receive Invoice

An invoice will be automatically sent to the gmail account associated with the user's Google Login details.

**insert screenshot**


# 4. Sign Out

## Click "Log Out" Button
"Log Out" button is available on both Home and Policies page. Upon clicking, users will be signed out from their Google account, and redirected back to the Sign In page

**insert screenshot**



