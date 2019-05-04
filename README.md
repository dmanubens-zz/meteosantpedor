# meteosantpedor
Tools to download and extract historical meteo data from meteosantpedor.org (PDF files from 1987 to 2016)

Pre-requisites:
---------------

Python2.7, Camelot, Pandas

Step by step:
-------------

```
cd src/

chmod +x *

./download.sh

./extract.sh

./format.sh

./convert.py
```

Data will be downloaded and extracted in `data/` folder.
