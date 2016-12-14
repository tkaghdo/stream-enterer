## 3. Resilient Distributed Datasets (RDD's) ##

raw_data = sc.textFile("daily_show.tsv")
raw_data.take(5)

## 6. Pipelines ##

daily_show = raw_data.map(lambda line: line.split('\t'))
daily_show.take(5)
# Hit check to see the output

## 8. ReduceByKey() ##

tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)
print(tally)

## 9. Explanation ##

tally.take(tally.count())

## 10. Filter ##

def filter_year(line):
    # Write your logic here
    if line[0] == "YEAR":
        return False
    else:
        return True

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))

## 11. All together now ##

filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)