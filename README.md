[![Run Tests CI](https://github.com/rpalival/cs515-project1/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/rpalival/cs515-project1/actions/workflows/test.yml)
# CS515 Project 1

**Name:** Raj Palival  
**Stevens Login:** rpalival@stevens.edu  
**CWID:** 20010540  
**GitHub URL:** [https://github.com/rpalival/cs515-project1](https://github.com/rpalival/cs515-project1)  
**Time Taken:** 40 hours  

## 3. Testing Approach

### Overview of Test Harness

- **Locating Test Files**:
  - Scans the `test/` directory for input files named `PROG.NAME.in` and corresponding expected output files named `PROG.NAME.out`.
  
- **Running Tests for Each Script**:
  - Determines the relevant program (e.g., `wc`, `gron`, `csvsum`) based on the filename and runs it with the provided input.

- **Comparing Output**:
  - Compares the script's output against the expected output in `.out` files, flagging discrepancies as failures.

- **Handling Different Input Modes**:
  - Tests both direct file input and `stdin` input for scripts that support both.

- **Flag and Argument Handling**:
  - Includes script-specific flags or arguments as indicated in test filenames.

- **Reporting Results**:
  - Reports which tests passed and which failed, providing detailed information on failures.

## 4. Unresolved Bugs or Issues

### Issue with Multiple Files Extension in `wc.py`

- **Test File Naming and Parsing**:
  - Difficulty in correctly parsing filenames for multiple input files.

- **Constructing Correct Command**:
  - Challenges in executing the command that correctly passes multiple files to `wc.py`.

- **Comparing Outputs**:
  - Complexities in accurately capturing and comparing outputs for multiple files.

## 5. Resolved Difficult Issue

### Challenge: Flag Extension in `gron.py`

- **Argument Parsing**:
  - Updated script to include `--obj` flag with default value 'json'.

- **Dynamic Object Naming**:
  - Refactored the JSON flattening function to use variable base object names.

- **Testing and Validation**:
  - Conducted thorough testing to ensure correct behavior with and without the flag.

## 6. Implemented Extensions

### 1. Flag Extension in `wc.py`

- **Objective**: Enhance `wc.py` with command-line flags for output control.
- **Flags Implemented**:
  - `-l` or `--lines`: Count only lines.
  - `-w` or `--words`: Count only words.
  - `-c` or `--chars`: Count only characters.
- **Testing**:
  - Verified flags' functionality through various test cases.

### 2. Multiple File Extension in `wc.py`

- **Objective**: Allow `wc.py` to process and aggregate results from multiple files.
- **Implementation**:
  - Modified file processing to handle multiple files and aggregate counts.

### 3. Custom Base Object Extension in `gron.py`

- **Objective**: Enable custom base object naming in flattened JSON output.
- **Implementation**:
  - Integrated `--obj` flag for customizable base object names.
- **Testing**:
  - Ensured functionality through targeted script testing.

---