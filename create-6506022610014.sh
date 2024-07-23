#!/bin/bash

for  i in {seq 1 5}; do
        groupadd group-0$i
        for j in $(seq 1 3);do
                useradd user-g0$i-0$j -g group-0$i -p user-g0$i-0$j
                echo "user-g0$i-0$j:user-g0$i-0$j" | chpasswd
        done
done