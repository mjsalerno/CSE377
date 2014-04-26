#!/bin/bash

cd ~
date 	>> homecontent
ls -l 	>> homecontent
echo -------------------- >> homecontent
find ~ -maxdepth 1 -type f | grep -v homecontent | xargs cat >> homecontent
# i dont know how to get the cat of one file