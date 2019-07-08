#Program to Crawl Data from Google Plus API  via API key Start
import os
import json
from googleapiclient.discovery import build
import hashlib
import pymongo
from pymongo.mongo_client import MongoClient
if __name__ == '__main__':
 api_key="AIzaSyDpa8u_lmjGGwj5pQCsKbAybtKctuDPGmw"
 service=build('plus','v1',developerKey=api_key)
 print("GooglePlus Data crawling started .....")
#Searching people having display name containg "Gandhi"
 people_feed=service.people()
 search_query_people=people_feed.search(query='Gandhi')
 search_result=search_query_people.execute()
 #print(json.dumps(search_result,indent=4))

#Searching  activity "Cricket"
activity_feed=service.activities()
search_query_activity=activity_feed.search(query='cricket',orderBy='best').execute()
#print(json.dumps(search_query_activity,indent=4))

# Group people based of particular activity
request = people_feed.listByActivity(
  activityId='z12pgvxbtuurubpka23ewxbb5tyoenawu04',
  maxResults='2').execute()


#Get an activity based on activity id
search_query_activity_by_id=activity_feed.get(activityId='z12pgvxbtuurubpka23ewxbb5tyoenawu04').execute()
#print(json.dumps(search_query_activity_by_id,indent=4))

#Get comments of a particular activity
comment_feed=service.comments()
search_query_comments=comment_feed.list(activityId='z12pgvxbtuurubpka23ewxbb5tyoenawu04').execute()
#comments=(json.dumps(search_query_comments,indent=4))

#Program to Crawl Data from Google Plus API  via API key Start
#Insertion in Local Mongo DB
#webscience is the Mongo DB being used to store the Google Plus API Crawled Data via API key
MONGO_HOST= 'mongodb://localhost/webscience'
client=MongoClient(MONGO_HOST)
db=client.webscience
db.googleplus_search.insert(search_result)
db.googleplus_search.insert(request)
db.googleplus_search.insert(search_query_activity)
db.googleplus_search.insert(search_query_activity_by_id)
db.googleplus_search.insert(search_query_comments)

print("GooglePlus Data crawling completed and inserted in the Mongo DB")