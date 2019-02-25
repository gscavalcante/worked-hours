#!/bin/bash
# Tip: source aliases.sh in your .bashrc, .bash_profile or .zshrc
# to define aliases in your shell for all known enviroments and servers.
#
# Example:
# source ~/worked-hours/aliases.sh
#

BASEDIR=$(dirname "$0")

alias track="python3 ${BASEDIR}/track.py"
alias report="python3 ${BASEDIR}/report.py"