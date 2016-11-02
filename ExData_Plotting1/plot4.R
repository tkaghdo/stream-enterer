library(dplyr)

#import the file
data_df_df = read.table("household_power_consumption.txt",sep=";", na.strings = "?", header=TRUE)

#pull the date range
data_df_df <- data_df_df[(data_df_df$Date=="1/2/2007" | data_df_df$Date=="2/2/2007"),]
# add the datetime variable to the data
data_df_df$DateTime <- strptime(paste(data_df_df$Date, data_df_df$Time, sep=" "), format="%d/%m/%Y %H:%M:%S")

#plot the data
png("plot4.png", width=480, height=480)
par(mfrow=c(2, 2))

plot(data_df$DateTime, data_df$Global_active_power, type="l", xlab="", ylab="Global Active Power")
plot(data_df_df$DateTime, data_df$Voltage, type="l", xlab="datetime", ylab="Voltage")
plot(data_df$DateTime, data_df$Sub_metering_1, type="l", xlab="", ylab="Energy sub metering")
lines(data_df$DateTime, data_df$Sub_metering_2, col="red")
lines(data_df$DateTime, data_df$Sub_metering_3, col="blue")
legend("topright", bty="n", lty=1, col=c("black", "red", "blue"), legend=c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))
plot(data_df$DateTime, data_df$Global_reactive_power, type="l", xlab="datetime", ylab="Global_reactive_Power")
dev.off()

