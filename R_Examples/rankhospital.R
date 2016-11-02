rankhospital <- function(state, outcome, num = "best") {
  ## Read outcome data
  results <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  ## Check that state and outcome are valid
  if (nrow(results[results$State == state, ]) == 0) 
    stop("invalid state")
  ## Return hospital name in that state with the given rank
  ## 30-day death rate
  
  if (num == "best")
    num <- 1
  
  if (outcome == "heart attack"){
    heartAttacks.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
    heartAttacks.df <- na.omit(heartAttacks.df)
    heartAttackForState <- subset(heartAttacks.df, heartAttacks.df$results.State == state)
    
    if (num != "worst"){
      heartAttackForStateSorted <- heartAttackForState[order(heartAttackForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack.),] 
    }
    else{
      num <- 1
      heartAttackForStateSorted <- heartAttackForState[order(heartAttackForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack.,decreasing = TRUE),] 
    }
    heartAttackForStateNthRow <- heartAttackForStateSorted[num,]
    nThHeartAttackHospital <- heartAttackForStateNthRow$results.Hospital.Name
    returnValue <- nThHeartAttackHospital
  }
  else if (outcome == "heart failure"){
    heartFailures.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure))
    heartFailures.df <- na.omit(heartFailures.df)
    heartFailuresForState <- subset(heartFailures.df, heartFailures.df$results.State == state)  
    
    if (num != "worst"){
      heartFailuresForStateSorted <- heartFailuresForState[order(heartFailuresForState$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure),] 
    }
    else{
      heartFailuresForStateSorted <- heartFailuresForState[order(heartFailuresForState$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure,decreasing = TRUE),] 
    }
    heartFailuresForStateNthRow <- heartFailuresForStateSorted[num,]
    nThHeartFailureHospital <- heartFailuresForStateNthRow$results.Hospital.Name
    returnValue <- nThHeartFailureHospital
  }
  else if (outcome == "pneumonia"){
    pneumonia.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
    pneumonia.df <- na.omit(pneumonia.df)
    pneumoniaForState <- subset(pneumonia.df, pneumonia.df$results.State == state) 
    
    if (num != "worst"){
      pneumoniaForStateSorted <- pneumoniaForState[order(pneumoniaForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia.),] 
    }
    else{
      pneumoniaForStateSorted <- pneumoniaForState[order(pneumoniaForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia.,decreasing = TRUE),]       
    }
    pneumoniaForStateNthRow <- pneumoniaForStateSorted[num,]
    nThpneumoniaHospital <- pneumoniaForStateNthRow$results.Hospital.Name
    returnValue <- nThpneumoniaHospital
  }
  else{
    stop("invalid outcome")
  }
  as.character(returnValue)
}