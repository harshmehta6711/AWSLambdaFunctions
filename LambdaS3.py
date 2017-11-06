import boto3
import json
import s3config

print('Loading function')
s3 = boto3.resource('s3', aws_access_key_id=s3config.s3['aws_access_id'],
                    aws_secret_access_key=s3config.s3['aws_access_key'])


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        print(data['test'])
        s3.Bucket('bucket').put_object(Key='/AWSTest/' + data['test'] + '.txt', Body=json.dumps(data))
        print("Received event: " + json.dumps(event, indent=2))
        payload = json.loads(event['body'])
        return respond(None, payload)

    except Exception as e:
        raise e
