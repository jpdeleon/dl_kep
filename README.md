# dl_kep

The `dl_kep` is the main script that downloads Kepler data for all quarters, corrects for possible systematics per quarter by fitting a simple spline on the baseline, stitches all quarters together on common normalization, and saves the output into a .csv file.

Just supply the KIC ID to run:
```
$ ./dl_kep 6922244 -v
```

There's another script to make a batch file based on the KIC ID parsed from `data/wget_list.txt`.
To create the batch file, run:
```
./make_batch --wget_file=wget_list.txt
```
Then use [`parallel`](http://macappstore.org/parallel/) to run the batch script in parallel:
```
cat dl_kep.batch | parallel
```
