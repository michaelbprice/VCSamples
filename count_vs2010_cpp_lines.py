#!/usr/bin/env python3
"""
Script to count lines of C++ code in VS 2010 sample directories.

This script counts the total lines of code in C++ files (.cpp, .c, .cxx, .cc, .h, .hpp, .hxx)
within the Visual Studio 2010 sample directories (VC2010Samples and VC2010SP1Samples).
It also provides a breakdown by individual project directories (those containing .sln files).
"""

import os
import sys
from pathlib import Path

def count_cpp_lines_in_directory(directory_path):
    """Count lines of C++ code in the given directory."""
    cpp_extensions = {'.cpp', '.c', '.cxx', '.cc', '.h', '.hpp', '.hxx'}
    total_lines = 0
    file_count = 0
    
    directory = Path(directory_path)
    if not directory.exists():
        print(f"Warning: Directory {directory_path} does not exist")
        return 0, 0
    
    for file_path in directory.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in cpp_extensions:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = sum(1 for _ in f)
                    total_lines += lines
                    file_count += 1
            except (IOError, OSError) as e:
                print(f"Warning: Could not read file {file_path}: {e}")
    
    return total_lines, file_count

def find_sln_directories(base_directories):
    """Find all directories containing .sln files."""
    sln_dirs = []
    
    for base_dir in base_directories:
        base_path = Path(base_dir)
        if not base_path.exists():
            continue
            
        for sln_file in base_path.rglob('*.sln'):
            sln_dir = sln_file.parent
            if sln_dir not in sln_dirs:
                sln_dirs.append(sln_dir)
    
    return sln_dirs

def main():
    """Main function to count C++ lines in VS 2010 sample directories."""
    script_dir = Path(__file__).parent
    
    # VS 2010 sample directories
    vs2010_dirs = ['VC2010Samples', 'VC2010SP1Samples']
    vs2010_paths = [script_dir / dir_name for dir_name in vs2010_dirs]
    
    print("VS 2010 C++ Code Line Counter")
    print("=" * 40)
    
    total_lines = 0
    total_files = 0
    
    # Count lines by top-level directories
    for dir_name in vs2010_dirs:
        dir_path = script_dir / dir_name
        lines, files = count_cpp_lines_in_directory(dir_path)
        
        print(f"{dir_name}:")
        print(f"  Files: {files:,}")
        print(f"  Lines: {lines:,}")
        print()
        
        total_lines += lines
        total_files += files
    
    print("Total VS 2010 C++ Code:")
    print(f"  Files: {total_files:,}")
    print(f"  Lines: {total_lines:,}")
    print()
    
    # Find and analyze directories with .sln files
    print("Project Directories (containing .sln files):")
    print("=" * 50)
    
    sln_dirs = find_sln_directories(vs2010_paths)
    project_stats = []
    
    for sln_dir in sln_dirs:
        lines, files = count_cpp_lines_in_directory(sln_dir)
        if lines > 0:  # Only include directories with C++ code
            # Get relative path for cleaner display
            try:
                rel_path = sln_dir.relative_to(script_dir)
            except ValueError:
                rel_path = sln_dir
            project_stats.append((rel_path, lines, files))
    
    # Sort by line count (descending)
    project_stats.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Found {len(project_stats)} project directories with C++ code:")
    print()
    
    for i, (rel_path, lines, files) in enumerate(project_stats, 1):
        print(f"{i:3d}. {rel_path}")
        print(f"     Lines: {lines:,}")
        print(f"     Files: {files:,}")
        print()

if __name__ == '__main__':
    main()