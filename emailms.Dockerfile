FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt -r amqp.reqs.txt
COPY ./amqp_setup.py ./emailms.py ./gmailAPI.py  ./
CMD [ "python", "./emailms.py" ]