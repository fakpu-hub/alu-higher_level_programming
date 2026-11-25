#!/bin/bash
# This script displays the HTTP methods accepted by a server.
curl -s -I "$1" | grep -i "Allow:" | cut -d' ' -f2-
