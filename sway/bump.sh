#!/bin/bash
REPO=swaywm/sway
SPEC=sway.spec
SHA=$(curl -s https://api.github.com/repos/$REPO/commits/master | jq -r .sha)
echo $SHA
sed -i "s/%global commit          .*/%global commit          $SHA/" $SPEC
