#!/bin/bash
# This script displays the body of a GET request only if the status code is 200.
curl -s -L -w "%{http_code}" "$1" -o /tmp/body; [ "$(cat /tmp/body)" ] && [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && cat /tmp/body
