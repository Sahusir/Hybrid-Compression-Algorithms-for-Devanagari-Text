import time
import os
import math
import pandas as pd
import lzma
import zstandard as zstd

def calculate_entropy(data):
    frequency = {char: data.count(char) for char in set(data)}
    total_chars = len(data)
    entropy = -sum((freq / total_chars) * math.log2(freq / total_chars) for freq in frequency.values()) if total_chars > 0 else 0
    return entropy

def hybrid_compress(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
    
    original_entropy = calculate_entropy(data)
    data_bytes = data.encode()
    
    start_time = time.perf_counter()
    zstd_compressed = zstd.ZstdCompressor(level=6).compress(data_bytes)
    compressed_data = lzma.compress(zstd_compressed, preset=6)
    compression_time = time.perf_counter() - start_time
    
    with open(output_file, 'wb') as f:
        f.write(compressed_data)
    
    original_size = len(data_bytes) / 1024  # KB
    compressed_size = len(compressed_data) / 1024  # KB
    compression_ratio = original_size / compressed_size if compressed_size > 0 else float('inf')
    compression_speed = (original_size / compression_time) / 1024 if compression_time > 0 else float('inf')  # MB/s
    
    return input_file, original_size, compressed_size, compression_ratio, compression_time, compression_speed, original_entropy

def hybrid_decompress(input_file, output_file):
    start_time = time.perf_counter()
    with open(input_file, 'rb') as f:
        compressed_data = f.read()
    
    lzma_decompressed = lzma.decompress(compressed_data)
    decompressed_data = zstd.ZstdDecompressor().decompress(lzma_decompressed).decode()
    decompression_time = time.perf_counter() - start_time
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decompressed_data)
    
    decompressed_size = len(decompressed_data.encode()) / 1024  # KB
    decompressed_entropy = calculate_entropy(decompressed_data)
    decompression_speed = (decompressed_size / decompression_time) / 1024 if decompression_time > 0 else float('inf')  # MB/s
    
    return input_file, decompressed_size, decompression_time, decompression_speed, decompressed_entropy

# === File Paths (relative to project root) ===
short_term_file = "data/Small Hinditextfile.txt"
medium_term_file = "data/medium hindi textfile.txt"
long_term_file = "data/large hindi textfile.txt"


# Output Paths
short_output = short_term_file + ".hybrid_compressed"
medium_output = medium_term_file + ".hybrid_compressed"
long_output = long_term_file + ".hybrid_compressed"
short_decompressed = short_term_file + ".hybrid_decompressed.txt"
medium_decompressed = medium_term_file + ".hybrid_decompressed.txt"
long_decompressed = long_term_file + ".hybrid_decompressed.txt"

# Compress files
compression_results = [
    hybrid_compress(short_term_file, short_output),
    hybrid_compress(medium_term_file, medium_output),
    hybrid_compress(long_term_file, long_output)
]

# Decompress files
decompression_results = [
    hybrid_decompress(short_output, short_decompressed),
    hybrid_decompress(medium_output, medium_decompressed),
    hybrid_decompress(long_output, long_decompressed)
]

# Create DataFrames and display results
compression_df = pd.DataFrame(compression_results, columns=["File", "Original Size (KB)", "Compressed Size (KB)", "Compression Ratio", "Compression Time (sec)", "Compression Speed (MB/s)", "Original Entropy"])
decompression_df = pd.DataFrame(decompression_results, columns=["File", "Decompressed Size (KB)", "Decompression Time (sec)", "Decompression Speed (MB/s)", "Decompressed Entropy"])

print("Compression Results:")
print(compression_df.to_string(index=False))
print("\nDecompression Results:")
print(decompression_df.to_string(index=False))
