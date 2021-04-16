#set dont allow duplicates
#set has no indexing
#so random access is not possible

seta={345,345,24,535,24,536,23456,6,"Jay","Pot"}

print(seta)
#print(seta[4])

for x in seta:
    print(x)

seta.add("Noh")
print(seta)