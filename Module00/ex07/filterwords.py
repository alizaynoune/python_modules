import sys
import re

if len(sys.argv) == 3:
    if not sys.argv[2].isnumeric():
        sys.exit('Error')
    minLen = int(sys.argv[2])
    new_list = re.sub(r'[^\w\s]', '', sys.argv[1]).split()
    test = ['done', 'test']
    print([c for c in new_list if len(c) > minLen])

else:
    sys.exit('Error')
