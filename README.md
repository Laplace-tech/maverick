# Maverick

Dive into Deep Learning study log with PyTorch implementations, experiment notes, and paper reviews.

## Main Focus

This repository is focused on studying **Dive into Deep Learning (D2L)**.

The goal is not just to read the textbook, but to understand, implement, experiment, and document the core ideas of modern deep learning.

## Study Rule

Read.  
Derive.  
Implement.  
Experiment.  
Commit.  
Review.

## Repository Structure

```text
maverick/
├── d2l/            # D2L chapter notes and implementations
├── papers/         # Paper reviews connected to D2L chapters
├── scripts/        # Utility scripts
├── requirements.txt
└── README.md
```

## Environment

This repository does not depend on the `d2l` Python package.

D2L is used as a web textbook, and implementations are written directly with PyTorch.

Main environment:

- Python 3.12
- PyTorch
- CUDA
- JupyterLab
- NumPy
- Pandas
- Matplotlib
- scikit-learn

## Current Status

- D2L environment configured
- CUDA available
- Chapter 2 preliminaries started

## Chapter Output Rule

Each chapter should produce:

- `notes.md` — concept summary
- `scratch implementation` — implementation from scratch when applicable
- `torch implementation` — PyTorch implementation
- `experiment log` — results, observations, and failures
- `reflection.md` — what I understood, what confused me, and what I need to review

## Paper Reading

Papers are used as secondary material connected to D2L chapters.

Each paper review should answer:

1. What problem does this paper solve?
2. What is the core idea?
3. How is it connected to the current D2L chapter?
4. What can I implement or experiment with?
5. What did I fail to understand?

## Notes

This repository is not a collection of copied tutorial notebooks.

The purpose is to build evidence of understanding through implementation, experiment, and documentation.
