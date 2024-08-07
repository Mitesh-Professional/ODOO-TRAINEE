import re

email = "mitesh123@gmail.com test@.com newTest@gmail otheremail@gmail.com"
# patten = r"[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}"
pattern = r"[\w._%+-]+@[\w-]+\.[A-Za-z]{2,3}"

print(re.findall(pattern,email))