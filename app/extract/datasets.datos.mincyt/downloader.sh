#!/bin/bash
while read p; do
  wget -c "$p"
done <links.txt