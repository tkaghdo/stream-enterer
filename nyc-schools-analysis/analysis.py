__author__ = 'Tamby Kaghdo'

import pandas as pd
import re
import numpy
import matplotlib.pyplot as plt

def find_lat(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

def find_lon(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

#pad '0'
def pad_csd(num):
    st = str(num)
    if len(st) > 1:
        return st
    else:
        return "0" + st

def first_2(s):
    return s[0:2]

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}
for f in data_files:
    d = pd.read_csv("./schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

#read comma delimited files
for k in data:
    print("*** Data Frame: {0}".format(k))
    print(data[k].head(5))

#read survey data (tab delimited)
all_survey = pd.read_csv("./schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("./schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")

#combine the survey data
survey = pd.concat([all_survey, d75_survey], axis=0)
print(survey.head(5))

#cleanup the survey dataframe
survey["DBN"] = survey["dbn"]
survey["DBN"] = survey["dbn"]

survey_fields = ["DBN","rr_s","rr_t","rr_p","N_s","N_t","N_p","saf_p_11","com_p_11"
    ,"eng_p_11","aca_p_11","saf_t_11","com_t_11",
    "eng_t_11",
    "aca_t_11",
    "saf_s_11",
    "com_s_11",
    "eng_s_11",
    "aca_s_11",
    "saf_tot_11",
    "com_tot_11",
    "eng_tot_11",
    "aca_tot_11",
]
survey = survey.loc[:,survey_fields]
data["survey"] = survey

print(survey.head())

#add surfey df to data dict
data["survey"] = survey

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]


#create DBN code
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())

#add the numbers for the sat categoris into one field
data["sat_results"]["SAT Math Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Math Avg. Score"],errors="coerce")
data["sat_results"]["SAT Critical Reading Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"],errors="coerce")
data["sat_results"]["SAT Writing Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Writing Avg. Score"],errors="coerce")
data["sat_results"]["sat_score"] = data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]
print(data["sat_results"]["sat_score"].head(5))

#get hs locations
data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)
data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")

#Condensing Class Size df
class_size = data["class_size"]
#only high school
class_size = class_size[class_size["GRADE "] == "09-12"]
#only GEN ED
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size.head(5))

#Find the average values for each column for each DBN in class_size
class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
print(data["class_size"].head(5))

#Condensing Demographics
data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head(5))

#Condensing Graduation
data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
print(data["graduation"].head())

#Converting AP Test Scores to numeric
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for c in cols:
    data["ap_2010"][c] = pd.to_numeric(data["ap_2010"][c],errors="coerce")

print(data["ap_2010"].head(5))

#join data frames
combined = data["sat_results"]
combined = combined.merge(data["ap_2010"], how="left", on="DBN")
combined = combined.merge(data["graduation"], how="left", on="DBN")
combined = combined.merge(data["class_size"], how="inner", on="DBN")
combined = combined.merge(data["demographics"], how="inner", on="DBN")
combined = combined.merge(data["survey"], how="inner", on="DBN")
combined = combined.merge(data["hs_directory"], how="inner", on="DBN")
print(combined.head(5))
print(combined.shape)

#fill in na
means = combined.mean()
combined = combined.fillna(means)
combined = combined.fillna(0)
print(combined.head(5))


#add school districts to df
combined["school_dist"] = combined["DBN"].apply(first_2)
print(combined["school_dist"].head(5))

#find correlations with sat_score
correlations = combined.corr()
correlations = correlations["sat_score"]
print(correlations)

#plot total_enrollment with sat_score; they are highly positively correlated
combined.plot.scatter(x="total_enrollment", y="sat_score")
plt.show()

#Exploring Schools With Low SAT Scores And Enrollment
low_enrollment = combined[combined["total_enrollment"] < 1000]
low_enrollment = low_enrollment[low_enrollment["sat_score"] < 1000]
print(low_enrollment)

#Plotting Language Learning Percentage
combined.plot.scatter(x="ell_percent", y="sat_score")
plt.show()

#map schools
'''
from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True)
plt.show()

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=combined["ell_percent"], cmap="summer")
plt.show()
'''
#Calculating District Level Statistics
districts = combined.groupby("school_dist").agg(numpy.mean)
districts.reset_index(inplace=True)
print(districts.head())

#Plotting Ell_percent By District
'''
from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = districts["lon"].tolist()
latitudes = districts["lat"].tolist()
m.scatter(longitudes, latitudes, s=50, zorder=2, latlon=True, c=districts["ell_percent"], cmap="summer")
plt.show()
'''
