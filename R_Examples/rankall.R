rankall <- function(outcome, num = "best") {
  ## Read outcome data
  data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  if(outcome == 'heart attack') {
    i <- 11
  }
  else if(outcome == 'heart failure') {
    i <- 17
  }
  else if(outcome == 'pneumonia') {
    i <- 23
  }
  else {
    stop('invalid outcome')
  }
  unique.states <- sort(unique(data$State))
  # print(unique.states)
  result.df <- list()
  for(state in unique.states) {
    data.state <- data[data$State == state, ]
    data.state[, i] <- as.numeric(x=data.state[, i])
    data.state <- data.state[complete.cases(data.state), ]
    # print(num)
    if(num == "best") {
      numrank = 1
    }
    else if(num == "worst") {
      numrank = nrow(data.state)
      # if(state == 'WI') {
      # print(num)
      # print('WI num')
      # }
    }
    else if(is.numeric(x=num)) {
      # print(num)
      if(num < 1 || num > nrow(data.state)) {
        result.df <- rbind(result.df, list(NA, state))
        print(state)
        next
      }
      else numrank <- num
      # print(num)
    }
    else {
      stop('invalid num')
    }
    # print(num)
    data.state <- data.state[order(data.state[,i], data.state$Hospital.Name), ]
    # if(state == 'WI') {
    # print(data.state[, c(2,i)])
    # print(numrank)
    # print(nrow(data.state))
    # }
    return.names <- data.state[numrank, ]$Hospital.Name
    # print(return.names[1])
    result.df <- rbind(result.df, list(return.names[1], state))
    # print(result.df)
  }
  result.df <- as.data.frame(x=result.df)
  colnames(x=result.df) <- c('hospital', 'state')
  result.df
}