# INFO300.LabExercise 6--Scoring
Date: October 07, 2022

Student: _________   Email:_______

Goals: Practice with ElasticSearch Scoring

Notes:
+ Use your email ID to replace "suwei".
+ Run the following command and write the response of each command.
+ Answer the questions.

---

##  1). Upload the yelp data (business.json) to ES 

Note: 

+ The "location" field should set to "geo_point" data type. 

##  2). Script Score Query

### Step 1. Run the Command:

```json
GET /suwei_yelp/_mapping
```

What's the data type of the following field?

Your Answer:
```text
"name"：
"location":
"stars":
"review_count":
"city":
"state"
```
Run the following command:
```json
GET /suwei_yelp/_search
{
  "query":{
    "script_score":{
      "query":{
       "match":{
        "name":"Chinese"
      }
    },
      "script":{
        "source":"doc['stars'].value+doc['review_count'].value/10"
      }
    }
  }
}
```
Your Response:
```json

```

### Step 2. Write a command to search "Sushi" in the "name" field and rank the retrieved documents according to the following formula.

+ saturation(*review_count*,10)

Your Command
```json

```
Your Response:
```json

```

Calculate the score by yourself (You need to give the details of your calculation). Are they same with the result of ES?

Your Answer:
```text

```

Re-write a command to rank the retrieved documents according to the following formula.

+ sigmoid(*review_count*, 2, 1)+sigmoid(*stars*, 2, 3)

Your Command:
```json

```
Your Response:
```json

```
### Step 3. Write a command to search "Chinese" in the "name" field and rank the retrieved documents according to the following formula.

+ randomScore(12)

Your Command:
```json

```
Your Response:
```json

```
### Step 4. Write a command to search "Pittsburgh" in the "city" field and rank the retrieved documents according to the following formula.

+ decayGeoExp(params.origin, params.scale, params.offset, params.decay,*location*)

  Note: You can use the following parameters and values.
```text
    "origin":"40.4812,-80.1234",
    "scale":"40km",
    "offset":"0km",
    "decay" : 0.2
```
Your Command
```json

```
Your Response:
```json

```
Write down the "name", "location" and score of each retrieved document.
```text

```
---

##  3). Re-upload the yelp file to ES 

Note: The "stars" and "review_count" fields should set to "rank_feature" data type. Use another index name such as "suwei_yelp_rank".

##  4). Rank Feature Query
Note: You should use the new index "suwei_yelp_rank" for the following steps.

### Step 1. Run the Command:

```json
GET /suwei_yelp_rank/_mapping
```

Your Response:
```json

```
 Run the Command:
```json
GET /suwei_yelp_rank/_search
{
  "query":{
    "bool":{
      "must":{
        "match":{"city":"Pittsburgh"}
      },
      "should":{
        "rank_feature":{
          "field":"review_count"
        }
      }
    }
  }
}
```
Your Response:
```json

```

### Step 2. Write a command to search "Pittsburgh" in the "city" field and rank the retrieved documents by rank_feature (*review_count*) and *saturation* function (with the following parameter).

+ "pivot": 8

Your Command:
```json

```
Your Response:
```json

```

##  5). Design a new scoring algorithm. (Bonus point: 4)

The description of the new algorithm:
```text

```

Your Command:
```json

```

Your Response:
```json

```