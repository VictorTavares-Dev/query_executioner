import boto3

class AthenaQueryExecutor:
    def __init__(self, database, s3_output_location):
        self.database = database
        self.s3_output_location = s3_output_location
        self.client = boto3.client('athena', region_name='us-east-1')

    def execute_query(self, query):
        response = self.client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': self.database
            },
            ResultConfiguration={
                'OutputLocation': self.s3_output_location,
            }
        )
        return response['QueryExecutionId']
