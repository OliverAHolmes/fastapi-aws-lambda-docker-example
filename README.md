# FastAPI Poetry Example project

How to run FastAPI server:
```bash
make run_server
```

How to generate requirements:
```bash
make generate_requirements
```

How to generate dev requirements:
```bash
make generate_dev_requirements
```

Run unit tests with coverage:
```bash
make run_tests_with_coverage
```

Run an overall repo health check:
```bash
make push-check
```

Run a synth for the CDK:
```bash
make synth_cdk
```

Deploy the CDK stacks:
```bash
make deploy_cdk
```

Login in to ECR to update image:
```bash
make aws_ecr_login
```

Update and push new version of Docker:
```bash
make update_lambda_docker
```

Update Lambda with latest Docker image:
```bash
make update_lambda_image
```
