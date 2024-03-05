#/bin/bash
script_dir=$(realpath "$(dirname "$0")")
pushd ${script_dir}/..

source .venv/bin/activate
python main.py

popd