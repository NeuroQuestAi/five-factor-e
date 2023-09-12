<img src="https://raw.githubusercontent.com/NeuroQuestAi/neuroquestai.github.io/main/brand/logo/neuroquest-orange-logo.png" align="right" width="80" height="80"/>

### About data 📊

The data directory contains the artifacts used for the [IPIP-NEO](https://ipip.ori.org/) used by this library, in the short version with **120** items and the long version with **300** items.

If you are thinking of using this library in your project, you should follow the standard question and answer files proposed in examples [120](https://github.com/NeuroQuestAi/five-factor-e/blob/main/data/IPIP-NEO/120/answers.json) and [300](https://github.com/NeuroQuestAi/five-factor-e/blob/main/data/IPIP-NEO/300/answers.json).

The translations of the questions are in the [translation](https://github.com/NeuroQuestAi/five-factor-e/tree/main/data/IPIP-NEO/120/translation) folder, as the translations happen, we will attach them to this directory. If you want to send a translation that is not in the repository, feel free to contribute with us following the [json file pattern](https://github.com/NeuroQuestAi/five-factor-e/blob/main/data/IPIP-NEO/120/translation/questions-en-us.json).

### Experiments with reverse scoring questions ⚡

If you want to test and experiment with questions with the reverse order, you need to use the [example json file](https://github.com/NeuroQuestAi/five-factor-e/blob/main/data/IPIP-NEO/120/test/answers-1.json). Answers that have the key (reverse_scored = *1*) will have the reverse score ie: The value selected was *5*, it will be turned into *1*. You can read more about it here:

 * [https://ipip.ori.org/newScoringInstructions.htm](https://ipip.ori.org/newScoringInstructions.htm)
 * [https://ipip.ori.org/newMultipleconstructs.htm](https://ipip.ori.org/newMultipleconstructs.htm)
 * [https://ipip.ori.org/Finding_Scales_to_Measure_Particular_Constructs.htm](https://ipip.ori.org/Finding_Scales_to_Measure_Particular_Constructs.htm)

```json
{
   "answers":[
      {
         "id_question":1,
         "id_select":5,
         "reverse_scored":1
      },
      {
         "id_question":2,
         "id_select":2,
         "reverse_scored":0
      }
    ]
}
```

Example loading json response file locally:

```python
import json

with open("my-test-answers.json", "r") as f:
  answers120 = json.load(f)
```

For the test, we must start the constructor with the test variable turned on:

```python
from ipipneo import IpipNeo

IpipNeo(question=120, test=True).compute(sex="M", age=40, answers=answers120, compare=True)
```

If you have any questions, please send us an email to: (**e at NeuroQuest.ai**) or create an issue reporting the question of the problem in the repository of this project (https://github.com/NeuroQuestAi/five-factor-e/issues).

Thanks!
