# AWSLambdaFunctions
Lambda function to store data in s3 using Python 3.6

### Dependencies
1) boto3
2) json

### Steps
1. install boto3 library in the project folder by below command:
```python
pip install boto3 -t .
```
2. Create a config file with the name s3config.py in the same project folder with the following format:
```javascript
s3 = {
    'aws_access_id': 'your aws access id',
    'aws_access_key': 'you aws access key'
}
```
To get access id and access key follow instructions [Here](http://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html)

3. Create deployment project of the project. Select necessary files and dependencies inside the project folder and compress in .zip format.

4. Login to AWS account

5. Create a Lambda function from scatch

6. Select Python 3.6 as runtime environment and click the option 'upload a .zip file' in Code Entry Type dropdown.

7. Write the Handler function as filename.handle_function_name. For this example we write lambdas3.lambda_handler.

8. Select appropriate role and click on save.

9. Create a new test case as mentioned below:
```javascript
{
"body": 
      {
  "test": "value3",
  "key2": "value2",
  "key1": "value1"
      }
}
```
