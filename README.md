# Introduction to Programming and Artificial Intelligence — Companion Code and Data

This repository contains the code examples and data files referenced in the
textbook **Introduction to Programming and Artificial Intelligence** by Jeffrey Ting.

## Structure

- `chapters/chapter-NN/` — code examples and data for each chapter
- `datasets/` — shared datasets used across multiple chapters

## Chapter Map

| Chapter | Topic | Files |
|---------|-------|-------|
| 1 | What Programming Is and Why It Matters | No code files |
| 2 | Data, Decisions, and the Shape of Code | temperature_converter.py, broken programs |
| 3 | Functions, Structure, and Reuse | menu_program.py |
| 4 | Collections, Loops, and Working with Data | diary.py, sample_scores.csv |
| 5 | Debugging | pdb_practice.py, broken programs |
| 6 | Files, Persistence, and Error Handling | directory_walk_demo.py |
| 7 | Algorithms: Thinking in Steps | merge_sort.py, sorting_timing.py |
| 8 | Recursion: Functions That Call Themselves | recursion_practice.py |
| 9 | Search: How Machines Find Paths | grid_search.py, maze files |
| 10 | Optimised and Informed Search | maze_solver.py, tictactoe.py, weighted mazes |
| 11 | Probability, Bayes, and Classification | spam.csv, spam_classifier.py, text_preprocessing.py |
| 12 | Evaluation: Measuring What Your Model Knows | spam.csv, make_spam_data.py |
| 13 | Machine Learning: Teaching Computers to Learn from Data | iris.csv, ml_pipeline.py, ml_comparison.py |
| 14 | Neural Networks and Deep Learning | iris.csv, keras_neural_network.py, model_comparison.py |
| 15 | Transformers and Generative AI | rule_based_chatbot.py, genai_api_client.py |
| 16 | Bias, Fairness, and Accountability in AI | bias_probes.json, bias_testing.py |
| 17 | Putting It Together: The Journey | No code files |

## Setup

All code requires Python 3.11 or later. Install dependencies:

```
pip install numpy scikit-learn pandas
```

For Chapter 14 (neural networks), also install:

```
pip install tensorflow
```

For Chapter 15 (generative AI), you will need an API key from a provider
such as OpenAI.

## Licence

These code examples are provided for educational use alongside the textbook.
