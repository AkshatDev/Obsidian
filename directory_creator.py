# This script creates a directory structure for a given book.

import os
import sys
from structures import structure, genres

class CreateDirectory:
    def __init__(self,genre, book_name,path=None):
        try:
            if not book_name:
                raise Exception("Book name is required")
            if genre not in genres:
                raise Exception("Invalid genre")
            self.book_name = book_name
            self.genre = genre
            self.path = path if path else os.getcwd()
            self.path = os.path.join(self.path, self.genre)
            
            print(f'Will create directory at: {self.path}/{self.book_name}')

        except Exception as e:
            print(f'Cannot create directory: {e}')
            sys.exit(1)
    def create_directory(self):
        try:
            #create director path/book_name
            os.makedirs(os.path.join(self.path, self.book_name))
            # create subdirectories in the book_name directory
            creation_path = os.path.join(self.path, self.book_name)
            for key, value in structure.items():
                os.makedirs(os.path.join(creation_path, key))
                for file in value:
                    with open(os.path.join(creation_path, key, str(self.book_name + file)), 'w') as f:
                        f.write(f'# {key}\n')
        except Exception as e:
            print(f'Cannot create directory: {e}')
            sys.exit(1)


if __name__ == "__main__":
    obj = CreateDirectory("Man's_Search_for_Meaning")
    obj.create_directory()