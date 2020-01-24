# dl_kep

The `dl_kep` is the main script that downloads Kepler data for all quarters, corrects for possible systematics, stitches altogether and saves into a .csv file.

Just supply the KIC ID to run:
```
$ ./dl_kep 6922244 -v
```

There's another script to make a batch file based on the KIC ID parsed from `wget_list.txt`.
To create the batch file, run:
```
./make_batch --wget_file=wget_list.txt
```
Then use [`parallel`](http://macappstore.org/parallel/) to download data in parallel:
```
cat dl_kep.batch | parallel
```
