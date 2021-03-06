"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""
name = raw_input("Enter file:")
if len(name) == 0 : name = "mbox-short.txt"

handle = open(name)

counts = dict()
list = list()

for line in handle:
	if not line.startswith('From '): continue
	words = line.split()
	time = words[5].split(':')
	hours = time[0]
	counts[hours] = counts.get(hours, 0) + 1
	
for key, value in counts.items():
    list.append((key,value))

for key, value in sorted(counts.items()):
    print key, value