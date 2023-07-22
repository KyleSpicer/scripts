#!/bin/bash

for i in $(seq 1 133); do
    echo -n "ERRNO: $i - "
    errno $i
done
