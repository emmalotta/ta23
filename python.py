# ( up #
# ) down #

fail = open("asi.txt")

a = fail.read()

print(a.count("(") - a.count(")"))

