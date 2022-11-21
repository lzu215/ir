# INFO300.Exercise 1
Date: Aug. 31, 2022

## Instructor:

+ Xia Lin, xlin@drexel.edu
+ Sue Wei, suwei@lzu.edu.cn


# Boolean Retrieval

Given the Data Set:  Courses for Drexel-Lanzhou Program:

```
D1={Introduction, information, systems}
D2={Introduction, Data, Science}
D3={Advanced, Mathematics, I}
D4={Advanced, Mathematics, II}
D5={Introduction, Computing, Security, Technology}
D6={Web, Systems, Technology, Service}
D7={Computing, information, design, I}
D8={Computing, Information, design, II}
D9= {information, retrieval, systems}
D10={computer programming}
```
#### FInd the Solution:


1.	(D1 AND D7 AND D9) = {information}

2.	((D1 AND D7) or D9) = {information, retrieval, systems}

3.	(D1 AND (D7 or D9) =  {information, systems}

4. If query=(computing or data or information), the retrieved set ={D5, D7, D8, D2, D1, D9}

5. If query=(information AND systems) the retrieved set={D1, D9}

6. If query=((introduction or I) NOT information) the retrieved set= {D2, D3, D5}
