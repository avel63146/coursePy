import re
import codecs
import binascii
mystery = '\U0001f4a9'
print(mystery)
pop_bytes = mystery.encode('UTF-8')
print(pop_bytes)
pop_string = pop_bytes.decode('UTF-8')
print(pop_string)
print(mystery == pop_string)

roast = 'roast beef'
ham = 'ham'
head = 'head'
clam = 'clam'
poem = '''
    My kitty cat likes %s
    My kitty cat likes %s
    My kitty cat fell on his %s
    And now thinks hes a %s
'''%(roast, ham, head, clam)
print(poem)

response = {'salutation': 'qq', 'name': 'Taras', 'product': 'molok', 'verbed': 'qq', 'room': 'kitchen',
'animals': 'LEv', 'amount': '222', 'percent': '22', 'spokesman': 's11', 'job_title': 'Nice'}

letter = '''
Dear {0[salutation]} {0[name]},
Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your
{0[room]}. Please note that it should never be used in a {0[room]}, especially
near any {0[animals]}.
Send us your receipt and {0[amount]} for shipping and handling. We will send
you another {0[product]} that, in our tests, is {0[percent]}% less likely to
have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}
'''
print(letter.format(response))
mamoth = '''
        We have seen thee, queen of cheese,
        Lying quietly at your ease,
        Gently fanned by evening breeze,
        Thy fair form no flies dare seize.
        All gaily dressed soon you'll go
        To the great Provincial show,
        To be admired by many a beau
        In the city of Toronto.
        Cows numerous as a swarm of bees,
        Or as the leaves upon the trees,
        It did require to make thee please,
        And stand unrivalled, queen of cheese.
        May you not receive a scar as
        We have heard that Mr. Harris
        Intends to send you off as far as
        The great world's show at Paris.
        Of the youth beware of these,
        For some of them might rudely squeeze
        And bite your cheek, then songs or glees
        We could not sing, oh! queen of cheese.
        We'rt thou suspended from balloon,
        You'd cast a shade even at noon,
        Folks would think it was the moon
        About to fall and crush them soon.
'''
print(re.findall(r'c.\w*|C.\w+', mamoth))
print(re.findall(r'c...\b|C...\b', mamoth))
print(re.findall(r'\w+r\b', mamoth))
print(re.findall(r'\w+[AEIOUaeiou][AEIOUaeiou][AEIOUaeiou]\w+', mamoth))

gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9'+'0401000000002c000000000100010000020144003b')
print(gif)
