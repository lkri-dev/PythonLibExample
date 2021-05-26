# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from ipaddress import IPv4Address
import pymysql.cursors

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('CSV.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            try:  # try statement is for the csv field, so it won't get parsed to IPv4Address
                if IPv4Address(row[0]) == IPv4Address("220.45.0.17"):
                    # print(type(row[0])) #remeber you can check the type of a value.
                    IPv4 = IPv4Address(row[0])
            except ValueError:  # the exception is to continue with the loop
                print("Error")  # you cna print the ValueError to print what it is
                continue

        if IPv4 is not None:  # printing out the IP if it was found
            print(IPv4)
        else:
            print("could not find IP address")
