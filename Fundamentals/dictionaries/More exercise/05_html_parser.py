import re

some_string = input()

title_match = re.search(r"(<title>(?P<title>.+)</title>)", some_string).groupdict()
title = re.sub(r"(<[^>]+>)", "", title_match["title"])
title = re.sub(r"\\n", "", title)

content_match = re.search(r"<body>(?P<content>.+)</body>", some_string).groupdict()
content = re.sub(r"(<[^>]+>)", "", content_match["content"])
content = re.sub(r"\\n", "", content)

print(f"Title: {title}")
print(f"Content: {content}")
