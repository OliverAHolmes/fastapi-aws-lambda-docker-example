#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.api_stack import ApiStack


app = cdk.App()
ApiStack(app, "ExampleApi")


app.synth()
