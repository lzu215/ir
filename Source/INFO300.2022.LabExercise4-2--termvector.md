# INFO300.LabExercise 4-2--Term Vectors APIs
Date: September 23, 2022

Student: _________   Email:_______

Goals: Practice with ElasticSearch term vectors


+ Use your email ID to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.
+ Submit your MD and PDF file with the name of "Week4Lab2-yourname"


##  1). term vectors 1

Run the Command:
```json
GET /news/_termvectors/cR2484IBj2RRERLmeEc6?fields=headline
```

+ What's the value of doc_freq, ttf, and term_freq for the word "college" in the above result?
+ Your Answer:
```text
doc_freq:
ttf:
term_freq:
```


##  2). term_statistics and field_statistics
Run the Command (Please Only run the following  command ONCE):
```json
PUT /suwei_termtest/_doc/t1
{
  "books":"mike eat fish, mike eat rice",
  "paper":"fish eat fish"
}

PUT /suwei_termtest/_doc/t2
{
  "books":"I love fish, mike eat rice",
  "paper":"fish love fish"
}
```

Run the Command
```json
GET /suwei_termtest/_termvectors/t1
{
  "fields":["books"],
  "offsets":true,
  "positions":true,
  "term_statistics":true,
  "field_statistics":true
}
```
Your Response:
```json

```
+ The field_statistics should be 
> "sum_doc_freq" : 10,
> "doc_count" : 2,
> "sum_ttf" : 12

(If your result is not same with the above, please delete your index and rebuid it again. Make sure Only run the two commands once.)

+ What's the meaning of sum_doc_freq, doc_count and sum_ttf?
+ Your Answer:
```text

```

+ What's the value of doc_freq and ttf for the word "mike" and "fish"?
+ Your Answer:
```text

```
+ What's the meaning of doc_freq and ttf?
+ Your Answer:
```text

```

##  3). Dynamically generate term vectors
Run the Command:
```json
GET /suwei_termtest/_termvectors
{
  "doc":{
    "books":"mike love fish"
  },
  "term_statistics":true,
  "field_statistics":true,
  "positions":false
}
```
+ What's the value of doc_freq, ttf and term_freq for the word "mike" and "fish"?
+ Your Answer:
```text

```

Write a command to get the term_statistics and field_staticstics of your firstname and lastname in the index "info300_students".

Your Command:
```json

```
Your Response:
```json

```
