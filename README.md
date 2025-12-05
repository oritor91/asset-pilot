# Asset Pilo FastAPI AWS SAM Template

A production-ready template for building FastAPI services packaged as AWS Lambda
functions fronted by API Gateway using AWS SAM. The repository includes
application scaffolding, infrastructure configuration, and local tooling to
accelerate new project setup.

## Prerequisites

- Python 3.11
- AWS CLI configured with appropriate credentials
- AWS SAM CLI
- Taskfile (https://taskfile.dev)

## Quickstart

```bash
# Install dependencies
task install

# Run tests and type checks
task lint
task typecheck
task test

# Start the FastAPI app locally
task run-local
```

## Environment Configuration

Create a `.env` file in the repository root with the following variables:

```
APP_ENVIRONMENT=local
APP_NAME=Asset Pilo FastAPI Service
APP_VERSION=0.1.0
APP_DESCRIPTION=FastAPI template deployed with AWS SAM and API Gateway.
APP_DOCS_URL=/docs
APP_REDOC_URL=/redoc
APP_AWS_REGION=us-east-1
```

## Project Structure

- `src/app/` – FastAPI application modules and AWS client utilities
- `infra/sam/` – AWS SAM template and build instructions
- `scripts/` – Helper scripts for local development and deployment
- `tests/` – Pytest-based unit test suite
- `Taskfile.yml` – Task runner commands for common workflows

## Deployment

```bash
# Build and deploy with SAM defaults defined in samconfig.toml
task sam-build
task sam-deploy
```

Adjust the `samconfig.toml` and `infra/sam/template.yaml` files as needed for
additional resources (e.g., DynamoDB tables, SQS queues).

## Local Development Notes

- API documentation is available via Swagger UI at `/docs` and ReDoc at `/redoc`.
- `scripts/run_local.sh` bootstraps Uvicorn with live reload.
- AWS clients are initialised via `app.aws.clients` to centralise session
  management and encourage reuse.