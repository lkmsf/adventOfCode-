import sys
sys.path.append("../")
import subprocess 
from pathlib import Path


def run_code(code_file, data_file): 
    subprocess.run(
        ["python3", code_file, data_file],
        stdout=None,   # inherit parent stdout
        stderr=None,   # inherit parent stderr
        check=True,
    )

def run_tests(code_file): 
	test_files = ["tests/" + p.name for p in Path("tests").iterdir() if p.is_file()]
	test_files.append('data.in')
	for test_file in test_files:
		print(f"FILE IS {test_file}")
		run_code(code_file, test_file)
		input()