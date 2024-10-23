# Build Scripts

This document provides an overview of the build scripts used for managing the `jsonpycraft` package.

## Overview

The build scripts automate the processes of building, publishing, and installing the `jsonpycraft` package. They streamline the workflow, reducing the need for manual steps.

## Scripts

### test_build.sh

#### Description
This script is used for building and testing the package in the TestPyPI environment.

#### Content
```bash
#!/usr/bin/env bash

set -e  # Exit immediately if a command exits with a non-zero status

poetry build
poetry publish --build --repository testpypi
pip install -U -i https://test.pypi.org/simple/ jsonpycraft
```

#### Steps
1. **Build the Package**: Uses `poetry build` to create the source distribution and wheel.
2. **Publish to TestPyPI**: Publishes the built package to TestPyPI for testing.
3. **Install from TestPyPI**: Installs the package from TestPyPI to verify the installation.

### build.sh

#### Description
This script is used for building and publishing the package in the production environment.

#### Content
```bash
#!/usr/bin/env bash

set -e  # Exit immediately if a command exits with a non-zero status

poetry build
poetry publish --build
pip install jsonpycraft
```

#### Steps
1. **Build the Package**: Uses `poetry build` to create the source distribution and wheel.
2. **Publish to PyPI**: Publishes the built package to the official PyPI repository.
3. **Install from PyPI**: Installs the package directly from PyPI.

## Usage

Ensure that the scripts have executable permissions. You can set this using:

```sh
chmod +x test_build.sh build.sh
```

For testing, run:

```sh
./sh/test_build.sh  # For testing
```

For production, run:

```sh
./sh/build.sh      # For production
```
