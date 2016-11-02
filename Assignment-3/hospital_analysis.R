#PART 1

setwd("C:\\workspace\\Coursera R Class\\Assignment 3")
print(getwd())
outcome <- read.csv("./rprog-data-ProgAssignment3-data/outcome-of-care-measures.csv", colClasses = "character")
head(outcome)

outcome[, 11] <- as.numeric(outcome[, 11])
hist(outcome[, 11])


