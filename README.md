# HadoopMR

## Projects Statement
Learn about Hadoop Distributed File System and MapReduce methodology.

Summarize and categorize total sales for specific stores over a 1M-entries global transaction ledger.

## Codes
- Mapper : mapper_store_sales_count.py
- Reducer: reducer_store_sales_count.py

## Run Hadoop MR Jobs

### Self-test

HadoopMR$ ./mapper_store_sales_count.py 

f1  f2      f3  f4  f5  f6

c1  c2  c3  c4  c5  c6

^D (Crtl-D)

f3  f5

c3  c5

HadoopMR$ head -50 purchases.txt > purchase_self_testfile

HadoopMR$ cat purchase_self_testfile | ./mapper_store_sales_count.py

HadoopMR$ cat purchase_self_testfile | ./mapper_store_sales_count.py | sort | ./reducer_store_sales_count.py

### Prerequisite of run
hadoop fs -ls    #returns files listing

hadoop fs -put purchase.txt    #upload input file to HDFS

hadoop fs -tail purchase.txt    #display tail

hadoop fs -cat purchase.txt

hadoop fs -mv purchase.txt purchase1.txt    #rename

(Above are good to know but useless to this project)


hadoop fs -mkdir inputDir

hadoop fs -put purchase.txt inputDir    #upload to directory in HDFS system

### Run MR
[Short Version]

hs {mapper_code} {reducer_code} {input_dir} {output_dir}

hs mapper_store_sales_count.py reducer_store_sales_count.py inputDir outputDir


hs is alias for:

hadoop jar {path/to/jar} -mapper {mapper_code} -reducer {reducer_code} -file {mapper_code} -file {reducer_code} -input {input_dir} -output {output_dir}

### After run
Files in {output_dir}:
- _SUCCESS: Means it succedded
- _logs: Log
- part-00000: Output of reducer

hadoop fs -get part-00000    #download result files from HDFS to local disk