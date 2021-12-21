# Setting a base image with lambda runtime api
FROM amazon/aws-lambda-python:3.8
# Initially we copy requirements.txt as the caching of this layer as source code may change.
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY lambda_function.py .
# Lambda handler to be invoked on the function start
CMD [ "lambda_function.lambda_handler" ]