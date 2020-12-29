text = " web Development graduate certificate program." \
       "focuses on the development of websites and web services " \
       "for multiple environments including database-driven programming, " \
       "content management and mobile services. A combination of conceptual " \
       "and practical training will prepare you to execute effective, efficient " \
       "website design."
text = text.lower()
print(text[2])
"l" in text
text_1 = list(text.split())
out = text_1.pop(7)
print(text_1, out)
print(text_1)
unique_worlds = set(text_1)
print(unique_worlds)
len(unique_worlds)
print(text_1.count("web"))
print(len(text_1))
