from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_ecr as ecr,
    CfnOutput,
)

from constructs import Construct

import datetime

import os

API_ECR_ARN = os.environ["API_ECR_ARN"]


class ApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Lambda function
        api_lambda = _lambda.Function(
            self,
            "ExampleApiLambda",
            code=_lambda.Code.from_ecr_image(
                repository=ecr.Repository.from_repository_arn(
                    self,
                    id="example-api",
                    repository_arn=API_ECR_ARN,
                ),
                tag_or_digest="latest",
            ),
            function_name="ExampleApiLambda",
            runtime=_lambda.Runtime.FROM_IMAGE,
            handler=_lambda.Handler.FROM_IMAGE,
            timeout=Duration.seconds(30),  # Set the timeout to 30 seconds
            memory_size=1024,  # Set the memory size to 1024 MB
            description=f"Deployed on {datetime.datetime.now()}",
        )

        # Create the API Gateway
        api = apigateway.LambdaRestApi(
            self,
            "ExampleApiGateway",
            handler=api_lambda,
            deploy_options={"stage_name": "prod"},
        )

        # Add an output to export the API Gateway URL
        CfnOutput(
            self,
            "APIGatewayURL",
            value=api.url,
            description="The URL of the API Gateway",
        )
