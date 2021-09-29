from __future__ import print_function

import boto3
import json
import re
import requests
import os

def lambda_handler(event, context):
    '''The Lambda function handler
    '''
    sns = event['Records'][0]['Sns']
    print('DEBUG:', sns['Message'])
    json_msg = json.loads(sns['Message'])
