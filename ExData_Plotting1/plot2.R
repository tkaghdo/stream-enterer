library(dplyr)

#import the file
data_df_df = read.table("household_power_consumption.txt",sep=";", na.strings = "?", header=TRUE)

#pull the date range
data_df_df <- data_df_df[(data_df_df$Date=="1/2/2007" | data_df_df$Date=="2/2/2007"),]
# add the datetime variable to the data
data_df_df$DateTime <- strptime(paste(data_df_df$Date, data_df_df$Time, sep=" "), format="%d/%m/%Y %H:%M:%S")


#plot the data
png("plot2.png", width=480, height=480)
plot(data_df_df$DateTime,data_df_df$Global_active_power, type = "l", xlab="", ylab="Global Active Power (kilowatts)")
dev.off()
