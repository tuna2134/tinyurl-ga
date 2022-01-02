from .main import create
from sys import argv

def main():
    result = create(argv[0])
    print(result.url)
