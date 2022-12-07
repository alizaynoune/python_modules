class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        # ... Your code here ...
        self.file_obj = open(filename)
        print('<<<<<')

    def __enter__(self):
        # ... Your code here ...
        print('enter')
        return None

    def __exit__(self, type, value, traceback):
        # ... Your code here ...
        print('exit', value)
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        # ... Your code here ...

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        # ... Your code here ...


if __name__ == "__main__":
    with CsvReader('good.csv2') as file:
        print(file)
        # data = file.getdata()
        # header = file.getheader()
