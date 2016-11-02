source("complete.R")

corr <- function(directory,threshold = 0){
    cor_temp_vect <- vector(mode="numeric", length=0) 
    cor_vect <- vector(mode="numeric", length=0) 
    num_of_files <- 1:332
    for (i in num_of_files){
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
        comp_df <- complete(directory,i)
        if (comp_df$nobs > threshold){
            df <- read.csv(file_path, header = TRUE)
            df_no_na <- na.omit(df)
            cor_temp_vect <- cor(df_no_na$sulfate,df_no_na$nitrate)
        }
        else{
            #cor_temp_vect <- 0
            
        }
        cor_vect <- union(cor_vect, cor_temp_vect)   
    }
    cor_vect
    
}

#corr_df <- corr("C:\\workspace\\Coursera R Class\\Assignment 1\\specdata",150)

set.seed(42)
cc <- complete("specdata", 1:332)
use <- sample(332, 10)
print(cc[use, "nobs"])

