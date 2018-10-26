#!/bin/sh
PKG=$1
COPR=$2
if [ ! -d "$PKG" ]; then
	echo "No dir: $PKG"
fi
copr add-package-scm --name $PKG --clone-url https://github.com/oranenj/copr-repos.git --subdir $PKG --spec $PKG.spec $COPR

