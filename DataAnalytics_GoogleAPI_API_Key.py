#Program to show Data Analytics of Google API Crawled Data  via  REST API start
import matplotlib.pyplot as plt
import numpy as np
import pymongo
from pymongo.mongo_client import MongoClient
#Mongo DB Details
MONGO_HOST= 'mongodb://localhost/webscience'
client=MongoClient(MONGO_HOST)
db=client.webscience
print ("---------Start of Google Plus Data Analytics------------")
#Total data collected
total_data=db.googleplus_search.count()
print ("Total data from Google Plus based on ObjectId:",total_data)
#Count of People
search_result_count=db.googleplus_search.find({"kind":"plus#peopleFeed"}).count()
print ("Total Count of People:",search_result_count)
# Group people based of particular activity
#Count of Activity
search_activity_count_plus=db.googleplus_search.find({"kind":"plus#activity"}).count()
print ("Total Count of Activities:",search_activity_count_plus)
#Count of Activity based on activity id
search_query_activity_by_id=db.googleplus_search.find({"id":"z12pgvxbtuurubpka23ewxbb5tyoenawu04"}).count()
print ("Total Count of Activies based on activity id:",search_query_activity_by_id)
#Count of comments
comments_count=db.googleplus_search.find({"kind":"plus#commentFeed"}).count()
print ("Total Count of Comments from GooglePlus",comments_count)
print ("---------End of Google Plus Data Analytics------------")
#Program to show Data Analytics of Google API Crawled Data  via  REST API end

#Saving the Data Analytics Result to GoogleAPI_DataAnalytics.txt
google_plus_data=[search_result_count,search_activity_count_plus,search_query_activity_by_id,comments_count]
f = open(r'C:\Users\SOUMITA\PycharmProjects\Webscience_CourseWork_Final\GoogleAPI_DataAnalytics.txt','w')
f.write('---------Start of Google Plus Data Analytics------------\n')
f.write("Total Count of People:")
f.write(repr(google_plus_data[0]))
f.write("\n")
f.write("Total Count of Activities:")
f.write(repr(google_plus_data[1]))
f.write("\n")
f.write("Total Count of Activies based on activity id:")
f.write(repr(google_plus_data[2]))
f.write("\n")
f.write("Total Count of Comments from GooglePlus")
f.write(repr(google_plus_data[3]))
f.write("\n")
f.write('---------End of Google Plus Data Analytics------------')
f.close()

#Google API total data collected based on Mongo DB Data Start

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlabel("Features of Google API")  # x-axis label
ax.set_ylabel("Counts of Features")        # y-axis label
ax.set_title("Features Vs Counts Crawled and Stored in Mongo DB ")
x=['People','Activity','Comments']
y=[search_result_count,search_activity_count_plus,comments_count]
ax.bar(x,y)
plt.show()

#Google API total data collected based on Mongo DB Data End