# BASIC IMPLEMENTATION OF REGULAR EXPRESSION...
# import re
# phone_num_pattern_ob = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# match_obj = phone_num_pattern_ob.search('My number is 415-555-4242')
# print(match_oprint(bj.group()))



# GROUPING WITH PARENTHESIS...
# import re
# phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})') # 2 groups made based on parenthesis
# mo = phone_re.search('My number is 415-555-4242')
# print(print(mo.group())) # Full
# print(print(mo.group(0))) # Full
# print(print(mo.group(1))) # 1print(st group
# )print(print(mo.group(2))) # 2print(nd group
# )# there exist no more groups... asking fprint(or group wo)uld raise an error!
# print(mo.groups()) # all groups at once

# area_code, main_number = mo.groups()
# print('area code =', area_code)
# print('main number =', main_number)



# # USING ESCAPE CHARACTERS...
# # sample phone number (415) 555-4242
# import re
# pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # escape characters through backslash '\' here to include parenthesis characters on purpose :)
# mo = pattern.search('My phone number is (415) 555-4242.')
# print(print(mo.group())) # Whole
# print(print(mo.group(0))) # Whole
# print(print(mo.group(1))) # 1print(st group
# )print(print(mo.group(2))) # 2print(nd group
# )print(mo.groups()) # All the groups at once



# # Matching Characters from Alternate Groups
# import re
# pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)') # mentioning 'Cat' as a prefix only once 
# mo = pattern.search('Catch me if you can.')

# try:
#     print(mo.group())
#     print(mo.group(1))
#     print(mo.groups())
# except AttributeError:
#     print(f'\'NoneType\' object has no attribute \'group\', here search function returns \'None\' since there is no match present in the input string :(')



# Returning All Matches

# import re
# pattern = re.compile(r'\d{3}-\d{3}-\d{4} | \(\d{3}\) \d{3}-\d{4}') # this regex has no groups.
# print(pattern.findall('My personal numbers are 123-456-7890 or 696-969-6767 and my official number is (987) 654-3210'))

# import re
# pattern = r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))|(\(\d\d\d\)) (\d\d\d-\d\d\d\d)' # this regex has groups
# x = [m.groups() for m in re.finditer(pattern, 'Cell: 415-555-4242 or (111) 234-5678, Work: 212-555-0000')]
# print([tuple(item.strip() for item in g[1:] if item is not None) for g in x])