# PERFORMANCE EVALUATION OF EFFICIENT HYBRID COMPRESSION METHODS FOR DEVANAGARI-ENCODED HINDI TEXT USING LOSSLESS ALGORITHMS

## Authors
- **Mukesh Sahu** – Delhi Technological University, Delhi 110 042, India  
- **Jeebananda Panda** – Delhi Technological University, Delhi 110 042, India  

## Abstract
This research paper provides a comprehensive performance analysis of five standard lossless compression algorithms—LZMA, Zstd, Brotli, Bzip2, and LZ4HC—alongside sixty hybrid combinations on UTF-8 encoded Hindi text datasets, written in the Devanagari script, across varying sizes—small, medium, and large. The evaluation covers compression ratio, compression speed, decompression speed, and a derived weighted normalized efficiency score.

Hybrid algorithms—especially those combining Zstd with LZ4HC or Brotli—demonstrate superior performance across all individual parameters. Independent Zstd achieves the highest efficiency score for the medium-sized dataset, illustrating how a well‑balanced algorithm can excel in overall efficiency despite not leading in any single metric. Notably, the hybrid combination **Zstd + LZ4HC** achieves the highest efficiency, with scores of 0.6764 for small files and 0.8597 for large files. This analysis highlights the potential of hybrid compression in applications such as cloud storage, mobile messaging, and NLP‑based Hindi text processing.

## Repository Contents

```text
research-hindi-compression/
├── paper/
│   └── Final_Paper.pdf       # or Final_Paper.docx / .tex
├── code/
│   └── [compression and evaluation scripts]
├── data/
│   ├── small/                # sample small dataset
│   ├── medium/               # sample medium dataset
│   └── large/                # sample large dataset
├── results/
│   ├── efficiency_scores.xlsx
│   └── plots/                # generated charts & figures

## Keywords
Hindi text compression, lossless compression, hybrid algorithms, Zstd, LZ4HC, LZMA, Brotli, Bzip2, compression ratio, decompression speed, performance evaluation

## License
This research is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

.

