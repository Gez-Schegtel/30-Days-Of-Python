# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string.
string1 = " ".join(["Thirty", "Days", "Of", "Python"])
print("1.", string1)
print()

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string.
string2 = " ".join(["Coding", "For", "All"])
print("2.", string2)
print()

# 3. Declare a variable named company and assign it to "Coding For All".
company = "Coding For All"
print(f"3. The company variable contains the following value: {company}")
print()

# 4. Print the variable company.
print("4.", company)
print()

# 5. Print the length of the company string using len().
print("5. Length of company:", len(company))
print()

# 6. Change all the characters to uppercase letters.
print("6. Uppercase:", company.upper())
print()

# 7. Change all the characters to lowercase letters.
print("7. Lowercase:", company.lower())
print()

# 8. Use capitalize(), title(), swapcase() methods to format the string.
print("8. Capitalize:", company.capitalize())
print("   Title:     ", company.title())
print("   Swapcase:  ", company.swapcase())
print()

# 9. Cut (slice) out the first word of "Coding For All".
first_space = company.find(" ")
sliced_company = company[first_space + 1:]
print("9. Without first word:", sliced_company)
print()

# 10. Check if "Coding For All" contains the word "Coding" (using find/index).
index_coding = company.find("Coding")  # devuelve 0 si se encuentra al inicio
print("10. 'Coding' found at index:", index_coding)
print()

# 11. Replace the word "Coding" in "Coding For All" with "Python".
replaced_company = company.replace("Coding", "Python")
print("11. Replaced:", replaced_company)
print()

# 12. Change "Python for Everyone" to "Python for All" using replace.
phrase = "Python for Everyone"
changed_phrase = phrase.replace("Everyone", "All")
print("12. Changed phrase:", changed_phrase)
print()

# 13. Split the string "Coding For All" using space as the separator.
split_company = company.split(" ")
print("13. Split:", split_company)
print()

# 14. Split "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma.
companies_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies_str.split(", ")
print("14. Split companies:", split_companies)
print()

# 15. What is the character at index 0 in the string "Coding For All"?
print("15. Character at index 0:", company[0])
print()

# 16. What is the last index of the string "Coding For All"?
last_index = len(company) - 1
print("16. Last index:", last_index)
print()

# 17. What character is at index 10 in "Coding For All"?
print("17. Character at index 10:", company[10])
print()

# 18. Create an acronym for the name "Python For Everyone".
acronym_pfe = "".join(word[0] for word in "Python For Everyone".split())
print("18. Acronym for 'Python For Everyone':", acronym_pfe)
print()

# 19. Create an acronym for the name "Coding For All".
acronym_cfa = "".join(word[0] for word in company.split())
print("19. Acronym for 'Coding For All':", acronym_cfa)
print()

# 20. Use index to determine the position of the first occurrence of 'C' in "Coding For All".
pos_C = company.index("C")
print("20. Position of 'C':", pos_C)
print()

# 21. Use index to determine the position of the first occurrence of 'F' in "Coding For All".
pos_F = company.index("F")
print("21. Position of 'F':", pos_F)
print()

# 22. Use rfind to determine the position of the last occurrence of 'l' in "Coding For All People".
string22 = "Coding For All People"
last_l_index = string22.rfind("l")
print("22. Last occurrence of 'l' in 'Coding For All People':", last_l_index)
print()

# Define the sentence used for the next exercises.
sentence = "You cannot end a sentence with because because because is a conjunction"

# 23. Use index or find to find the position of the first occurrence of the word 'because'.
pos_because_first = sentence.find("because")
print("23. First occurrence of 'because':", pos_because_first)
print()

# 24. Use rindex to find the position of the last occurrence of the word 'because'.
pos_because_last = sentence.rindex("because")
print("24. Last occurrence of 'because':", pos_because_last)
print()

# 25. Slice out the phrase 'because because because' from the sentence.
phrase_to_slice = "because because because"
start_slice = sentence.find(phrase_to_slice)
sliced_phrase = sentence[start_slice:start_slice + len(phrase_to_slice)]
print("25. Sliced phrase:", sliced_phrase)
print()

# 26. Find the position of the first occurrence of the word 'because' (again).
pos_because_first_again = sentence.find("because")
print("26. First occurrence of 'because' (again):", pos_because_first_again)
print()

# 27. Slice out the phrase 'because because because' (again).
sliced_phrase_again = sentence[start_slice:start_slice + len(phrase_to_slice)]
print("27. Sliced phrase (again):", sliced_phrase_again)
print()

# 28. Does "Coding For All" start with the substring "Coding"?
print("28. Starts with 'Coding'?", company.startswith("Coding"))
print()

# 29. Does "Coding For All" end with the substring "coding"?
print("29. Ends with 'coding'?", company.endswith("coding"))
print()

# 30. Remove the left and right trailing spaces from "   Coding For All      ".
string_with_spaces = "   Coding For All      "
trimmed_string = string_with_spaces.strip()
print("30. Trimmed string:", repr(trimmed_string))
print()

# 31. Check which of the following variables return True when using isidentifier().
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print("31. Is '30DaysOfPython' an identifier?", var1.isidentifier())
print("    Is 'thirty_days_of_python' an identifier?", var2.isidentifier())
print()

# 32. Join the list of python libraries with a hash and space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = "# ".join(libraries)
print("32. Joined libraries:", joined_libraries)
print()

# 33. Use the new line escape sequence to separate the sentences.
multiline_text = "I am enjoying this challenge.\nI just wonder what is next."
print("33. New line separated sentences:\n", multiline_text)
print()

# 34. Use a tab escape sequence to write the following lines.
tabbed_text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print("34. Tab separated lines:\n", tabbed_text)
print()

# 35. Use string formatting to display the area of a circle.
radius = 10
area = 3.14 * radius ** 2
print("35. The area of a circle with radius {} is {} meters square.".format(radius, int(area)))
print()

# 36. Use string formatting methods to display arithmetic operations.
a, b = 8, 6
print("36. {} + {} = {}".format(a, b, a + b))
print("    {} - {} = {}".format(a, b, a - b))
print("    {} * {} = {}".format(a, b, a * b))
print("    {} / {} = {:.2f}".format(a, b, a / b))
print("    {} % {} = {}".format(a, b, a % b))
print("    {} // {} = {}".format(a, b, a // b))
print("    {} ** {} = {}".format(a, b, a ** b))
print()

