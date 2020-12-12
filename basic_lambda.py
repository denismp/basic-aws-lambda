import os
import sys
import boto3
import logging
import json

class BasicLambda():
    def __init__(self):
        self.response = { 'message': "Hello world..."}

    def get_response(self):
        return self.response

def lambda_handler(event, context):
    """
    This method is the default lambda handler that is called by the AWS lambda service
    :param event:
    :param context:
    :return: Json response
    """
    my_object = BasicLambda()

    return json.dumps(my_object.get_response())

def main():
    """
    Main called when run from the commnd line.
    """
    lambda_handler(None,None)

if __name__ == "__main__":
    '''We are being called from the command line and not from AWS'''
    main()