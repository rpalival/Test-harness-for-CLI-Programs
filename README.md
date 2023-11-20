[![Run Tests CI](https://github.com/rpalival/cs515-project1/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/rpalival/cs515-project1/actions/workflows/test.yml)
# cs515-project1

Name: Raj Palival
Stevens login: rpalival@stevens.edu
CWID: 20010540

GitHub URL: https://github.com/rpalival/cs515-project1
TIme-Taken: 40 hours

3. a description of how you tested your code?
Overview of Test Harness:
Locating Test Files:
The test harness scans the test/ directory to find test input files, typically with a specific naming convention, e.g., PROG.NAME.in for input and PROG.NAME.out for expected output. This allows it to automatically pair each input file with its corresponding expected output file.
Running Tests for Each Script:
For each test file found, the test harness determines the corresponding program (e.g., wc, gron, or csvsum) based on the filename.
It then runs the appropriate Python script (like wc.py, gron.py, or csvsum.py) using the input file and captures the script's output.
Comparing Output:
The captured output of each script is compared against the expected output stored in the corresponding .out file.
The test harness checks if the actual output matches the expected output exactly. Any discrepancies are flagged as a test failure.
Handling Different Input Modes:
For scripts that support both direct file input and standard input (stdin), the test harness may run each test twice:
Once by passing the filename as an argument.
Once by piping the contents of the file into the script, emulating stdin.
This dual approach ensures the script correctly handles input in both ways.
Flag and Argument Handling:
For scripts like wc.py that accept flags or specific arguments (e.g., column names for csvsum.py), the test harness can be set up to include these flags or arguments when running the script.
Test filenames may include indications of which flags or arguments to use, and the test harness parses these from the filename.
Reporting Results:
After running all tests, the test harness reports the results, detailing which tests passed and which failed.
For failed tests, it may provide information about what was expected versus what was actually produced.

4. any bugs or issues you could not resolve?
Issue with Multiple Files Extension in wc.py Testing
Test File Naming and Parsing:
The test harness needs to correctly parse test filenames that indicate multiple input files for wc.py. This involves a specific naming convention (like wc.file1_file2.in) and extracting individual file names from it.
Constructing Correct Command:
The test harness must construct and execute the command that passes multiple files to wc.py. This can be complex, as it involves handling a list of files rather than a single file.
Comparing Outputs:
Ensuring the output from wc.py when processing multiple files is correctly captured and compared against the expected output can be tricky, especially when considering the aggregated results.


5. an example of a difficult issue or bug and how you resolved it
Challenge: The main challenge was modifying the script to dynamically change the base object name in the gron.py based on user input while ensuring it did not disrupt the existing functionality and structure of the script. Additionally, the script needed to handle cases where the flag was not used, defaulting to the original behavior.

Resolution Steps
Argument Parsing: First, the script was updated to include a new argument in the argparse parser for the --obj flag. Care was taken to ensure this new argument was optional and had a default value of 'json'.
Dynamic Object Naming: The core function responsible for flattening the JSON was then updated. This function previously hard-coded the base object name as 'json'. The code was refactored to replace this hard-coded value with a variable that could change based on the user's input.
Testing and Validation: After implementing the changes, a series of tests were conducted. This included scenarios where the flag was used with different values and scenarios where the flag was omitted. The aim was to ensure that the script's output matched expected results in all these cases.

6. a list of the three extensions you’ve chosen to implement, with appropriate detail
1. Flag Extension in wc.py
Objective: Enhance wc.py to support command-line flags for controlling the output, similar to the Unix wc command.

Details:
Flags Implemented:
-l or --lines: Count only the number of lines.
-w or --words: Count only the number of words.
-c or --chars: Count only the number of characters.
Functionality: When one or more of these flags are used, wc.py will restrict its output to only the requested metrics. For example, if -l is used, it will only report the number of lines.
Default Behavior: Without any flags, the script will count lines, words, and characters, as it originally did.
Implementation: Involved updating the argument parsing to handle these flags and modifying the core counting logic to conditionally perform counts based on the presence of these flags.
Testing:
2. Multiple File Extension in wc.py
Objective: Extend wc.py to process multiple files simultaneously and provide aggregated results.

Details:
Multiple File Input: Allow wc.py to accept multiple file paths as input.
Aggregated Output: In addition to individual counts for each file, provide a total count that aggregates lines, words, and characters across all provided files.
Handling File Errors: Implement error handling for scenarios where a provided file path does not exist or is not accessible.
Implementation: Required modification of the file processing loop to iterate over multiple files and an aggregation mechanism to compile total counts.
3. Custom Base Object Extension in gron.py
Objective: Implement a feature in gron.py to allow users to specify a custom base object name for the flattened JSON output.
Testing:
Details:
Custom Base Object Flag: Introduce a --obj flag that enables users to specify the name of the base object in the output.
Default Behavior: By default, or if the flag is not used, the base object name remains 'json'.
Dynamic Replacement: Modify the JSON flattening logic to dynamically use the user-specified base object name instead of the hardcoded 'json'.
Error Handling: Ensure the script gracefully handles cases where the provided base object name is invalid or empty.
Implementation: Involved updating the argument parser to include the --obj flag and refactoring the JSON processing function to use this customizable base object name.
Testing: