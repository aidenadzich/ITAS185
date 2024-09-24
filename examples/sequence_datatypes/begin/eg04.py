star_wars_species = {'Human': 'Luke Skywalker', 'Tugruta': 'Ahsoka Tano', 'Gungan': 'Jar Jar Binks', 'Wookie': 'Chewbacca'}

# Print the dictionary
print(star_wars_species)
print(star_wars_species['Gungan'])
print(star_wars_species.get('Hutt', 'Species not found!'))

star_wars_jedi = {
    "Luke Skywalker": {
        "species": 'Human',
        'saber_colour': 'Green',
        'homeworld': 'Tatooine',
        'master': 'Obi-Wan Kenobi (Old Ben)',
        'apprentice': ['Leia Organa', 'Grogu', 'Ben Solo']
    },
    "Mace Windu": {
        "species": 'Human',
        'saber_colour': 'Purple',
        'homeworld': 'Haruun Kal',
        'master': 'Cyslin Myr'  
    }
}
print(star_wars_jedi)
print(star_wars_jedi.get('Luke Skywalker'))
print(star_wars_jedi['Mace Windu']['saber_colour'])
print(star_wars_jedi['Luke Skywalker']['apprentice'][3])