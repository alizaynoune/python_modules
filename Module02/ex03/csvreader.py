import sys


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.file_obj = open(filename, 'r')
            self.sep = sep
            self.header = header
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            self.data = []
        except Exception:
            self.file_obj = None

    def __enter__(self):
        if not self.file_obj:
            return None
        lines = self.file_obj.readlines()
        self.data = [[ls for ls in l.strip().split(self.sep)]
                     for l in lines]
        hLen = len(self.data[0])
        for i in self.data:
            if len(i) != hLen or not all(len(l) for l in i):
                return None
        return self

    def __exit__(self, type, value, traceback):
        if self.file_obj:
            self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        if self.file_obj:
            start = self.skip_top + 1 if self.header else self.skip_top
            end = len(self.data) - self.skip_bottom
            return self.data[start:end]
        return None

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header:
            return self.data[0]
        return None


if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")

    with CsvReader(filename, header=True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")
