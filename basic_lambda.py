import os
import sys
import boto3
import logging
import json

class BasicLambda():
    pass

def lambda_handler(event, context):
    """
    This method is the default lambda handler that is called by the AWS lambda service
    :param event:
    :param context:
    :return: Json response
    """
    response = { 'message:', "Hello world..."}
    return json.dumps(response)

def main():
    """
    Main called when run from the commnd line.
    """
    lambda_handler(None,None)

if __name__ == "__main__":
    '''We are being called from the command line and not from AWS'''
    main()