# INFO300.LabExercise 3 Part One
Date: September 13, 2022

Student: ___Wenbo Liu___  Email: ___wbliu20@lzu.edu.cn___

+ Goals: Practice with ElasticSearch Mapping


+ Submit a Makedown file named "Week3Lab-1.yourName.md" and a PDF file named "Week3Lab-1.yourName.pdf" 
 ( you may use this file as a template ) 

## 1. Working with ElasticSearch Mapping


### 1). Create an index with a name of "yourEmailID_course", put a document including four fields into the index. 
  + "course_name": "Machine Learning"
  + "credit":3
  + "start_date":"2022/08/30"
  + "score":"75"

Your command 1:
```json

```

Response 1:
```json
{

}
```
### 2). Write a command to get the mapping of your index and answer the following questions:

Your command 2:
```json

```

Response 2:
```json
{

}
```

+ What are data types of the following fields:
  + "course_name":_________
  + "credit":_______
  + "start_date":_________
  + "score":_______


### 3). Delete the above index 

Your command 3:
```json

```

Response 3:
```json
{

}
```

### 4). Re-create the index of "yourEmailID_course", Create a mapping for the index with the following data type.

  + "course_name": keyword
  + "credit": integer
  + "start_date":date
  + "score":float

Your command 4:
```json

```

Response 4:
```json
{

}
```

### 5). After you have properly configured the mappings for your index, load a document data to the index with PUT command.

Your command 5:
```json

```

Response 5:
```json
{

}
```

### 6). Looking up mapping records for the index of "info300_publications" and "news" 

Your command 6:
```json


```