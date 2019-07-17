s = input('')
 
if (s>='a' and s<='z') or (s>='A' and s<='Z'):
 
    if s in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
	    print('Vowel')
    else:
	    print('Consonant')
 
else:
    print('invalid')
