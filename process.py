#opening the server txt file
log_file = open("um-server-01.txt")

#function sales_reports with the paramater
def sales_reports(log_file):
    #for loop
    for line in log_file:
        #removes whitespace
        line = line.rstrip()
        #pulls first 3 items from the 0 index
        day = line[0:3]
        #pulls all the data from a specific day
        if day == "Mon":
            #logs the line data in your terminal
            print(line)

#invocation of previous function
sales_reports(log_file)
