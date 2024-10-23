#!/usr/bin/env bash

# sh/test_build.sh
# build for testing
set -e  # Exit immediately if a command exits with a non-zero status

echo "Building the package..."
poetry build
echo "Publishing to TestPyPI..."
poetry publish --build --repository testpypi
echo "Installing from TestPyPI..."
pip install --index-url https://test.pypi.org/simple/ jsonpycraft
