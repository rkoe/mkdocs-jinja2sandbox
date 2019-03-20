#!/usr/bin/env bash
#
# Run sandbox-test.

cd "$(dirname $0)"
mkdocs build -c

cat site/index.html
