# INFO300.LabExercise 3 Part Two
Date: September 13, 2022

Student: _________   Email:_______

Goals: Practice with ElasticSearch single document APIs

+ Submit a Makedown file named "Week3Lab-2.yourName.md" and a PDF file named "Week3Lab-2.yourName.pdf" 
 ( you may use this file as a template ) 

Notes:
+ Use your email ID to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.

## Working with ElasticSearch single document APIs

###  1). POST vs. PUT

Run the Command:
```json
POST /suwei_posttest1/_doc
{
  "t1":"abc"
}
```
Your Response:
```json

```

Run the Command:
```json
PUT /suwei_puttest1/_doc
{
  "t1":"abc"
}
```
+ Why there is an error?
+ Your Answer:
```text

```
Run the Command:
```json
PUT /suwei_puttest1/_doc/1
{
  "t1":"abc"
}
```
Your Response:
```json

```

Run the Command:
```json
PUT /suwei_puttest1/_create/2
{
  "t2":"nbc"
}
```
Your Response:
```json

```
Run the Command:
```json
POST /suwei_posttest1/_create/2
{
  "t2":"nbc"
}
```
Your Response:
```json

```

### 2). GET and HEAD


Run the Command:
```json
GET /suwei_puttest1/_doc/2
```
Your Response:
```json

```
Run the Command:
```json
HEAD /suwei_puttest1/_doc/2
```
Your Response:
```json

```

Run the Command:
```json
GET /suwei_puttest1/_source/2
```
Your Response:
```json

```

Run the Command:
```json
HEAD /suwei_puttest1/_source/1234
```
Your Response:
```json

```
+ What's meaning of 404?
+ Your Answer:
```text

```

### 3). Delete

Run the Command:
```json
DELETE /suwei_puttest1/_doc/2 
```
Your Response:
```json

```

Run the Command:
```json
POST /suwei_posttest1/_delete_by_query
{
  "query":{
    "match":{
      "t2":"nbc"
    }
  }
}
```
Your Response:
```json

```

Run the Command:
```json
POST suwei_puttest1,suwei_posttest2/_delete_by_query
{
  "query":{
    "match_all":{}
  }
}
```
Your Response:
```json

```
+ Are there any documents in the index "suwei_puttest1"? Does the index "suwei_puttest1" still exist?
+ Your Answer:
```text

```

### 4). Update

Run the Command:
```json
PUT /suwei_test3/_doc/1
{
  "Ntest":1,
  "date":["2021-11-04"]
}

POST /suwei_test3/_update/1
{
  "script":{
    "source": "ctx._source.Ntest+=params.aa",
    "lang": "painless", 
    "params":{
      "aa":3
    }
  }
}
```
Your Response:
```json

```
+ What's the value of "Ntest" now?
+ Your Answer:
```text

```

Run the Command:
```json
POST /suwei_test3/_update/1
{
  "script":{
    "source": "ctx._source.date.add(params.dt)",
    "lang": "painless", 
    "params":{
      "dt":"2021-11-05"
    }
  }
}
```
Your Response:
```json

```
Write a query to see the document content of index "suwei_test3"

Your Command:
```json

```
Your Response:
```json

```
