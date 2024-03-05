#!/bin/bash
script_dir=$(realpath "$(dirname "$0")")
pushd ${script_dir}/..

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

popd