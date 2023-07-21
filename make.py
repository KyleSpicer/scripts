#!/usr/bin/env python3.10

import argparse
import sys
import subprocess
import time

loop_dir = "for filename in $(find . -name '*.py'); do "
end = "; done"
dev_null = ' > /dev/null'


def make_text_bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def test_file():
    for num in range(49):
        subprocess.run(f'python3 pypeople.py --ancestors {num} -l' , shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --descendants {num}' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --parents {num} -l' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --siblings {num} -l' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --ancestors {num}' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --cousins {num} -l'  + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --details {num} -l'  + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --id 2'  + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --search first_name=Guido'  + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --role d soldier farmer none' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --crops sd turnips tomatoes' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --intermarriage turnips tomatoes' + dev_null, shell=True, check=True)
        # subprocess.run(f'python3 pypeople.py --marriages -l' + dev_null , shell=True, check=True)
        time.sleep(.5)
        subprocess.run(f'clear', shell=True, check=True)
    print('Success')


commands = {
    "test": [f"python3 -m unittest discover test"],
    "clean": ["rm -rf venv __pychache__/*", 'rm classes.png'],
    "mypy": [loop_dir + 'echo $filename; mypy $filename' + end],
    "mypy_s": [loop_dir + 'echo $filename; mypy $filename --check-untyped-defs' + end],
    "format": [loop_dir + 'autopep8 --in-place --aggressive $filename' + end],
    "style": [loop_dir + 'pycodestyle $filename' + end],
    "indent": ['indent -linux ./src/*.c ./src/*.h', 'rm -f ./src/*.c~ ./src/*.h~'],    
    "clang_format": ['echo clang-format --style=Microsoft'],    
    "compileall": ['python -m compileall'],
    "uml": ['touch __init__.py', 'pyreverse -o png .', 'open classes.png',
            'rm packages.png'],
    "test_nums": [test_file],

}


def run_command(command, arg):
    match arg:
        case 'test':
            print(make_text_bold('----- RUNNING UNITTEST -----\n'))
        case 'clean':
            print(f'Cleaning pycache and classes.png')
        case 'mypy':
            print(f'Mypy on dir')
        case 'mypy_s':
            print(f'Strict Mypy on dir')
        case 'format':
            print(f'autopep8')
        case 'test_nums':
            print(f'test_nums')
            command()
            return

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print('Errors found')

def arg_parse():
    parser = argparse.ArgumentParser(
        description="Run commands similar to a make file.")
    parser.add_argument("command", choices=commands.keys(),
                        help="The command to run.")

    args = parser.parse_args()

    for cmd in commands[args.command]:
        run_command(cmd, args.command)


def main():
    try:
        arg_parse()
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
