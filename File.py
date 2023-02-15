import pandas as pd

class File:
    """
    Class used to manage the data and transformations
    """
    is_full = None
    file = None
    undo_step_file = None
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(File, cls).__new__(cls)
        return cls.instance


    def read_excel(self, file):
        if not self.is_full:
            self.is_full = True
            self.file = pd.read_excel(file)

    def get_file(self):
        return self.file

    def delete_column(self, column_name):
        self.undo_step_file = self.file
        self.file = self.file.drop(columns=column_name)
