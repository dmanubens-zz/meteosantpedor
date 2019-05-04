#!/bin/bash

start="19870901"
end="20161130"

cd ../data

for ((i=start; i <= end; i=$(date -d "$i+1 month" +%Y%m%d))); do
    year=$(date -d "$i" +%Y)
    month=$(date -d "$i" +%m)
    sed -e 's/","/   /g' -e 's/"//g' "$(date -d "$i" +%Y%m)"-page-1-table-1.csv > "$(date -d "$i" +%Y%m)".csv
    sed -i  "s/\/$month/\/$month\/$year/g" "$(date -d "$i" +%Y%m)".csv
done
