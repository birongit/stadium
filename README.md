# Stadium

[![Build Status](https://github.com/birongit/stadium/actions/workflows/build-test.yml/badge.svg?master)](https://github.com/birongit/stadium/actions)
[![codecov](https://codecov.io/gh/birongit/stadium/branch/master/graph/badge.svg)](https://codecov.io/gh/birongit/stadium)

## Run and Test

Commands to run and test the code, also used as pre-merge checks.

### Run
The basic functionality can be executing by running the following test:
```
python test_game.py
```

### Check
Using flake8 linting to check code format.
```
flake8 . --count --show-source --statistics
```

### Test
Run all tests.
```
pytest
```

### Code coverage
Coverage reports can be generated with xml or html output:
```
pytest --cov --cov-report=html .
pytest --cov --cov-report=xml .
```

