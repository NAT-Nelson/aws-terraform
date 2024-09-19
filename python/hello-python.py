def lambda_handler(event, context):
    # Return a properly formatted JSON response
    return {
        'statusCode': 200,
        'body': '{"message": "Hello, World!"}',
        'headers': {
            'Content-Type': 'application/json'
        }
    }
