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

## Other Python Packages
```
pip install flask
pip install -U flask-cors
pip install invoke
pip install pika
pip install SQLAlchemy
pip install virtualenv
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

<img width="1727" alt="Screenshot 2022-04-04 at 11 48 50 PM" src="https://user-images.githubusercontent.com/89062429/161582543-160ff7ee-bfac-4bdf-9803-bc24b8ee94ea.png">

Users will be automatically redirected to the _signin.html_ page if the browser does not detect Customer ID - i.e the user's unique Google ID

## 3.2a) Home Page - New User / No Outstanding Payments (index.html)

Upon successful login via Google, users will be automatically redirected to _index.html_ which will showcase the policies catalog available for purchase

<img width="1726" alt="Screenshot 2022-04-05 at 12 43 11 AM" src="https://user-images.githubusercontent.com/89062429/161593618-073dc26a-409a-42b0-9136-a6e3534abaf4.png">


## 3.2b) Home Page - ERROR HANDLING for Outstanding Payments

If there is an outstanding payment, our business disallows users from browsing and purchasing new policies. A pop-up will appear, and users will be redirected to _payment.html_ to make payment first. [(See Section 3.4)](#makepayment)

<img width="1364" alt="Screenshot 2022-04-05 at 12 51 09 AM" src="https://user-images.githubusercontent.com/89062429/161593663-f0746d2f-484f-42ac-83a4-cf9d6082ecfd.png">

### SMS Alert for Outstanding Payments

An SMS alert will be sent to users to remind them to make payment for oustanding policies
** At the moment, only registered mobile numbers of the Team Members are able to receive SMS notification.

![IMAGE 2022-04-05 01:12:01](https://user-images.githubusercontent.com/89062429/161596465-0523a6fe-8738-4e2d-8165-460b6b9a6fcd.jpg)


## 3.3) Purchase a New Policy

### Click Sign Up
Click on the Sign Up! button of the desired Region

<img width="439" alt="Screenshot 2022-04-05 at 12 35 29 AM" src="https://user-images.githubusercontent.com/89062429/161593745-c0b00995-3127-45a9-9de6-4ac176d62458.png">


### Fill Details
Fill up the required details such as Specific Country and Start/End Date

<img width="1362" alt="Screenshot 2022-04-05 at 12 44 14 AM" src="https://user-images.githubusercontent.com/89062429/161593805-4444ef0a-14d7-4e42-adc4-802581a6c96a.png">

Select sign up button to confirm sign up of policy. Users will be redirected to the _payment.html_ page to make payment for their purchased policy.


## 3.4) My Policies Page (payment.html)

### View Policies
Users can view a list of active policies here. 

<img width="1726" alt="Screenshot 2022-04-05 at 12 52 18 AM" src="https://user-images.githubusercontent.com/89062429/161595761-d5b08bb7-8d47-4064-b2b9-132a56da849e.png">


<a name="makepayment"></a>
### Make Payment
PayPal button will appear if there is an outstanding payment to be made. Since business logic disables new signups if there are outstanding payments, users will only make payment for the latest policy that they have purchased (1-1 relationship for Payment-Policy).

<img width="499" alt="Screenshot 2022-04-05 at 12 58 24 AM" src="https://user-images.githubusercontent.com/89062429/161594303-1b7cf17e-647f-49d7-b8a6-ddac5a193e97.png">


```
// Paypal Sandbox Credentials:

Email: sb-e4wfp788217@personal.example.com
Password: 123456WAD
```

### Policies Page w Updated Status

Upon successful payment via PayPal, page will refresh and indicate payment status as "Paid". Users will be able to browse and purchase new policies.

<img width="1335" alt="Screenshot 2022-04-05 at 12 59 42 AM" src="https://user-images.githubusercontent.com/89062429/161594487-c5562b38-4147-4966-9679-6fe5d7cea2a0.png">

### Receive Invoice via Email

An invoice will be automatically sent to the gmail account associated with the user's Google Login details.

<img width="1123" alt="Screenshot 2022-04-05 at 1 06 21 AM" src="https://user-images.githubusercontent.com/89062429/161595511-b1d1575b-369f-43e2-8882-489b09ce2ccb.png">


# 4. Sign Out

## Click "Log Out" Button
"Log Out" button is available on both Home and Policies page. Upon clicking, users will be signed out from their Google account, and redirected back to the Sign In page

<img width="284" alt="Screenshot 2022-04-05 at 1 14 03 AM" src="https://user-images.githubusercontent.com/89062429/161596635-4ff582e8-a40e-499f-ad8d-0b8e0f64b6f8.png">




