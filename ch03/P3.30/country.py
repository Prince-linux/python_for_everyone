#Question: P3.30:  French country names are feminine when they end with the letter e, 
#masculine oth­erwise, except for the following which are masculine even though they end with e:
#• le Belize
#• le Cambodge
#• le Mexique
#• le Mozambique
#• le Zaïre
#• le Zimbabwe
#Write a program that reads the French name of a country and adds the article: le for masculine 
#or la for feminine, such as le Canada or la Belgique.
#However, if the country name starts with a vowel, use l’; for example, l’Afghanistan. 
#For the following plural country names, use les:
#• les Etats­Unis
#• les Pays­Bas

#Author: Prince Oppong Boamah<regioths@gmail.com>
#Date: 1st March, 2019

country = input("Please enter a country name: ")
vowel = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u')

if country == 'EtatsUnis' or country == 'PaysBas':
	print('les ' + country)
elif country.startswith(vowel):
	print("l'" + country)
elif country == 'Belize' or country == 'Cambodge' or country == 'Mexique' or country == 'Mozambique' or country == 'Zaïre' or country == 'Zimbabwe':
	print('le ' + country)
elif country.endswith('a'):
	print('le ' + country)
elif country.endswith('e'):
	print('la ' + country)
else:
	print('Wrong Country name')



