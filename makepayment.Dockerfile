FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt -r amqp.reqs.txt
COPY ./makePayment.py .
COPY ./esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json .
COPY ./amqp_setup.py ./invokes.py ./
CMD [ "python", "./makePayment.py" ]
