release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
#print (release_year_dict)
#print (release_year_dict['Thriller'])
#print(release_year_dict.keys())
print(release_year_dict.values())

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)

# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict