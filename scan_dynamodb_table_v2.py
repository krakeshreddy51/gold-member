#Ref:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html
import boto3

client = boto3.client('dynamodb')
response = client.scan(
    ExpressionAttributeNames={
        '#MN': 'Movie_Name',
        '#L': 'Language',
    },
    ExpressionAttributeValues={
        ':a': {
            'S': 'RRR',
        },
    },
    FilterExpression='Movie_Name = :a',
    ProjectionExpression='#MN, #L',
    TableName='Movies',
)

print(response)