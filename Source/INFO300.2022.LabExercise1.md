# INFO300.LabExercise 1
Date: September 2, 2022

Goals: Learn to start working wiht ElasticSearch and be able to run simple queries and add documents to ElasticSearch.

Grading:  You name must become searchable in the collection "info300_students".

## 1. Working with ElasticSearch through Kibana

+ Logon to Kibana and open the "Dev Tools"
+ RUn the following query:
```
GET /info300_students/_search
{
  "query": {
    "match_all": {}
  }
}
```
+ Observe the query results on the right.
+ Currently, How many results are returned from this query:
+ "His Total =  ____"

## 2. Adding your name to the collection by running a similiar query like this:
```
POST /info300_students/_doc/
{
  "studentID": "2020030405",
  "name":"Jielun Zhou",
  "class": "Data Science 2020",
  "from": "Fujian",
  "favor_food":"Orange Beef",
  "favor_fruit":"Apple",
  "favor_university":"Drexel",
  "interest":["reading", "traveling", "programming", "Information retrieval", "visualization", "information visualization"]
}
```
Requirements:
+ If you do it successfully, your name should become searchable.
+ You should enter one item each for your "favor food", "favor fruit", and favor favor_university".
+ Enter at least three items in the "interest" array.

## 3. Running a similiar query to verify your name is there:
```
GET /info300_students/_search
{
  "query": {
    "match": {
      "name": "Jielun Zhou"
    }
  }
}
```
## 4. Adding another document using "PUT":
```
PUT /info300_students/_doc/jzhou101
{
  "studentID": "jzhou101",
  "name":"周杰伦",
  "class": "Lanzhou2019",
  "from": "Fujian",
  "favor_food":"Beef",
  "favor_fruit":"Orange",
  "favor_university":"Lanzhou University",
  "interest":["reading", "traveling", "programming", "Information retrieval", "visualization", "information visualization"]
}
```
Requirements:
+ Make sure to use your studentID as the documentID on the command!
+ Enter your Chinese name this time.
+ You should modify some of your favorite items there.
+ Run a query to make sure your entry is there.

## 5. Now you have complete the first try of using ElasticSearch. Explore the dpcumentation of ElasticSearch to see what other queries you can run on this info300_students collection.

+
Introduction to ElasticSearch:
https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro.html

+ Don't need to submit any paper for this exercise. But your names must be searchable in this collection to receive the grade.
