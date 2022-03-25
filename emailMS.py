

from venv import create
from gmailAPI import create_message, main

res = create_message("a", "b", "c", "d")

print(res)

raw_string = create_message("esdg9t02@gmail.com", "hengweishin@gmail.com", "another email subject", "another hello world content")


main(raw_string)