#!/usr/bin/env bash

# sh/build.sh
# build for production
set -e  # Exit immediately if a command exits with a non-zero status

echo "Building the package..."
poetry build
echo "Publishing to TestPyPI..."
poetry publish --build --repository pypi
echo "Installing from PyPI..."
pip install jsonpycraft
