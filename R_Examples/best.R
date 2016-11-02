best <- function(state, outcome){
  
  results <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  if (nrow(results[results$State == state, ]) == 0) 
    stop("invalid state")
  
  if (outcome == "heart attack"){
    heartAttacks.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
    heartAttacks.df <- na.omit(heartAttacks.df)
    heartAttackForState <- subset(heartAttacks.df, heartAttacks.df$results.State == state)
    
    heartAttackForStateSorted <- heartAttackForState[order(heartAttackForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack.),] 
    heartAttackForStateFirstRow <- head(heartAttackForStateSorted,1)
    bestHeartAttackHospital <- heartAttackForStateFirstRow$results.Hospital.Name
    returnValue <- bestHeartAttackHospital
  }
  else if (outcome == "heart failure"){
    heartFailures.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure))
    heartFailures.df <- na.omit(heartFailures.df)
    heartFailuresForState <- subset(heartFailures.df, heartFailures.df$results.State == state)  
    
    heartFailuresForStateSorted <- heartFailuresForState[order(heartFailuresForState$Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure),] 
    heartFailuresForStateFirstRow <- head(heartFailuresForStateSorted,1)
    bestHeartFailureHospital <- heartFailuresForStateFirstRow$results.Hospital.Name
    returnValue <- bestHeartFailureHospital
  }
  else if (outcome == "pneumonia"){
    pneumonia.df <- data.frame(results$State,results$Hospital.Name,as.numeric(results$Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
    pneumonia.df <- na.omit(pneumonia.df)
    pneumoniaForState <- subset(pneumonia.df, pneumonia.df$results.State == state) 
    
    pneumoniaForStateSorted <- pneumoniaForState[order(pneumoniaForState$as.numeric.results.Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia.),] 
    pneumoniaForStateFirstRow <- head(pneumoniaForStateSorted,1)
    bestpneumoniaHospital <- pneumoniaForStateFirstRow$results.Hospital.Name
    returnValue <- bestpneumoniaHospital
  }
  else{
    print(paste("Error in best(NY,", outcome, ") : invalid outcome"))
  }
  as.character(returnValue)
}
