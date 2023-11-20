#!/opt/homebrew/bin/python3
import os
import subprocess

def run_test(prog_dir, prog, input_file, expected_output_file, use_shell=False, additional_args=None):
    with open(expected_output_file, 'r') as expectedfile:
        if use_shell:
            # Building the command to use shell piping
            cat_command = f"cat {input_file} | python3 {os.path.join(prog_dir, f'{prog}.py')}"
            if additional_args:
                cat_command += ' ' + ' '.join(additional_args)
            command = cat_command
        else:
            # Directly running the script with subprocess
            command = ['python3', os.path.join(prog_dir, f'{prog}.py')]
            if prog == 'wc':
                command.append(input_file)
            elif additional_args:
                command.extend(additional_args)

        print(f"Running test with input: {input_file}, command: {command}")
        # Run the program from the 'prog' directory
        if use_shell:
            proc = subprocess.run(command, shell=True, capture_output=True, text=True)
        else:
            with open(input_file, 'r') as infile:
                proc = subprocess.run(command, stdin=infile, capture_output=True, text=True)

        output = proc.stdout.rstrip('\n')
        expected_output = expectedfile.read().rstrip('\n')

        if output != expected_output or proc.returncode != 0:
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
            test_type = parts[1]

            input_files = None
            additional_args = []

            if test_name == 'wc' and '_' in parts[1]:
                file_parts = parts[1].split('_')
                flagvalue = file_parts[0]  # Extracting flag values
                input_files = [os.path.join(test_dir, f'{name}.in') for name in file_parts[1:]]  # Extracting file names

                if 'l' in flagvalue:
                    additional_args.append('-l')
                if 'w' in flagvalue:
                    additional_args.append('-w')
                if 'c' in flagvalue:
                    additional_args.append('-c')
            else:
                input_files = os.path.join(test_dir, filename)

            expected_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.out')
            expected_arg_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.arg.out')


            if len(parts) > 3:
                flag_and_value = parts[2]
                flag_parts = flag_and_value.split('_')
                if len(flag_parts) == 2:
                    flag, flag_value = flag_parts
                    additional_args = [f'--{flag}', flag_value]

            expected_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.out')
            expected_arg_output_file = os.path.join(test_dir, f'{test_name}.{test_type}.arg.out')

            # Run test in STDIN/Shell mode
            passed, output, expected_output = run_test(prog_dir, test_name, input_files, expected_output_file, False, additional_args)
            if not passed:
                print(f"FAIL: {test_name} failed in file mode (TestResult.OutputMismatch)\n"
                      f"      expected:\n{expected_output}\n\n"
                      f"           got:\n{output}\n")
                test_results['OutputMismatch'] += 1
            else:
                test_results['OK'] += 1

            # Run test in argument mode
            passed, output, expected_output = run_test(prog_dir, test_name, input_files, expected_arg_output_file, True, additional_args)
            if not passed:
                print(f"FAIL: {test_name} failed in argument/shell mode (TestResult.OutputMismatch)\n"
                        f"      expected:\n{expected_output}\n\n"
                        f"           got:\n{output}\n")
                test_results['OutputMismatch'] += 1
            else:
                test_results['OK'] += 1

            test_results['total'] += 2

    # Print summary
    print(f"\nOK: {test_results['OK']}\noutput mismatch: {test_results['OutputMismatch']}\ntotal: {test_results['total']}")

    if test_results['OutputMismatch'] > 0:
        exit(1)

if __name__ == "__main__":
    main()
