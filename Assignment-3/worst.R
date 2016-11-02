library(dplyr)

worst <- function(state, outcome) {
	worst_hospital <- ""
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
	
	## Return hospital name in that state with highest 30-day death
	hospital_df <- subset(outcome_df, State == state)
	#create table data frame
	hospital_tbl_df <- tbl_df(hospital_df)
	#sort by hospital name in case there is a tie
	hospital_tbl_df <- arrange(hospital_tbl_df,Hospital.Name)
	Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack
	#remove outcome_df from memory
	rm("outcome_df")
	if (outcome == "heart attack"){
		#get the max heart attack value
		max_value <- max(as.numeric(hospital_df[,heart_attack_col_loc]),na.rm=TRUE)
		
		#filter out the rows that have the max heart attacks deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[heart_attack_col_loc] == max_value)
		worst_hospital <- result[2]
	}
	else if (outcome == "heart failure"){
		#get the max heart failure value
		max_value <- max(as.numeric(hospital_df[,heart_failure_col_loc]),na.rm=TRUE)
		#filter out the rows that have the max heart failure deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[heart_failure_col_loc] == max_value)
		worst_hospital <- result[2]
	}
	else if (outcome == "pneumonia"){
		#get the max pneumonia value
		max_value <- max(as.numeric(hospital_df[,pneumonia_col_loc]),na.rm=TRUE)
		
		#filter out the rows that have the max pneumonia deaths
		result <- filter(hospital_tbl_df, hospital_tbl_df[pneumonia_col_loc] == max_value)
		worst_hospital <- result[2]
	}
	## rate
	worst_hospital$Hospital.Name[1]
}