
complete <- function(directory, id = 1:332){
    ids_vector <- vector(mode="numeric", length=0)
    observations_vector <- vector(mode="numeric", length=0)                                               
    file_row_count_no_na <- -999  
    for (i in id) {
        id_str <- ""
        if (i < 10) {
            id_str <- paste("00",toString(i),sep = "")
        }
         else if (i >= 10 && i < 100){
            id_str <- paste("0",toString(i),sep = "")
        }
        else{
            id_str <- toString(i)
        }
        file_path <- paste(directory,"\\",id_str,".csv",sep = "")
            
        df <- read.csv(file_path, header = TRUE)
        file_no_na <- na.omit(df)
        file_row_count_no_na <- nrow(file_no_na)
        #append to id vector
        ids_vector <- union(ids_vector,i)
        #append to complete observations vector
        observations_vector <- union(observations_vector, file_row_count_no_na)
        
    }
    complete_df <- data.frame(ids_vector, observations_vector)
    names(complete_df) <- c("id","nobs")
    
    #return
    complete_df
}

comp <- complete("C:\\workspace\\Coursera R Class\\Assignment 1\\specdata",54)

