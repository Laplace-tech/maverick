# Maverick D2L Code Style

Derived from all 68 notebooks under `src` on 2026-07-27.

## Canonical patterns

- Preserve the supplied D2L source algorithm, class hierarchy, data helper, trainer, and lesson flow. Repository style may change syntax and formatting, but it must not replace the source implementation with a different training architecture.
- Use `@` for matrix multiplication. Do not use `torch.matmul(...)` in learner practice code.
- Prefer explicit algebra that mirrors the formula, for example:
  `H = relu(X @ self.W1 + self.b1)`.
- When adding a method after a class definition, use explicit assignment:
  `Classifier.accuracy = classifier_accuracy`.
- Do not use `@d2l.add_to_class(...)`.
- Use `.reshape(...)`; the existing notebooks do not use `.view(...)`.
- Prefer standard PyTorch and locally defined classes over opaque D2L helper abstractions. Use D2L utilities only where they are intentionally part of the lesson, such as plotting or supplied data helpers.
- Scratch implementations should expose the tensor operations directly.
- Concise implementations should use `nn.Module`, `nn.Sequential`, and standard PyTorch layers.
- Use descriptive `snake_case` names and double-quoted strings.
- Break long function calls and expressions across lines with trailing commas.
- Put a short title comment at the top of every supplied code cell.
- Add shape comments at important matrix operations and reshapes.
- Keep `logits` separate from probabilities and pass logits directly to stable combined losses such as `CrossEntropyLoss`.
- Clear accumulated gradients before each new backward pass.
- Use `@torch.no_grad()` or `with torch.no_grad():` where gradient tracking is genuinely unnecessary; this rule does not prohibit standard PyTorch decorators.
- Give learner-defined tensor helpers explicit `torch.Tensor` parameter and return annotations when Pylance cannot infer a stable type.
- Do not aggregate a generator of tensors with Python's built-in `sum(...)`: its integer start value can widen the inferred result to `torch.Tensor | int`. Use `torch.stack(tensors, dim=0).sum(dim=0)` instead.
- Treat source fidelity as algorithm and lesson-flow fidelity, not verbatim preservation of unclear syntax.
- Before presenting practice code, verify all four gates: source algorithm preserved, tensor types explicit where needed, Pylance type errors eliminated, and equivalent Runtime execution successful.
- Runtime success alone is not sufficient for learner-facing code.

## Repository evidence

- Notebooks inspected: 68
- Matrix multiplication with `@`: 61 occurrences
- `torch.matmul`: 1 occurrence, in the currently incomplete Chapter 5 cell
- `@d2l.add_to_class`: 0 occurrences
- Explicit post-definition method assignments:
  - `Classifier.accuracy = classifier_accuracy`
  - `SoftmaxRegressionScratch.loss = model_loss`
- `.reshape(...)`: 55 occurrences
- `.view(...)`: 0 occurrences
- Double-quoted strings dominate single-quoted strings: 987 versus 9 matches

## Notebook ownership

- Codex creates a valid notebook with only the standard imports prepopulated when a new notebook is required; the import cell has no title comment.
- Codex executes and saves the import cell with the `Python (maverick)` kernel, verifying the required imports before handoff.
- Standard D2L imports are `torch`, `from torch import nn`, and `from d2l import torch as d2l`; add other imports only when the source requires them.
- The learner types and executes every lesson cell after the prebuilt import cell.
- Codex does not modify existing learner-authored cells or outputs.
