
# Created on Wed Apr  3 15:53:10 2019

# Author : Vishal Rathod


import boto3
import json
import os
import time


def lambda_handler(event, context):
    """
    This function sends a message to the SQS queue.
    """
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=os.environ['QUEUE_NAME'])
    message = json.dumps(event)
    response = queue.send_message(MessageBody=message)
    return response

print(lambda_handler)


"""
OUTPUT:
<function lambda_handler at 0x7f7b8a0f8b10>
"""