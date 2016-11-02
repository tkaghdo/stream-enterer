source("C:\\workspace\\Coursera R Class\\Assignment 3\\best.R")
source("C:\\workspace\\Coursera R Class\\Assignment 3\\worst.R")
source("C:\\workspace\\Coursera R Class\\Assignment 3\\rank_h.R")

rankhospital <- function(state, outcome, num = "best") {
	setwd("C:\\workspace\\Coursera R Class\\Assignment 3")
	return_value <- ""
	## Read outcome data
	outcome_df <- read.csv("./rprog-data-ProgAssignment3-data/outcome-of-care-measures.csv", colClasses = "character")
	
	## Check that state and outcome are valid
	#create a vector of unique values
	state_vect <- unique(outcome_df$State)
	outcome_vect <- c("heart attack", "heart failure", "pneumonia")
	## Check that state and outcome are valid
	if (any(state_vect == state) != TRUE){
		stop("invalid state")
	}
	if (any(outcome_vect == outcome) != TRUE){
		stop("invalid outcome")
	}
	
	## Return hospital name in that state with the given rank
	if (num == "best"){
		return_value <- best(state,outcome)
	}
	else if (num == "worst"){
		return_value <- worst(state,outcome)
	}
	else{
		return_value <- rank_h(state,outcome,num)
	}
	
	## 30-day death rate
	return_value
}