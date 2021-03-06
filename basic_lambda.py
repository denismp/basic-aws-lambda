import os
import sys
#import boto3
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

    my_response = { 'statusCode': 200, 'body': json.dumps(my_object.get_response())}
    print(f"my_response={my_response}")
    logger.info("my_response={}".format(my_response))
    return my_response

def main():
    """
    Main called when run from the commnd line.
    """
    lambda_handler(None,None)

if __name__ == "__main__":
    '''We are being called from the command line and not from AWS'''
    main()