import boto3


def create_envariables_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8080")

    table = dynamodb.create_table(
        TableName='EnVariables',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'value',
                'KeyType': 'RANGE'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'value',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    envariables_table = create_envariables_table()
    print("Table status:", envariables_table.table_status)