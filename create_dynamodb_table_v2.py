import boto3

client = boto3.client('dynamodb')

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Movie_Name',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Language',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Movie_Name',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Language',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Movies',
)

print(response)