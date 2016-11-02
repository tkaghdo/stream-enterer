# The purpose of this project is to demonstrate your ability to collect, work with, and clean a data set. The goal is to prepare tidy data that can be used for   
#later analysis. You will be graded by your peers on a series of yes/no questions related to the project. You will be required to submit: 1) a tidy data set as 
#described below, 2) a link to a Github repository with your script for performing the analysis, and 3) a code book that describes the variables, the data, and
#any transformations or work that you performed to clean up the data called CodeBook.md. 

library(plyr);

#this function merges the train and test files
merge_files <- function(file_path,folder_1,folder_2,file_1,file_2,var_name,features=FALSE){
	#read test and train files
	test_df <- read.table(file.path(file_path, folder_1 , file_1),header = FALSE)
	train_df <- read.table(file.path(file_path, folder_2, file_2),header = FALSE)
	#union both test and train data frames
	merged_df <- rbind(train_df, test_df)
	#name the variable	
	if (features != FALSE){
		feature_names <<- read.table(file.path(data_files_path , "features.txt"),head=FALSE)
		names(merged_df)<- feature_names$V2
	}
	else{
		names(merged_df)<- c(var_name)
	}
	
	#return
	merged_df
}

#set the data folder
data_files_path <- file.path("./" , "UCI HAR Dataset")

#merge test and train files
test_train_df <- merge_files(data_files_path,"test","train","Y_test.txt","Y_train.txt","activity")
subject_df <- merge_files(data_files_path,"test","train", "subject_test.txt","subject_train.txt","subject")
features_df <- merge_files(data_files_path,"test","train", "X_test.txt","X_train.txt","",TRUE)

#join subject with activity
join_activity_with_subject <- cbind(subject_df, test_train_df)
merged_data <- cbind(features_df, join_activity_with_subject)

#subset mean and std
feature_names_replacement <- feature_names$V2[grep("mean\\(\\)|std\\(\\)", feature_names$V2)]

subject_activity_names<-c(as.character(feature_names_replacement), "subject", "activity" )

merged_data<-subset(merged_data,select=subject_activity_names)

activity_labels <- read.table(file.path(data_files_path, "activity_labels.txt"),header = FALSE)

merged_data$activity<-factor(merged_data$activity);
merged_data$activity<- factor(merged_data$activity,labels=as.character(activity_labels$V2))

#rename variable names
names(merged_data)<-gsub("^t", "Time", names(merged_data))
names(merged_data)<-gsub("^f", "Frequency", names(merged_data))
names(merged_data)<-gsub("Acc", "Accelerometer", names(merged_data))
names(merged_data)<-gsub("Gyro", "Gyroscope", names(merged_data))
names(merged_data)<-gsub("Mag", "Magnitude", names(merged_data))
names(merged_data)<-gsub("BodyBody", "Body", names(merged_data))


tidy_df<-aggregate(. ~subject + activity, merged_data, mean)
tidy_df<-tidy_df[order(tidy_df$subject,tidy_df$activity),]

#output the tidy data set
write.table(tidy_df, file = "tidydata.txt",row.name=FALSE)

str(tidy_df)

