import pandas as pd

class File:
    """
    Class used to manage the data and transformations
    """
    is_full = None
    file = None
    previous_step_file = None

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
        self.previous_step_file = self.file
        self.file = self.file.drop(columns=column_name)
    
    def undo(self):
        if isinstance(self.previous_step_file, pd.DataFrame):
            self.file = self.previous_step_file

    def apply_lowercase(self, column_name: str):
        if self.file.dtypes[column_name] != pd.StringDtype:
            return
        self.file[column_name] = self.file[column_name].str.lower()


    def apply_uppercase(self, column_name: str):
        if self.file.dtypes[column_name] != pd.StringDtype:
            return
        self.file[column_name] = self.file[column_name].str.upper()
            
            
