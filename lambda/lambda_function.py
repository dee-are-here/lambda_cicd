import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps("Hello again squared from CICD Lambda!")
    }