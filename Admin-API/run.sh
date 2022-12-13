#!/bin/sh
. `dirname $0`/env/bin/activate
FLASK_APP=app FLASK_DEBUG=True CONFIGURATION_CONTEXT=Development flask run --port 8080 --host 0.0.0.0