#!/usr/bin/env sh
#
# Run from the root of a PHP project, creates exuberant-ctags and cscope
# databases.
#
# Uses the `chronic` utility from the moreutils package to shut up `ctags`
# when it finds empty tags in Javascript files.

find -name '*.php' -print > cscope.files
cscope -b
chronic ctags -R .
