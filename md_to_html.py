import sys
import markdown

inputpath = (sys.argv[1])
outputpath = (sys.argv[2])

with open(inputpath, encoding="utf-8") as f:
    contents = f.read()

html = markdown.markdown(contents)

with open(outputpath, "w", encoding="utf-8") as f:
    f.write(html)
