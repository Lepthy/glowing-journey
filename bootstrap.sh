#!/bin/bash

set -e

PYTHON=`which python3`
OPTIONS=-B

VENV=.venv
BIN=${VENV}/bin

PATH=src
MODULE=${PATH}/glowing-journey
ENTRYPOINT=server.py

echo "Boostrapping application..."

if [ ! -d ${VENV} ]; then
    ${PYTHON} -m venv ${VENV}
    ${BIN}/pip install -r requirements.txt
fi

echo "Application successfully bootstrapped"
PYTHONPATH=${PATH} ${BIN}/python ${OPTIONS} ${MODULE}/${ENTRYPOINT}
