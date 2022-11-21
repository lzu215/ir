# INFO300.LabExercise 3 Part Three
Date: September 13, 2022

Student: _________   Email:_______

Goals: Practice with ElasticSearch multiple document APIs

+ Submit a Makedown file named "Week3Lab-3.yourName.md" and a PDF file named "Week3Lab-3.yourName.pdf" 
 ( you may use this file as a template ) 

Notes:

+ Use your email ID to replace "suwei".
+ Run the following command and write the response of each command.

## Working with ElasticSearch multiple document APIs

### 1). Mget

Run the Command:
```json
GET /news/_mget
{
  "docs":[
    {
      "_id":"PKB4iHwBaCKd_ZllMBuC"
    },
    {
      "_id":"QaB4iHwBaCKd_ZllMBuC"
    }
    ]
}
```
Your Response:
```json

```

Run the Command:
```json
GET /_mget
{
  "docs":[
    {
      "_index":"news",
      "_id":"R6B4iHwBaCKd_ZllMBuC"
    },
    {
      "_index":"suwei_test3",
      "_id":"1"
    }
    ]
}
```
Your Response:
```json

```

### 2). Bulk API
Run the Command:
```json
POST /_bulk
{"index":{"_index":"suwei_test3","_id":"3"}}
{"name":"tom","age":21}
{"update":{"_index":"suwei_test3","_id":"1"}}
{"doc":{"t2":"male"}}
{"index":{"_index":"suwei_test3","_id":"4"}}
{"name":"mike","age":23}
```
Your Response:
```json

```

### 3). Reindex API
Run the Command:
```json
POST /_reindex
{
  "source":{
    "index":"suwei_test3"
  },
  "dest": {
    "index":"suwei_test4"
  }
}
```
Your Response:
```json

```
