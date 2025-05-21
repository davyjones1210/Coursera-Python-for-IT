#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        # echo "Command failed, retrying..."
        # Sleep for n seconds
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;