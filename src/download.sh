#!/bin/bash

start="19870901"
end="20161101"

for ((i=start; i <= end; i=$(date -d "$i+1 month" +%Y%m%d))); do
    #echo http://meteosantpedor.org/wp-content/uploads/pauprat/"$(date -d "$i" +%Y%m)".pdf
    wget http://meteosantpedor.org/wp-content/uploads/pauprat/"$(date -d "$i" +%Y%m)".pdf
done
