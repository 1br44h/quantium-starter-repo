#!/bin/bash

# activate the virtual environment (windows path)
source venv/Scripts/activate

# execute the test suite
pytest test_app.py

# capture the exit code of the pytest command
EXIT_CODE=$?

# return 0 if passed, or 1 if failed
exit $EXIT_CODE