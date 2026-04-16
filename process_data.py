import csv

# define file paths
in_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]
out_file = "data/formatted_sales.csv"

# set up final list with headers
output = [["sales", "date", "region"]]

# loop through each csv
for file in in_files:
    with open(file, "r") as f:
        reader = csv.reader(f)
        
        # skip the header row
        next(reader) 
        
        # read row by row
        for row in reader:
            product = row[0]
            
            # keep only pink morsels
            if product == "pink morsel":
                
                # strip $ and convert to decimal
                raw_price = row[1].replace("$", "")
                price = float(raw_price)
                
                # get quantity and multiply
                qty = int(row[2])
                sales = price * qty
                
                # grab date and region
                date = row[3]
                region = row[4]
                
                # add clean row to final list
                output.append([sales, date, region])

# write everything to a new csv
with open(out_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)
    
print("done!")