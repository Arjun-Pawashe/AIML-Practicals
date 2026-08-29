# Car Fault Diagnostic Expert System (Prolog)

## Overview
A small **rule-based expert system** implemented in Prolog that interactively asks the user yes/no questions about car symptoms and, using **backward-chaining inference**, reports the most likely fault.

## Problem Statement
Design and implement a simple expert (diagnostic) system in Prolog that interacts with a user through yes/no questions to identify the likely cause of a car's starting/running problem (e.g. dead battery, faulty starter motor, fuel starvation, ignition misfire) using backward-chaining rule-based reasoning.

## Files
| File | Description |
|---|---|
| `auto.pl` | Prolog source code implementing the diagnostic system |
| `README.md` | This file |
| `sample_input_output.txt` | Sample console sessions (multiple test cases) |

## How It Works
- **Knowledge base:** a set of ordered `diagnose/0` rules, each representing an if-symptom(s)-then-conclusion production rule.
- **Fact acquisition (`ask/1`):** since symptom facts aren't known in advance, the system queries the user directly via `format/2` and `read/1`, succeeding only if the answer is `y`.
- **Inference:** Prolog's own backward chaining tries each `diagnose/0` clause in order, asking only the questions needed for that rule.
- **Cut (`!`):** once a rule's conditions are satisfied, the cut commits Prolog to that diagnosis and prevents backtracking into the remaining, more general rules.
- **Default case:** if no specific rule matches, the system falls through to a final clause advising the user to consult a mechanic.

## Requirements
- [SWI-Prolog](https://www.swi-prolog.org/) (or any standard Prolog with `format/2`, `read/1`, `writeln/1`)

## How to Run
```prolog
?- [auto].
?- start.
```
Answer each prompt with `y.` or `n.` (including the trailing period).

## Sample Output
```
?- start.
--- CAR DIAGNOSTIC SYSTEM ---
Answer with y. or n.

Does the car fail to start? (y/n): |: y.
Does the engine refuse to crank? (y/n): |: y.

-> RESULT: Dead or weak battery.
true.
```

See `sample_input_output.txt` for additional test cases (faulty starter motor, and an inconclusive case).

## Author
[Your Name]
