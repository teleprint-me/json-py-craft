#!/usr/bin/env bash

# sh/test_build.sh
# build for testing

poetry build
poetry publish --build --repository testpypi
pip install --index-url https://test.pypi.org/simple/ jsonpycraft
