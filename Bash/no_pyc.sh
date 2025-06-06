#!/usr/bin/env bash

# Create virtual environment (python3-venv)
# python3 -m venv venv --prompt="backend" --upgrade-deps
FILE=./.venv/bin/activate

# [[ and ]], double bracket conditional tests (logical)
if [[ -d ./.venv && -f $FILE ]]; then
    if ! grep -q 'DONTWRITEBYTECODE\|UNBUFFERED' $FILE; then
        echo '
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
' >> $FILE
    fi
fi


# variable name with a dollar sign $, reference the value it contains

# negate the if condition using the ! (not) operator;
# if ! [[ expr ]]; then

# [ aka test builtin in bash
# file-related tests, https://tldp.org/LDP/abs/html/fto.html
# string-related and integer-related tests
# https://tldp.org/LDP/abs/html/comparison-ops.html

# [[ is a bash extension
# can prevent logic errors in scripts (&&, ||)
