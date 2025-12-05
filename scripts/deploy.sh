#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

sam build --template-file infra/sam/template.yaml
sam deploy --template-file infra/sam/template.yaml --config-file samconfig.toml "$@"

