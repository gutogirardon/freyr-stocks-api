#!/usr/bin/sh
for f in `git diff --name-only upstream/master | grep py  `; do
        echo $f;
        autopep8 -i -a $f;
        pylint $f;
done
