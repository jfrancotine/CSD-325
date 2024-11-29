#Jose Franco
#11/28/2024
#Assignment 7.2 - Test Cases


#Function that returns a string in the format 'City, Country - population xxx, Language'
#if both population and language are provided.
#handles cases where population and/or language may be missing.

def city_country(city, country, population=None, language=None):
    countryinfo = f"{city}, {country}"
    if population:
        countryinfo += f" - population {population}"
    if language:
        countryinfo += f", {language}"
    return countryinfo

# Function calls
print(city_country("Rome", "Italy"))
print(city_country("Caracas", "Venezuela", 2991000))
print(city_country("Dallas", "United States", 1302000, "English"))
