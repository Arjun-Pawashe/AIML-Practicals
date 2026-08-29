# Vacuum Cleaner World Agent (Prolog)

## Overview
A **model-based reflex agent** implemented in Prolog that autonomously cleans a small world of interconnected rooms (`a`, `b`, `c`). The agent perceives its current location and the dirt status of the environment, then uses a rule-based inference engine to decide whether to **clean**, **move**, or **stop**.

## Problem Statement
Design and implement an intelligent vacuum-cleaning agent in Prolog that operates in a world of interconnected rooms, some of which may be dirty. The agent must perceive the state of its current room and its neighbouring rooms, and use a rule-based inference engine to decide whether to clean the current room, move to an adjacent dirty room, or stop when the entire environment is clean.

## Files
| File | Description |
|---|---|
| `vacuum_agent.pl` | Prolog source code implementing the agent |
| `README.md` | This file |
| `sample_input_output.txt` | Sample console sessions (multiple test cases) |

## How It Works
- **Environment representation:** `room/1` and `adjacent/2` are static facts describing the rooms and how they connect.
- **World state:** `dirty/1` and `vacuum_location/1` are declared `:- dynamic` so they can be updated at run time.
- **Inference engine (`action/1`):** three rules decide the next action —
  1. If the current room is dirty → `clean`.
  2. Else, if an adjacent room is dirty → `move(ToRoom)`.
  3. Else, if no room anywhere is dirty → `stop`.
- **Execution (`perform/1`):** carries out the chosen action, updating the world with `assertz`/`retract` and printing a status message.
- **Control loop (`start/0`):** recursively repeats perceive → decide → act until the agent stops.

## Requirements
- [SWI-Prolog](https://www.swi-prolog.org/) (or any standard Prolog with `format/2`, `dynamic/1`, `assertz/1`, `retract/1`)

## How to Run
```prolog
?- [vacuum_agent].
?- start.
```

## Sample Output
```
?- start.
Vacuum cleaned room a.
Vacuum moved to room b.
Vacuum cleaned room b.
All rooms are clean. Stopping...
true.
```

See `sample_input_output.txt` for additional test cases (an already-clean world, and dirt in a non-adjacent room).

## Author
[Your Name]
