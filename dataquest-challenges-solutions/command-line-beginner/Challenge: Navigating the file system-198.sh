## 1. Exploring the file system ##

~$ ls -l

## 2. Moving problematic files to a separate folder ##

~$ mv legislators problematic/

## 3. Fixing file extensions ##

~/problematic$ mv legislators legislators.csv

## 4. Consolidating files ##

~$ mv problematic/ csv_datasets

## 5. Restricting permissions ##

~/csv_datasets$ chmod 0740 titanic_survival.csv