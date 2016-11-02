
pollutantmean <- function(directory, pollutant, id = 1:322) {
    counter <- 0
    for (i in id) {
        #DATA<-rbind(DATA,read.csv("c:\\temp\\file1b.csv",header=T))
        counter <- counter + 1
        id_str <- ""
        if (i < 10) {
            id_str <- paste("00",toString(i),sep = "")
        }
        else if (i >= 10 && i < 100) {
            id_str <- paste("0",toString(i),sep = "")
        }
        else{
            id_str <- toString(i)
        }
        file_path <- paste(directory,"\\",id_str,".csv",sep = "")
        
        if (counter == 1){
            df <- read.csv(file_path, header = TRUE)
        }
        else{
            df <- rbind(df,read.csv(file_path, header = TRUE))
        }
    }
    #mean(df[,2],na.rm = TRUE)
    pollutant_mean <- 0
    if (pollutant == "sulfate"){
        pollutant_mean <- mean(df$sulfate,na.rm = TRUE)
    }
    else if (pollutant == "nitrate"){
        pollutant_mean <- mean(df$nitrate,na.rm = TRUE)
    }
    
    #return
    
}

pollutant_mean <- pollutantmean("C:\\workspace\\Coursera R Class\\Assignment 1\\specdata","nitrate", 70:72)


