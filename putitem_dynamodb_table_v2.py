import boto3

client = boto3.client('dynamodb')
response = client.batch_write_item(
    RequestItems={
        'Movies': [
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Fast &Furious',
                        },
                        'Language': {
                            'S': 'English',
                        },
                    },
                },
            },
             {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Dhoom',
                        },
                        'Language': {
                            'S': 'Hindi',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'War',
                        },
                        'Language': {
                            'S': 'Hindi',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Hunt',
                        },
                        'Language': {
                            'S': 'TELUGU',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Ratchasan',
                        },
                        'Language': {
                            'S': 'Tamil',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Love story',
                        },
                        'Language': {
                            'S': 'Telugu',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Dhee',
                        },
                        'Language': {
                            'S': 'Telugu',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'ValtairV',
                        },
                        'Language': {
                            'S': 'Telugu',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'Bahubali',
                        },
                        'Language': {
                            'S': 'Telugu',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Movie_Name': {
                            'S': 'RRR',
                        },
                        'Language': {
                            'S': 'Telugu',
                        },
                    },
                },
            },
            ],
    },
)

print(response)
