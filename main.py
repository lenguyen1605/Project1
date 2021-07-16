# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', type=int)
    args = parser.parse_args()
    directory = "CatProject"

    parent_dir = '/Users/lenguyen/Desktop'
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.mkdir(path)

    for i in range(args.integers):
        location = os.path.join(path, 'cat' + str(i))

        r = requests.get('https://cataas.com/cat')
        with open(location, 'wb') as f:
            f.write(r.content)
   print(path)

    print(r.headers.get('content-type'))

if __name__ == '__main__':
    main()
