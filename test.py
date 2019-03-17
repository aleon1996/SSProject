import re

#pattern = ".Ariana Grande.God is a woman."
pattern = '.*Ariana Grande.*God is a woman.*'
pattern1 = '.*God is a woman.*'
text1 = "the new song by Ariana Grande God is a woman is sooooo good"
text2 = "Ariana Grande's new song God is a woman "
text3 = "song by ariana grande God is a woman"
text4 = "God is a woman is a great song"
text5 = "God and Jesus"
print(re.search(pattern1, text5))
