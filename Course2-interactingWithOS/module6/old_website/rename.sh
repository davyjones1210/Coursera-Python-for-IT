#!/bin/bash

for file in *.html; do
        name=$(basename "$file" .html)
        echo mv "$file" "$name.HTM" 
done 