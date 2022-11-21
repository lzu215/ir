# INFO300.LabExercise 4
Date: September 23, 2022

Student: __________  Email: __________

+ Goals: Practice with ElasticSearch Analyzer 


+ Submit a Makedown and a PDF file named "Week4Lab1-yourName" 
 ( you may use this file as a template ) 


### 1). Given the following text, use "whitespace", "standard", "english" Analyzer to analyze the text.

+ text: "Lanzhou University now hosts 45 first-level disciplines authorized to confer master’s degree."

+ command example:
```json
POST _analyze
{
  "analyzer":"",
  "text": ""
}
```
Your Command 1:
```json

```

Your Command 2:
```json

```

Your Command 3:
```json

```

Write the terms under the three analyzers:

+ whitespace:
```text

```

+ standard: 
```text

```
+ english: 
```text

```

### 2). Create an index of "yourEmailID_books" and customized Analyzer with the type of "standard", the max token length of "8", the stopword of "_english_".

Command example:
```json
PUT /suwei_books
{
 "settings": {
   "analysis": {
     "analyzer": {
       "yourEmailID":{
         "type":"",
         "max_token_length":"",
         "stopwords":""
       }
     }
   }
 }
}
```

Your Command 4:
```json

```

Use the Analyzer to analyze the text: "Lanzhou University now hosts 45 first-level disciplines authorized to confer master’s degree.".

Command example:
```json
POST /suwei_books/_analyze
{
  "analyzer":"",
  "text": ""
}
```

Your Command 5:
```json

```

Write all the terms under the new Analyzer:

+ yourEmailID:
```text

```

### 3). Create a new index with name "yourEmailID_analyzertest", Set the type of the field "title" to "text". Set the search time analyzer to "english" and the index time analyzer to "standard".

Command Example:
```json
PUT /suwei_analyzertest
{
  "mappings": {
   "properties": {
     "FieldName": {
       "type": "",
       "analyzer": "",
       "search_analyzer": ""
      }
    }
 }
}
```

Your Command 6:
```json


```

Index a document including a field "title" with the text: "Lanzhou University now hosts 45 first-level disciplines authorized to confer master’s degree.".

Command example:
```json
PUT /suwei_analyzertest/_doc/1
{
  "title": ""
}
```

Your Command 7:
```json

```

Write four queries to retrieval the following text:

+ "University"
+ "first to beijing"
+ "hosts master's student"

Your Command 7:
```json

```
Response 7:
```json
{

}
```

Your Command 8:
```json

```

Response 8:
```json
{

}
```

Your Command 9:
```json

```
Response 9:
```json
{

}
```

Give a short descrition why there IS or IS NO hit for each query.

Your Answer:
* "University":
```text

```

* "first to beijing":
```text

```
* "hosts master's student":
```text

```