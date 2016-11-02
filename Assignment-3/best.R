library(dplyr)

best <- function(state, outcome) {
	best_hospital <- ""
	setwd("C:\\workspace\\Coursera R Class\\Assignment 3")
	heart_attack_col_loc = 11
	heart_failure_col_loc = 17
	pneumonia_col_loc = 23
	## Read outcome data
	outcome_df <- read.csv("./rprog-data-ProgAssignment3-data/outcome-of-care-measures.csv", colClasses = "character")
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
	
	## Return hospital name in that state with lowest 30-day death
	hospital_df <- subset(outcome_df, State == state)
	#create table data frame
	hospital_tbl_df <- tbl_df(hospital_df)
	#sort by hospital name in case there is a tie
	hospital_tbl_df <- arrange(hospital_tbl_df,Hospital.Name)
	#remove outcome_df from memory
	rm("outcome_df")
	if (outcome == "heart attack"){
		#get the min heart attack value
		min_value <- min(as.numeric(hospital_df[,heart_attack_col_loc]),na.rm=TRUE)
		
		#filter out the rows that have the min heart attacks deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[heart_attack_col_loc] == min_value)
		best_hospital <- result[2]
	}
	else if (outcome == "heart failure"){
		#get the min heart failure value
		min_value <- min(as.numeric(hospital_df[,heart_failure_col_loc]),na.rm=TRUE)
		print(min_value)
		#filter out the rows that have the min heart failure deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[heart_failure_col_loc] == min_value)
		best_hospital <- result[2]
	}
	else if (outcome == "pneumonia"){
		#get the min pneumonia value
		min_value <- min(as.numeric(hospital_df[,pneumonia_col_loc]),na.rm=TRUE)
		
		#filter out the rows that have the min pneumonia deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[pneumonia_col_loc] == min_value)
		best_hospital <- result[2]
	}
	## rate
	best_hospital$Hospital.Name[1]
}