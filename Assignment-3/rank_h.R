library(dplyr)
library(data.table)

rank_h <- function(state, outcome, num) {
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
	#create data.table
	DT <- as.data.table(hospital_df)
	#create table data frame
	hospital_tbl_df <- tbl_df(hospital_df)
	#sort by hospital name in case there is a tie
	hospital_tbl_df <- arrange(hospital_tbl_df,Hospital.Name)
	#remove outcome_df from memory
	rm("outcome_df")
	if (outcome == "heart attack"){
		DT[,heart_attack_rank:=rank(Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack,ties.method="first"),by=State]
		
		result <- filter(DT, heart_attack_rank == num)
		best_hospital <- result$Hospital.Name 
	}
	else if (outcome == "heart failure"){
		DT[,heart_failure_rank:=rank(Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure,ties.method="first"),by=State]
		
		result <- filter(DT, heart_failure_rank == num)
		best_hospital <- result$Hospital.Name 
	}
	else if (outcome == "pneumonia"){
		DT[,pneumonia_rank:=rank(Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia,ties.method="first"),by=State]
		
		result <- filter(DT, pneumonia_rank == num)
		best_hospital <- result$Hospital.Name 
	}
	## rate
	best_hospital
}