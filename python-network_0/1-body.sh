#!/bin/bash
# This script displays the response body only when the HTTP status code is 200.
curl -s -L -w "%{http_code}" "$1" -o /tmp/body | grep -q '^200$' && cat /tmp/body
