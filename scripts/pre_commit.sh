#!/bin/sh

set -e

make formatting

git add .

make restart
make test