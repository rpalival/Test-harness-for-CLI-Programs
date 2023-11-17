#!/opt/homebrew/bin/python3
import os
import subprocess

def run_test(prog_dir, prog, input_file, expected_output_file):
    with open(input_file, 'r') as infile, open(expected_output_file, 'r') as expectedfile:
        # Run the program from the 'prog' directory
        proc = subprocess.run([os.path.join(prog_dir, f'{prog}.py')], stdin=infile, capture_output=True, text=True)
        output = proc.stdout.rstrip('\n')
        expected_output = expectedfile.read().rstrip('\n')

        if output != expected_output or proc.returncode != 0:
            # Additional debugging information
            return False, output, expected_output

    return True, None, None

def main():
    # Define paths to the 'test' and 'prog' directories
    test_dir = './test/'
    prog_dir = './prog/'

    test_results = {'OK': 0, 'OutputMismatch': 0, 'total': 0}

    for filename in os.listdir(test_dir):
        if filename.endswith('.in'):
            parts = filename.split('.')
            test_name = parts[0]  # Get the program name
            test_type = '.'.join(parts[1:-1])  # Get the test type
            input_file = os.path.join(test_dir, filename)
            expected_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.out')
            expected_arg_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.arg.out')

            # Run test in STDIN mode
            passed, output, expected_output = run_test(prog_dir, test_name, input_file, expected_output_file)
            if not passed:
                print(f"FAIL: {test_name} failed (TestResult.OutputMismatch)\n"
                      f"      expected:\n{expected_output}\n\n"
                      f"           got:\n{output}\n")
                test_results['OutputMismatch'] += 1
            else:
                test_results['OK'] += 1

            # Run test in argument mode
            if os.path.exists(expected_arg_output_file):
                passed, output, expected_output = run_test(prog_dir, test_name, input_file, expected_arg_output_file)
                if not passed:
                    print(f"FAIL: {test_name} failed in argument mode (TestResult.OutputMismatch)\n"
                          f"      expected:\n{expected_output}\n\n"
                          f"           got:\n{output}\n")
                    test_results['OutputMismatch'] += 1
                else:
                    test_results['OK'] += 1

            test_results['total'] += 1

    # Print summary
    print(f"\nOK: {test_results['OK']}\noutput mismatch: {test_results['OutputMismatch']}\ntotal: {test_results['total']}")

    if test_results['OutputMismatch'] > 0:
        exit(1)

if __name__ == "__main__":
    main()
