# D2L Study Checkpoint

Updated: 2026-07-28 KST

## Current progress

- Chapter 4 sections 4.4 through 4.6 completed.
- Section 4.7 was explicitly skipped by the learner.
- Chapter 5 introductory passage and section 5.1 introduction completed.
- Section 5.1.1 Hidden Layers was redone as a paragraph-complete translation using English-first technical terminology and LaTeX equations.
- Section 5.1.2 Activation Functions is complete: ReLU, pReLU, Sigmoid, and Tanh.
- Section 5.1.3 Summary and Discussion is complete.
- Section 5.1.4 Exercises is skipped by default.
- Section 5.2 introduction and 5.2.1 Implementation from Scratch have been delivered; learner practice is pending.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_2_implementation_of_multilayer_perceptrons/01_mlp_from_scratch.ipynb`.
- Section 5.2.2 Concise Implementation has been delivered; learner practice is pending.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_2_implementation_of_multilayer_perceptrons/02_concise_mlp.ipynb`.
- Section 5.2.3 Summary is complete.
- Section 5.2.4 Exercises is skipped by default.
- Section 5.3 introduction and 5.3.1 Forward Propagation are complete.
- Section 5.3.2 Computational Graph of Forward Propagation is complete.
- Section 5.3.3 Backpropagation is complete.
- Section 5.3.4 Training Neural Networks is complete.
- Section 5.3.5 Summary is complete.
- Section 5.3.6 Exercises is skipped by default.
- No separate 5.3 practice notebook is planned: the source contains no code and a new exercise would mostly repeat Chapter 2 automatic differentiation.
- Section 5.4.1 source practice code has been delivered: Sigmoid Gradient and Exploding Matrix Product.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_4_numerical_stability_and_initialization/01_vanishing_and_exploding_gradients.ipynb`.
- Section 5.4.2 Parameter Initialization contains no source implementation code; no notebook was created.
- Section 5.4.3 Summary is complete.
- Section 5.4.4 Exercises is skipped by default.
- Section 5.5 Generalization in Deep Learning contains no source implementation code; no notebook was created.
- Section 5.5.6 Exercises is skipped by default.
- Section 5.6 was restarted under the combined translation, explanation, and implementation workflow.
- Section 5.6 introduction has been redelivered.
- Section 5.6.1 Dropout in Practice is complete.
- Section 5.6.2 Implementation from Scratch practice is complete.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_6_dropout/01_dropout_from_scratch.ipynb`.
- Section 5.6.3 Concise Implementation practice is complete.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_6_dropout/02_concise_dropout.ipynb`.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_1_multilayer_perceptrons/01_activation_functions.ipynb`.
- Section 5.6.4 Summary is complete.
- Section 5.6.5 Exercises is skipped by default.
- Section 5.7 introduction, 5.7.1 Downloading Data, and 5.7.2 Kaggle are complete.
- Section 5.7.3 Accessing and Reading the Dataset practice is complete.
- Section 5.7.4 Data Preprocessing is complete.
- Section 5.7.5 Error Measure practice is complete.
- Section 5.7.6 K-Fold Cross-Validation practice is complete.
- Section 5.7.7 Model Selection practice is complete.
- Section 5.7.8 Submitting Predictions on Kaggle practice and the first Kaggle submission are complete; public score: 0.41188.
- Practice notebook: `src/ch05_multilayer_perceptrons/sec5_7_predicting_house_prices_on_kaggle/01_kaggle_house_price_prediction.ipynb`.
- Section 5.7.9 Summary and Discussion is complete.
- Section 5.7.10 Exercises is skipped by default.
- Chapter 5 is complete.

## Teaching and notebook rules

- Codex handles the complete workflow again: full source translation, conceptual tutoring, notebook preparation, and source-faithful implementation code.
- `다음` advances to the next source boundary and includes both translation and explanation; implementation code follows whenever it appears in the source.
- If the source has no implementation code and no useful practice is warranted, Codex does not invent code or create a notebook.
- Cover ordinary sections and subsections in the original book order.
- For each subsection, provide the full translation first, then an undergraduate-level explanation, formulas and tensor shapes, implementation pitfalls, and practice code when code is appropriate.
- Skip subsections titled `Exercises` unless the learner explicitly requests them.
- Group notebooks by a coherent implementation flow and split them only when they become unwieldy.
- When a notebook is needed, Codex creates only a blank valid `.ipynb`.
- The learner manually types and runs every code cell.
- Codex provides code in chat, divided cell by cell.
- Every code cell begins with a title comment such as `# 셀 3 — 안정적인 교차 엔트로피`.
- Always identify the notebook path before presenting cells.
- Use VS Code with `.venv/bin/python` as the interpreter/kernel.
- Before a new implementation block, lightly verify that the active `maverick .venv` kernel can execute code; never terminate a healthy kernel.

## Preserved source text

- `source/ch04_sections_4_4_to_4_7.txt`
  - SHA-256: `b9ada89ade13236d39991411af7c7f248c2711fa6b7436237e4b6b2d16c2ba33`
- `source/ch05_full.txt`
  - SHA-256: `f75bf11c5ed1fca9f879968fbf94f1e2e7fc22077354364dcda2586fa45ae33b`
- `source/ch05_section_5_1_excerpt.txt`
  - SHA-256: `978c3f6cc347a72e1dca7955cbda594429f0fe43440cb4acd4cc4ede38b99667`

## Existing Chapter 4 notebooks

- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/01_concise_softmax_regression.ipynb`
- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/02_softmax_revisited.ipynb`
- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/03_training.ipynb`

Preserve all learner-written notebook cells and outputs.
