# INFO300.LabExercise 5--Similarity
Date: September 30, 2022

Student: _________   Email:_______

Goals: Practice with ElasticSearch Similarity

Notes:
+ Use your email ID to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.
+ Please submit both MD and PDF files named "Week5Lab.yourName".

##  1). BM25 and boolean Similarity

Run the Command:
```json
PUT /suwei_simitest
{
  "mappings":{
    "properties": {
      "f1":{
        "type": "text"
      },
      "f2":{
        "type":"text",
        "similarity": "boolean"
      }
    }
  }
}
```
Your Response:
```json

```
+ Q1: What's the similarity function of field "f1" and "f2"?
+ Your Answer:
```text

```

Run the Command:

```json
POST /suwei_simitest/_doc/1
{
  "f1":"Beijing Beijing Shanghai",
  "f2":"Lanzhou Lanzhou"
}
```
Your Response:
```json

```
Run the Command:
```json
POST /suwei_simitest/_doc/2
{
   "f1":"Beijing Tianjin",
   "f2":"Lanzhou Lanzhou Tianjin"
}
```
Your Response:
```json

```
Run the Command:
```json
POST /suwei_simitest/_doc/3
{
   "f1":"Beijing Beijing Lanzhou Tianjin",
   "f2":"Lanzhou Shanghai Tianjin"
}
```
Your Response:
```json

```
Run the Command:
```json
GET /suwei_simitest/_search
{
  "query": {
    "multi_match" : {
      "query": "Beijing",
      "fields": ["f1"]
    }
  }
}
```
Your Response:
```json

```
+ Q2: What's the sequence of retrieved documents？ What's the score of each retrieved document?
+ Your Answer:
```text

```
Run the Command:
```json
GET /suwei_simitest/_search
{
  "query": {
    "multi_match" : {
      "query":    "Lanzhou",
      "fields": ["f2"]
    }
  }
}
```
Your Response:
```json

```
+ Q3: What's the sequence of retrieved documents？ What's the score of each retrieved document?
+ Your Answer:
```text

```

Run the Command:
```json
GET /suwei_simitest/_search?explain=true
{
  "query": {
    "multi_match" : {
      "query": "Beijing",
      "fields": ["f1"]
    }
  }
}
```
Your Response:
```json

```
+ Q4: Please give the formula for computing the similarity score. Please write down the values of each parameter and variable for Document “3”.
+ Your Answer:
```text

```

Run the Command:
```json
GET /suwei_simitest/_search?explain=true
{
  "query": {
    "multi_match" : {
      "query":    "Lanzhou",
      "fields": ["f2"]
    }
  }
}
```
Your Response:
```json

```

##  2). DFR as Default Similarity

Run the Command:
```json
GET /suwei_simitest/_mapping
```
Your Response:
```json

```

Run the Command:
```json
POST /suwei_simitest/_close?wait_for_active_shards=0
```
Your Response:
```json

```
Run the Command:
```json
PUT /suwei_simitest/_settings
{
  "index": {
    "similarity": {
      "default": {
        "type": "DFR",
        "basic_model": "g",
        "after_effect": "l",
        "normalization": "h2",
        "normalization.h2.c": "3.0"
      }
    }
  }
}
```
Your Response:
```json

```
Run the Command:
```json
POST /suwei_simitest/_open
```
Your Response:
```json

```
Run the Command:
```json
GET /suwei_simitest/_search?explain=true
{
  "query": {
    "multi_match" : {
      "query": "Beijing",
      "fields": ["f1"]
    }
  }
}
```
Your Response:
```json

```

+ Q5: Look into the document of Elastic Search, please write out all the possible values of each parameter for DFR similarity.
+ Your Answer:
```text
 "basic_model": 
 "after_effect": 
 "normalization": 
```

##  3). DFI and IB Similarity

Run the Command:
```json
PUT /suwei_simitest1
{
  "settings":{
    "index": {
      "similarity":{
        "my_dfi":{
          "type":"DFI",
          "independence_measure":"standardized"
        },
        "my_ib":{
          "type":"IB",
          "distribution":"ll",
          "lambda":"df",
          "normalization":"h1"
        }
      }
    }  
  }
}
```
Your Response:
```json

```
Run the Command:
```json
PUT /suwei_simitest1/_mapping
{
  "properties":{
      "f1":{
        "type": "text", 
        "similarity":"my_dfi"
      },
      "f2":{
        "type":"text",
        "similarity": "my_ib"
      }
    }
}
```
Your Response:
```json

```
Run the Command:
```json
POST /suwei_simitest1/_doc/1
{
  "f1":"Beijing Lanzhou",
  "f2":"Lanzhou Lanzhou"
}

POST /suwei_simitest1/_doc/2
{
   "f1":"Beijing Beijing Tianjin",
   "f2":"Beijing Tianjin Tianjin"
}

POST /suwei_simitest1/_doc/3
{
   "f1":"Lanzhou Lanzhou Tianjin",
   "f2":"Lanzhou Tianjin Lanzhou"
}
```
Run the Command:
```json
GET /suwei_simitest1/_search?explain=true
{
  "query": {
    "multi_match" : {
      "query": "Beijing",
      "fields": ["f1"]
    }
  }
}
```
Your Response:
```json

```
Run the Command:
```json
GET /suwei_simitest1/_search?explain=true
{
  "query": {
    "multi_match" : {
      "query": "Lanzhou",
      "fields": ["f2"]
    }
  }
}
```
Your Response:
```json

```
##  4). Scripted Similarity
Run the Command:
```json
PUT /suwei_simitest_mytfidf/
{
  "settings": {
    "number_of_shards": 1,
    "similarity":{
      "su_tfidf":{
        "type":"scripted",
        "script":{
          "source":"double tf=Math.sqrt(doc.freq);double idf=Math.log((field.docCount+3.0)/(term.docFreq+2.0))+3.0;double norm=1/Math.sqrt(doc.length);return query.boost * tf * idf * norm;"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "books":{
        "type":"text",
        "similarity": "su_tfidf"
      }
    }
  }
}
```
Your Response:
```json

```