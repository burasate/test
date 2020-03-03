import csv

csv_data = []  #prepre list of data
root_path = '/workspace/sample/csv/' #Root Diractory
csv_file = 'F18Expression.csv' #File Name

#open csv checking if has csv file
try :
    csv_f = open(root_path + csv_file, 'r')
    csv_reader = csv.reader(csv_f,delimiter=',')
    for i in csv_reader :
        csv_data.append(i)
    csv_f.close()
#have no csv file
except :
    # HEADER SETUP
    header_list = [colA,colB,colC]
    csv_data.append(header_list)

#Action of Data
#--------------------------------------------------------------
#Write in New Row
new_row = [] #Append value of collum to this
#--------------------------------------------------------------

#Apply New Row
csv_data.append(new_row)

#Write CSV
csv_writer = open(root_path + csv_file, 'wb')  # Python2
with csv_writer :
    writer = csv.writer(csv_writer)
    writer.writerows(csv_data)
csv_writer.close()
