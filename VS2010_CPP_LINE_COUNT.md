# VS 2010 C++ Code Line Counter

This script counts the total lines of C++ code in the Visual Studio 2010 sample directories.

## Usage

Run the script from the repository root directory:

```bash
python3 count_vs2010_cpp_lines.py
```

Or make it executable and run directly:

```bash
chmod +x count_vs2010_cpp_lines.py
./count_vs2010_cpp_lines.py
```

## What it counts

The script counts lines in C++ files with the following extensions:
- `.cpp` - C++ source files
- `.c` - C source files  
- `.cxx` - C++ source files (alternative extension)
- `.cc` - C++ source files (alternative extension)
- `.h` - Header files
- `.hpp` - C++ header files
- `.hxx` - C++ header files (alternative extension)

## Directories analyzed

- **VC2010Samples** - Main Visual Studio 2010 sample directory
- **VC2010SP1Samples** - Visual Studio 2010 Service Pack 1 samples

## Sample Output

```
VS 2010 C++ Code Line Counter
========================================
VC2010Samples:
  Files: 2,870
  Lines: 348,782

VC2010SP1Samples:
  Files: 49
  Lines: 5,127

Total VS 2010 C++ Code:
  Files: 2,919
  Lines: 353,909
```

The script provides both file counts and line counts for each directory, as well as totals across all VS 2010 sample directories.