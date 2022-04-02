FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./catalog.py .
COPY ./catalog.json .
COPY ./esdg9t02-insurance-firebase-adminsdk-umgr1-f4dd6e06a6.json .
CMD [ "python", "./catalog.py" ]
