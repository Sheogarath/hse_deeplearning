# Review of remaining course materials

Reviewed 2026-11-14 using `COURSE_CODE_REVIEW/INVENTORY.md`, `NOTEBOOKS.md`, and `TEXT_FILES.md`. Source extraction includes six Jupyter notebooks and Python scripts. This is a static content review; no training jobs or end-to-end execution were performed.

## Notebook materials
- `lecture_01/seminar_1_zanatye.ipynb`: tensors/autograd, manual gradient descent, cat/dog feature vectors, perceptron, loss visualization, XOR failure of one neuron and solution with a hidden layer.
- `lecture_02/seminar2.ipynb`: manual derivative/gradient descent, approximation of a scalar function, PyTorch datasets/layers, loss/optimizer, `backward()`, training and validation loop, group exercise.
- `lecture_02/pytorch_homework.ipynb`: introductory tensor operations and `nn.Module`, ReLU, cross-entropy.
- `lecture_05/seminar_tokens_embeddingsss.ipynb`: manual BPE, corpus tokenization, real tokenizers, co-occurrence/PPMI/SVD, semantic analogies, Russian pretrained word vectors, order-sensitive versus bag-of-words representations.
- `homeworks/Homework_tsk_1.ipynb`: training pipeline, manual/autograd gradients, optimizers, dropout and batch norm, train/eval behavior.
- `homeworks/Homework_task_2.ipynb`: EuroSAT 27k images, 10 classes, CNN from scratch with target test accuracy 0.85, residual block and MiniResNet, ResNet-18 transfer learning, class-level error analysis/confusion matrix/feature visualizations/attention maps.

## Python and ancillary materials
- Lecture 3: Fashion-MNIST preparation, synthetic datasets, simple classification network.
- Lecture 4: image datasets, CIFAR-10 and colored MNIST preparation, CNN example, submission evaluation and teacher notes.
- Lecture 6: MNIST autoencoders, VAE and GAN implementations, latent interpolation and generation.
- Lecture 7: RNN character/word prediction, bidirectional RNN, LSTM, GRU; text corpora and a 53MB word-vector archive.
- Lecture 8: PyTorch `MultiheadAttention` and attention mask example.
- Additional PDF duplicates, JPG/PNG teaching images, IDE config and GitHub automation files are listed in the inventory.

## Review limitations
- Static reading does not prove that every notebook or script executes successfully in a clean environment.
- Some notebook outputs contain embedded images that the text extraction omits.
- The word-vector TAR and PDFs were inventoried, not exhaustively inspected.
- The indexer's extraction may truncate source strings over 20,000 characters per cell and large text files.
- Before claiming code correctness, run a separate reproducible validation with dependencies, dataset access, and GPU where needed.

## References
- [Inventory](COURSE_CODE_REVIEW/INVENTORY.md)
- [Notebooks](COURSE_CODE_REVIEW/NOTEBOOKS.md)
- [Text scripts](COURSE_CODE_REVIEW/TEXT_FILES.md)
- [Visual lecture review](LECTURE_REVIEW.md)
