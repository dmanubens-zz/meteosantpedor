#!/bin/bash

start="19870901"
end="20161130"

for ((i=start; i <= end; i=$(date -d "$i+1 month" +%Y%m%d))); do
    #echo "camelot -o "$(date -d "$i" +%Y%m)".csv -f csv stream -T 15,700,402,374 "$(date -d "$i" +%Y%m)".pdf"
    camelot -o "$(date -d "$i" +%Y%m)".csv -f csv stream -T 15,700,402,374 "$(date -d "$i" +%Y%m)".pdf
done
