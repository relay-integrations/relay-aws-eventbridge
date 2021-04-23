#!/bin/sh
set -e

if [ -d v-env ]; then
    rm -r v-env
fi
python3.8 -m venv v-env
. v-env/bin/activate
python3.8 -m pip install requests
deactivate
cd v-env/lib/python3.8/site-packages
zip -r9 "${OLDPWD}/function.zip" .
cd "${OLDPWD}"
zip -g function.zip lambda_function.py


echo "You may now upload ./function.zip to Lambda"
