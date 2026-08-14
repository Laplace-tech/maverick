# D2L Study Checkpoint

Updated: 2026-08-14 KST

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
- Chapter 6 Builders' Guide is complete.
- Section 6.1 Layers and Modules practice is complete.
- Practice notebooks:
  - `src/ch06_builders_guide/sec6_1_layers_and_modules/01_layers_and_modules.ipynb`
  - `src/ch06_builders_guide/sec6_1_layers_and_modules/02_my_sequential.ipynb`
  - `src/ch06_builders_guide/sec6_1_layers_and_modules/03_custom_forward_propagation.ipynb`
- Section 6.2 Parameter Management practice is complete.
- Section 6.3 Parameter Initialization practice is complete.
- Section 6.4 Lazy Initialization practice is complete.
- Section 6.5 Custom Layers practice is complete.
- Section 6.6 File I/O practice is complete.
- Section 6.7 GPUs practice is complete through 6.7.3 Neural Networks and GPUs.
- Section 6.7.4 Summary is complete; it contains no additional implementation.
- Section 6.7.5 Exercises is skipped by default.
- GPU practice notebooks:
  - `src/ch06_builders_guide/sec6_7_gpus/01_computing_devices.ipynb`
  - `src/ch06_builders_guide/sec6_7_gpus/02_tensors_and_gpus.ipynb`
  - `src/ch06_builders_guide/sec6_7_gpus/03_neural_networks_and_gpus.ipynb`
- Chapter 7 source text is preserved in full and was verified on 2026-08-01.
- Chapter 7 Convolutional Neural Networks is complete through Section 7.6.3 Summary.
- Sections 7.1.6, 7.2.8, 7.3.4, 7.4.5, 7.5.5, and 7.6.4 Exercises were skipped by default.
- Nine Chapter 7 practice notebooks cover cross-correlation, kernel learning, padding and stride, multiple channels, `1x1` convolution, pooling, and LeNet.
- LeNet was trained on Fashion-MNIST with the RTX 3060 Ti; final validation accuracy was 73.39% after 10 epochs.
- Chapter 8 source text was supplied, preserved in full, and range-validated on 2026-08-03.
- The preserved range begins with the Chapter 8 introduction and ends after Section 8.8.6 Exercises.
- Chapter 8 is complete through Section 8.7.6, covering AlexNet, VGG, NiN, GoogLeNet, batch normalization, ResNet, ResNeXt, and DenseNet.
- Section 8.8 Designing Convolution Network Architectures was intentionally skipped by the learner.
- Chapter 8 Exercises were skipped by default.
- Chapter 9 source text was supplied, preserved in full, and range-validated on 2026-08-06.
- The preserved Chapter 9 range begins with the chapter introduction and ends after Section 9.7.4 Exercises.
- The supplied extraction contains compressed spacing and formula-layout artifacts in parts of the later sections; preserve the source text and verify affected equations during tutoring.
- Chapter 9 notebooks were hard-reset by the learner on 2026-08-08. Do not reuse pre-reset notebook contents or Git history as implementation templates; rebuild from the preserved source and the learner's current fresh notebooks only.
- Resolve relative dataset paths from the actual notebook working directory. For notebooks under `sec9_2_converting_raw_text_into_sequence_data`, the original D2L default root `../data` resolves to `src/ch09_recurrent_neural_networks/data`.
- Chapter 9 is complete through Section 9.7.3 Summary.
- Section 9.7.4 Exercises was skipped by default.
- Chapter 10 Modern Recurrent Neural Networks source text was supplied, preserved in full, and range-validated on 2026-08-09.
- The preserved Chapter 10 range begins with the chapter introduction and ends after Section 10.8.5 Exercises and its discussion marker.
- Chapter 10 main sections and numbered subsections were checked against the official D2L 1.0.3 web pages; Sections 10.1 through 10.8 are present with no missing numbered subsection.
- The supplied extraction contains compressed spacing and formula-layout artifacts; preserve the source text and verify affected equations against the official page during tutoring.
- Chapter 10 is complete through Section 10.8.4 Summary; Section 10.8.5 Exercises was skipped by default.
- Chapter 11 Attention Mechanisms and Transformers source text was supplied, LF-normalized, preserved in full, and range-validated on 2026-08-13.
- The preserved Chapter 11 range begins with the chapter introduction and ends after Section 11.9.7 Exercises and its discussion marker.
- Chapter 11 main sections and numbered subsections were checked against the official D2L 1.0.3 table of contents; Sections 11.1 through 11.9 are present with no missing numbered subsection.
- The supplied extraction contains compressed spacing and formula-layout artifacts; preserve the source text and verify affected equations against the official page during tutoring.
- Chapter 11 is complete through Section 11.3.5 Summary; Sections 11.2.5 and 11.3.6 Exercises were skipped by default.
- Section 11.4 introduction and 11.4.1 Model are complete, including a focused review of the conventional fixed-context Seq2Seq encoder–decoder bottleneck.
- Practice notebooks cover attention heatmaps, similarity kernels, Nadaraya–Watson attention pooling, kernel comparison, kernel-width adaptation, masked softmax, batch matrix multiplication, scaled dot product attention, and additive attention.
- The conventional Seq2Seq decoder review was rewritten through its decoder tensor-shape validation in `src/ch10_modern_recurrent_neural_networks/sec10_7_sequence_to_sequence_learning_for_machine_translation/02_seq2seq_decoder.ipynb`.
- Next starting point: Section 11.4.2 Defining the Decoder with Attention.

## Teaching and notebook rules

- Codex handles the complete workflow again: full source translation, conceptual tutoring, notebook preparation, and source-faithful implementation code.
- `다음` advances to the next source boundary and includes both translation and explanation; implementation code follows whenever it appears in the source.
- If the source has no implementation code and no useful practice is warranted, Codex does not invent code or create a notebook.
- Cover ordinary sections and subsections in the original book order.
- For each subsection, provide the full translation first, then an undergraduate-level explanation, formulas and tensor shapes, implementation pitfalls, and practice code when code is appropriate.
- Build the core explanation with visual data-flow diagrams and the source equations; add clearly identified supplemental equations when they materially improve first-time understanding.
- When source implementation appears, preserve its algorithm and lesson flow while reorganizing it into learner-sized cells with shape checks, intermediate outputs, or small visual probes that help a first-time learner internalize the CNN principle.
- Skip subsections titled `Exercises` unless the learner explicitly requests them.
- Group notebooks by a coherent implementation flow and split them only when they become unwieldy.
- When a notebook is needed, Codex creates a valid `.ipynb` whose first cell contains only the required imports; do not add a title comment such as `# 셀 1 — 기본 import` to this import cell.
- Codex executes and saves that import cell with the `Python (maverick)` kernel to verify that the notebook kernel and required imports work.
- A standard D2L import cell contains `torch`, `nn`, and `d2l`; add other source-required imports only when needed.
- The learner manually types and runs every lesson cell after the prebuilt import cell.
- Codex provides code in chat, divided cell by cell.
- Every code cell begins with a title comment such as `# 셀 3 — 안정적인 교차 엔트로피`.
- Always identify the notebook path before presenting cells.
- Keep Pylance types stable in tensor helpers: add `torch.Tensor` annotations and use `torch.stack(...).sum(dim=0)` instead of Python `sum(...)` over tensors.
- Every supplied practice block must pass four gates before handoff: preserve the source algorithm and lesson flow, use explicit tensor types where inference is unstable, remain clean under Pylance, and succeed in an equivalent Runtime check. Do not reproduce unclear source syntax verbatim merely for visual fidelity.
- Use VS Code with `.venv/bin/python` as the interpreter/kernel.
- Before a new implementation block, lightly verify that the active `maverick .venv` kernel can execute code; never terminate a healthy kernel.

## Preserved source text

- `source/ch04_sections_4_4_to_4_7.txt`
  - SHA-256: `b9ada89ade13236d39991411af7c7f248c2711fa6b7436237e4b6b2d16c2ba33`
- `source/ch05_full.txt`
  - SHA-256: `f75bf11c5ed1fca9f879968fbf94f1e2e7fc22077354364dcda2586fa45ae33b`
- `source/ch05_section_5_1_excerpt.txt`
  - SHA-256: `978c3f6cc347a72e1dca7955cbda594429f0fe43440cb4acd4cc4ede38b99667`
- `source/ch07_full.txt`
  - SHA-256: `59b63df44b79fa18fbf333cb6fa0cd7e20c701db9b261e768b5b01bbe7236de5`
- `source/ch08_full.txt`
  - SHA-256: `84140dde76766ccc1ff0472ecc3160c51e151edc67428d4fe7f5938cefdeaa8e`
- `source/ch08_section_8_1_alexnet.txt`
  - SHA-256: `a21cf5098b8de7609e5b7dbb60d3d9cf7cbd5d0b5b9d92356ac741fddff61c1e`
  - Verified against the corresponding Chapter 8 full-source range on 2026-08-03; substantive text and code match.
- `source/ch08_sections_8_2_to_8_5.txt`
  - SHA-256: `096e5970f8324fba4bb15f487b922f1713a52a68156665708726e3c495fb94a4`
  - Covers Sections 8.2 through 8.5.7 and matches the corresponding full-source range except for terminal discussion-link punctuation.
- `source/ch09_full.txt`
  - SHA-256: `f871d222d89342350e83d98fd846653d643fdf1e72a079784c945a0d4a251632`
  - LF-normalized preservation of the supplied Chapter 9 source; range begins at the chapter introduction and ends after Section 9.7.4 Exercises.
- `source/ch10_full.txt`
  - SHA-256: `0eed239078b1f83f9036342bddab260a13fa19f37f2f136b8aacbd04890440a9`
  - LF-normalized preservation of the supplied Chapter 10 source; range begins at the chapter introduction and ends after Section 10.8.5 Exercises and its discussion marker.
- `source/ch11_full.txt`
  - SHA-256: `bb3680bf98c31cc034d74afc0fe02e16fccb233450fba30d97a5b5e4b7329787`
  - LF-normalized, trailing-whitespace-cleaned preservation of the supplied Chapter 11 source; range begins at the chapter introduction and ends after Section 11.9.7 Exercises and its discussion marker.

## Existing Chapter 4 notebooks

- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/01_concise_softmax_regression.ipynb`
- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/02_softmax_revisited.ipynb`
- `src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/03_training.ipynb`

Preserve all learner-written notebook cells and outputs.
