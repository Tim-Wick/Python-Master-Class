a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(13) + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \\followed by some text"
# Need two backslashes to actually print a backslash
print(backslash_string)

backslash_string_raw = r"or you can use a raw string\ to use a backslash"
# But don't end with a backslash! Need double backslash to end a string with a backslash
print(backslash_string_raw)
