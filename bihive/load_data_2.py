__author__ = 'Tamby Kaghdo'

"""
load_data.py: this script is used to load sample data into a sqlite db
"""

import sqlite3
import sys


def create_table(ddl):
    status = None
    try:
        conn = sqlite3.connect("C:\\workspace\\DataScience\\bihive\data\\advworks.db")
        conn.execute(ddl).fetchall()
        status = 0
    except:
        print(sys.stderr,"Unable to create table")
        status = 1

    conn.close()

    return status

def bulk_load_data(input_file):
    count_columns(input_file)
    fileHandle = open(input_file, 'r')
    i = 0
    for line in fileHandle:
        fields = line.split('|')
        #remove BOM
        if i == 0:
            fields[0] = list(fields[0])
            fields[0] = fields[0][2:len(fields[0])]
            fields[0] = ''.join(fields[0])
        print(fields[0])
        i += 1
    fileHandle.close()


def count_columns(input_file):
    column_count = None
    fileHandle = open(input_file, 'r')
    i = 0
    for line in fileHandle:
        fields = line.split('|')
        if i == 0:
            column_count = len(fields)
            break

    fileHandle.close()

    return column_count

def column_names(input_file):
    column_names = []
    fileHandle = open(input_file, 'r')
    i = 0
    for line in fileHandle:
        fields = line.split('|')
        if i == 0:
            break

    fileHandle.close()

def main():
    dim_date_ddl = "CREATE TABLE DimDate(DateKey INTEGER NOT NULL, FullDateAlternateKey TEXT NOT NULL, DayNumberOfWeek INTEGER NOT NULL, EnglishDayNameOfWeek TEXT NOT NULL, SpanishDayNameOfWeek TEXT NOT NULL, FrenchDayNameOfWeek TEXT NOT NULL, DayNumberOfMonth INTEGER NOT NULL, DayNumberOfYear INTEGER NOT NULL, WeekNumberOfYear INTEGER NOT NULL, EnglishMonthName TEXT NOT NULL, SpanishMonthName TEXT NOT NULL, FrenchMonthName TEXT NOT NULL, MonthNumberOfYear INTEGER NOT NULL, CalendarQuarter INTEGER NOT NULL, CalendarYear INTEGER NOT NULL, CalendarSemester INTEGER NOT NULL, FiscalQuarter INTEGER NOT NULL, FiscalYear INTEGER NOT NULL, FiscalSemester INTEGER NOT NULL)"
    fact_call_center_ddl = "CREATE TABLE FactCallCenter(FactCallCenterID INTEGER NOT NULL, DateKey INTEGER NOT NULL, WageType TEXT NOT NULL, Shift TEXT NOT NULL, LevelOneOperators INTEGER NOT NULL, LevelTwoOperators INTEGER NOT NULL, TotalOperators INTEGER NOT NULL, Calls INTEGER NOT NULL, AutomaticResponses INTEGER NOT NULL, Orders INTEGER NOT NULL, IssuesRaised INTEGER NOT NULL, AverageTimePerIssue INTEGER NOT NULL, ServiceGrade REAL NOT NULL)"

    #create_table(dim_date_ddl)
    #create_table(fact_call_center_ddl)

    dim_date_file_location = "C:\\workspace\\DataScience\\bihive\data\\AdventureWorksSQLDW2012\\DimDate.txt"
    bulk_load_data(dim_date_file_location)


if __name__ == "__main__":
    # call main
    sys.exit(0 if main() else 1)