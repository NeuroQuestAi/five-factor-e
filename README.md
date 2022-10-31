# Five Factor E Library 📦

![version 1.0.0][img_version]
![python 3.7 | 3.8 | 3.9 | 3.10][python_version]
[![PyPI Downloads](https://img.shields.io/pypi/dm/five-factor-e.svg?label=PyPI%20downloads)](
https://pypi.org/project/five-factor-e/)

[img_version]: https://img.shields.io/static/v1.svg?label=version&message=1.0.0&color=blue
[python_version]: https://img.shields.io/static/v1.svg?label=python&message=3.7%20|%203.8%20|%203.9%20|%203.10%20&color=blue

<p align="center">
  <img src="https://raw.githubusercontent.com/neural7/five-factor-e/04ac3ce31e37f582e66ffdf694d4c4bcb8469ec9/doc/big-five.png" alt="Representation of the Big Five"/>
</p>

This project assesses a person's 🗣 personality based on an inventory of questions. The project uses the Big Five theory using the [IPIP-NEO-120](http://www.personal.psu.edu/~j5j/IPIP/ipipneo120.htm) and [IPIP-NEO-300](http://www.personal.psu.edu/~j5j/IPIP/ipipneo300.htm) model developed by Professor **Dr. John A. Johnson**, this is free representation of [NEO PI-R™](https://en.wikipedia.org/wiki/Revised_NEO_Personality_Inventory).

*"The IPIP-NEO is not identical to the original NEO PI-R, but in my opinion it is close enough to serve as a good substitute. More and more people are beginning to use it in published research, so its acceptance is growing."* - Dr. Johnson

The main idea of the project is to facilitate the use of **Python** developers who want to use **IPIP-NEO** in their projects. *The project is also done in pure Python, it doesn't have any dependencies on other libraries*.

Notes: *The project is based on the work of [Dhiru Kholia](https://github.com/kholia/IPIP-NEO-PI), and is an adaptation of Neural7 for a version that can be reused in other projects of the company.*

### Synopsis 🌐

A little theory, the The Big Five or Five Factor is made up of **5** great human personalities also known as the *O.C.E.A.N*. Are they:

 * Openness
 * Conscientiousness
 * Extraversion
 * Agreeableness
 * Neuroticism

To compose each great personality there are **6** traits or facets, totaling **30** traits. The user must answer a questionnaire of 120 or 300 single-choice questions. The user must answer an inventory of questions where each answer can have a unique and mandatory choice with **5** options:

* Very Inaccurate
* Moderately Inaccurate
* Neither Accurate Nor Inaccurate
* Moderately Accurate
* Very Accurate

For more information to demystify the Big Five, please see the article: [Measuring the Big Five Personality Domains](https://pages.uoregon.edu/sanjay/bigfive.html#norms)

### Installation 🚀

The simplest way is to use **PIP**, like the command:

```shell
$ pip install five-factor-e
```

### How to use 🔥

The answers must be in a standardized *json*, you can enter this template in the project folder [data](https://github.com/neural7/five-factor-e/blob/main/data/IPIP-NEO/120/answers.json). To calculate the Big Five use the code snippet below:

```python
from ipipneo import IpipNeo

IpipNeo(question=120).compute(sex=<>, age=<>, answers=JSON_STANDARD)
```

As an example you can load the project json to test.

```python
import json, urllib.request

data = urllib.request.urlopen("https://raw.githubusercontent.com/neural7/five-factor-e/main/data/IPIP-NEO/120/answers.json").read()
answers = json.loads(data)
```

Calculate the Big Five for a 40-year-old man:

```python
from ipipneo import IpipNeo

IpipNeo(question=120).compute(sex="M", age=40, answers=answers)
```

For a 25 year old woman:

```python
from ipipneo import IpipNeo

IpipNeo(question=120).compute(sex="F", age=25, answers=answers)
```

### Unit tests 🏗

Simply run the command below:

```shell
$ ./run-test
```

### About data 📊 

Inside the data [data](https://github.com/neural7/five-factor-e/blob/main/data/) directory, there are examples of questions and answers. The most important is the response data entry which must follow the pattern of this [file](https://github.com/neural7/five-factor-e/blob/main/data/IPIP-NEO/120/answers.json). Example:

```json
{
   "answers":[
      {
         "id_question":50,
         "id_select":5
      },
      {
         "id_question":80,
         "id_select":2
      }
   ]
}
```

Notes: *The order of answers does not affect the result.*

The id question field refers to the question in this [file](https://github.com/neural7/five-factor-e/blob/main/data/IPIP-NEO/120/questions-en-us.json). Obviously you may want to change the form of the questions, we are working on the English, Portuguese and Spanish translations.

### Credits 🏆

  * Dr John A. Johnson
  * Dhiru Kholia

### Resources 📗

  * https://github.com/kholia/IPIP-NEO-PI
  * http://www.personal.psu.edu/j5j/IPIP/ipipneo300.htm
  * http://www.personal.psu.edu/~j5j/IPIP/ipipneo120.htm
  * http://www.personal.psu.edu/faculty/j/5/j5j/
  * https://ipip.ori.org/
  * https://osf.io/tbmh5/

### Authors 👨‍💻

  * [Ederson Corbari](mailto:e@neural7.io)
  * [Marcos Ferretti](mailto:m@neural7.io)
