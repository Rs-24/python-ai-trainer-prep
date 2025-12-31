# python-ai-trainer-prep

This repository contains practice Python projects to prepare for remote **AI coding trainer / evaluator** roles (e.g. Scale, Outlier, and similar vendors). It focuses on Python problem solving, testing, debugging, code review, and writing clear explanations of code and reasoning.

It is aimed at organisations hiring Python-based coding evaluators, rubric writers, and AI code reviewers. If you’re reviewing this as a potential client or hiring manager, the sections below map my work directly to typical AI coding trainer responsibilities and show how I approach code quality, testing, and explanation.

---

## At a glance

This repo demonstrates my ability to:

- Solve a wide range of Python coding challenges with written explanations  
- Build and use a small testing framework with edge-case tests  
- Find and fix bugs, with short written post-mortems  
- Review and compare human and AI-generated solutions side by side  
- Design clear rubrics and grading guidelines for coding tasks  

If you only have a few minutes, I recommend starting with:
- `judging_two_solutions`
- `reviewing_ai_code`
- `rubrics`

---

## Repository structure

The repository is grouped into subfolders, each targeting a specific skill:

- `beginner_python_challenges`  
  Small Python projects to practise basic programming concepts and simple scripting.

- `classic_python_challenges`  
  Fifteen classic programming problems to build breadth and depth in Python problem solving.

- `testing_practice`  
  A mini test framework and tests for the classic challenges, to practise writing and running tests over multiple problems.

- `api_explorer`  
  Code that interacts with web APIs and JSON data, including basic error handling and formatted output.

- `bug_fixing_practice`  
  Five of the classic challenge solutions with bugs deliberately introduced. For each one I:
  - identify the bug  
  - explain how I found it  
  - show how I fixed it  

- `judging_two_solutions`  
  Twelve code files:
  - 10 problems where I implement **two different solutions** (one simpler but potentially less efficient, one more optimised), compare them, and recommend which I would use and why  
  - 2 files where I analyse an AI-generated solution, suggest improvements, and give a final verdict  

  In all cases I discuss trade-offs and basic time/space complexity.

- `rubrics`  
  Four markdown files. Each is a rubric for a specific problem, including:
  - the task objective  
  - example tests  
  - written guidelines for grading code  

- `reviewing_ai_code`  
  Ten files, each containing AI-written code for a specific problem. For each one I:
  - explain how the code works  
  - highlight strengths and risky aspects  
  - suggest concrete improvements  

---

## Mapping to AI coding trainer / evaluator work

- **Solving coding challenges**  
  `beginner_python_challenges`, `classic_python_challenges`

- **Writing and running tests; thinking about edge cases**  
  `testing_practice`, parts of `bug_fixing_practice`

- **Debugging and explaining fixes**  
  `bug_fixing_practice`

- **Evaluating and comparing solutions, including AI-generated code**  
  `judging_two_solutions`, `reviewing_ai_code`

- **Designing rubrics and grading guidelines**  
  `rubrics`

- **Working with real-world style code and APIs**  
  `api_explorer`

Unless noted otherwise in comments, all code and written analysis in this repository was created by me.

---

## Skills demonstrated

**Python fundamentals**

- Control flow, functions, and error handling  
- Lists, dictionaries, sets, strings  
- File I/O and basic scripts  

**Problem solving & algorithms**

- Classic coding challenge problems  
- Multiple solutions with trade-offs  
- Basic time/space complexity reasoning  

**Testing & reliability**

- Simple assertion-style test helpers  
- Edge-case thinking  
- Using tests to drive debugging of broken code  

**Debugging & code quality**

- Locating and fixing logical bugs  
- Explaining what was wrong and why the fix works  
- Improving readability and structure  

**Code review & evaluation**

- Reviewing AI-generated and human-written solutions  
- Comparing two solutions to the same task  
- Writing rubrics and qualitative feedback  

---

**Requirements**

- Python 3.10+ (any recent 3.x version should work)  
- Standard library only for most folders  
- `requests` library for `api_explorer`


---

**Quickstart**

The following commands can be used to quickly run tests for the 15 classic programming problems.

First, ensure you are in the python-ai-trainer-prep directory, then run the following:

python -m venv .venv

Windows: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate

pip install -r requirements.txt

python -m python -m testing_practice.mini_test_framework
