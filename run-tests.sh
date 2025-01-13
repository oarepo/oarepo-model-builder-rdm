#!/bin/bash
set -e

OAREPO_VERSION=${OAREPO_VERSION:-12}
PYTHON=${PYTHON:-python3.12}

BUILDER_VENV=".venv-builder"
export INVENIO_INVENIO_RDM_ENABLED=true
if test -d $BUILDER_VENV ; then
	rm -rf $BUILDER_VENV
fi

$PYTHON -m venv $BUILDER_VENV
. $BUILDER_VENV/bin/activate
pip install -U setuptools pip wheel
pip install -e .


MODEL="thesis"
VENV=".venv-tests"

if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi

oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL -vvv
if test -d $VENV ; then
	rm -rf $VENV
fi
$PYTHON -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel nrp-devtools
$VENV/bin/nrp-devtools proxy 120 &
pip install "oarepo[tests, rdm]==${OAREPO_VERSION}.*" --index-url "http://127.0.0.1:4549/simple" --extra-index-url https://pypi.org/simple

pip install "./build-tests/${MODEL}[tests]" --index-url "http://127.0.0.1:4549/simple" --extra-index-url https://pypi.org/simple
pytest build-tests/$MODEL/tests

