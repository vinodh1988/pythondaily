multiline="""
India has been a federal republic since 1950,
 governed in a democratic parliamentary system.
  It is a pluralistic, multilingual and multi-ethnic society. 
  India's population grew from 361 million in 1951 to 1.211 billion in 2011.[50] During the same time, its nominal per capita income increased from US$64 annually to US$1,498, and its literacy rate from 16.6% to 74%. From being a comparatively destitute country in 1951,[51] India has become a fast-growing major economy and a hub for information technology services, with an expanding middle class.[52] It has a space programme which includes several planned or completed extraterrestrial missions. Indian movies, music, and spiritual teachings play an increasing role in global culture
"""

"""
  this is 
  multiline comment
"""

print(multiline)
print(len(multiline))

for x in multiline:
    print(x, end=" ")

print(multiline[600:])
print(multiline[0::3])