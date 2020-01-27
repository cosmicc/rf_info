from random import randint
import subprocess
import sys

RAND_TESTS = 5

def randomtest(min, max):
    rand_tests = RAND_TESTS
    while rand_tests > 0:
        output = subprocess.run(['clear'], stdout=sys.stdout)
        random = randint(min, max)
        output = subprocess.run(['rf-info', str(random), 'hz', 'us'], stdout=sys.stdout)
        rand_tests -= 1
        print(' ')
        input('Return Code: {}'.format(output.returncode))

randomtest(1, 50_000)
randomtest(50_001, 100_000)
randomtest(100_001, 500_000)
randomtest(500_001, 1_000_000)
randomtest(1_000_001, 5_000_000)
randomtest(5_000_001, 999_000_000)
randomtest(999_000_001, 20_000_000_000)
randomtest(20_000_000_001, 999_999_999_999)
