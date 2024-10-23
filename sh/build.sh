#!/usr/bin/env bash

# sh/build.sh
# build for production

poetry build
poetry publish --build --repository pypi
pip install jsonpycraft
