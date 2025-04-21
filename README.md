PERFORMANCE EVALUATION OF EFFICIENT HYBRID COMPRESSION METHODS FOR DEVANAGARI-ENCODED HINDI TEXT USING LOSSLESS ALGORITHMS
## Authors
Mukesh Sahu – Delhi Technological University, Delhi 110 042, India

Jeebananda Panda – Delhi Technological University, Delhi 110 042, India

## Abstract
This research paper provides a comprehensive performance analysis of five standard lossless compression algorithms—LZMA, Zstd, Brotli, Bzip2, and LZ4HC—alongside sixty hybrid combinations on UTF-8 encoded Hindi text datasets, written in the Devanagari script, across varying sizes—small, medium, and large. The evaluation covers compression ratio, compression speed, decompression speed, and a derived weighted normalized efficiency score.

Hybrid algorithms—especially those combining Zstd with LZ4HC or Brotli—demonstrate superior performance across all individual parameters. Independent Zstd achieves the highest efficiency score for the medium-sized dataset, illustrating how a well‑balanced algorithm can excel in overall efficiency despite not leading in any single metric. Notably, the hybrid combination Zstd + LZ4HC achieves the highest efficiency, with scores of 0.6764 for small files and 0.8597 for large files. This analysis highlights the potential of hybrid compression in applications such as cloud storage, mobile messaging, and NLP‑based Hindi text processing.

## Implementation Details
The compression framework employs a sequential hybrid approach, where two compression algorithms are applied in succession. The following standard configurations were used for all algorithms:

LZMA: Compression level 6, no dictionary.

Zstandard (Zstd): Compression level 6, no dictionary.

Brotli: Quality level 6, window size 22.

Bzip2: Default settings, block size of 900 KB.

LZ4HC: Compression level 6, no dictionary.

These configurations were selected to ensure consistency and fairness across all standalone and hybrid evaluations.

## Repository Contents
research-hindi-compression/
├── paper/                # Final paper and appendix
│   ├── Final_Paper.docx
│   └── All_Algorithms_Performance_Metrics.docx
├── code/                 # Compression and evaluation scripts
├── data/                 # Sample Hindi text datasets: small, medium, large
├── results/              # Final results summary and analysis with graphs/tables
│   └── Final_Results_Analysis.docx
├── README.md             # Project description and usage instructions

## How to Replicate Results

 To replicate the results from this project, follow the steps below:

1. Clone or Download the Repository
Clone the repository using Git:
git clone https://github.com/your-username/Hybrid-Compression-Algorithms-for-Devanagari-Text.git

 Alternatively, you can download the repository as a .zip file from GitHub and extract it.

2. Ensure the Folder Structure Is Correct
After cloning or downloading, make sure your directory structure looks like this:
/Hybrid-Compression-Algorithms-for-Devanagari-Text
├── code/
├── data/
│   ├── Small Hinditextfile.txt
│   ├── medium hindi textfile.txt
│   └── large hindi textfile.txt
├── paper/
│   └── All_Algorithms_Performance_Metrics.docx
└── README.md
3. Install Dependencies
 Ensure that Python 3.8+ is installed on your system.

 Install required Python packages:
pip install pandas lzma zstandard brotli bz2file lz4

4. Run the Compression Script
 Navigate to the code/ folder:
cd code/

 Run the compression script:
python zstd+lzma pipeline.py


5. Results
After running the script, the compression and decompression results will be output, including metrics like compression ratio, compression speed, decompression speed, and entropy.



## Compare Results:

a. Detailed metrics: paper/All_Algorithms_Performance_Metrics.docx

b. Top 10 comparisons & charts: results/Final_Results_Analysis.docx

##  Keywords
Hindi text compression, lossless compression, hybrid algorithms, Zstd, LZ4HC, LZMA, Brotli, Bzip2, compression ratio, decompression speed, performance evaluation

## License
This research is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
