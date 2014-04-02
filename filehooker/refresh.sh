#!/bin/sh
set -eu
cd "$(dirname "$(readlink -f "$0")")"
rm -rvf  out/ work
./build.sh -N filehooker -v
cp -v out/filehooker* /home/makefu/isos
