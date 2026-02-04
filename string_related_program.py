s1 = "Hello"
s2 = 'v sri siddarth'
s3 = """Welcome to python class"""

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print()

print("First character of s1:", s1[0])        
print("Last character of s1:", s1[-1])        
print()


s4 = s1 + " " + s2
print("Concatenation (s1 + ' ' + s2):", s4)

s5 = s1 * 3
print("Repetition (s1 * 3):", s5)


print("Length of s3:", len(s3))


print("'Py' in s2?", "Py" in s2)
print("'java' not in s2?", "java" not in s2)
print()


text = "Programming"
print("text =", text)

print("text[0:4]   =", text[0:4])     
print("text[3:]    =", text[3:])      
print("text[:5]    =", text[:5])      
print("text[-4:]   =", text[-4:])     
print("text[::2]   =", text[::2])     
print("text[::-1]  =", text[::-1])    
print()


sample = "   hello python world   "
print("Original sample: '", sample, "'", sep="")


print("strip()  -> '", sample.strip(), "'", sep="")


print("upper()   ->", sample.upper())
print("lower()   ->", sample.lower())

print("replace('python', 'Java') ->", sample.replace("python", "Java"))


words = sample.strip().split()
print("split() ->", words)

joined = "-".join(words)
print("'-'.join(words) ->", joined)


print("find('python') ->", sample.find("python"))


print("count('l') ->", sample.count("l"))

print("startswith('   he') ->", sample.startswith("   he"))
print("endswith('world   ') ->", sample.endswith("world   "))


only_letters = "HelloWorld"
only_digits = "12345"
print("'HelloWorld'.isalpha() ->", only_letters.isalpha())
print("'12345'.isdigit() ->", only_digits.isdigit())          



output
s1 = Hello
s2 = v sri siddarth
s3 = Welcome to python class

First character of s1: H
Last character of s1: o

Concatenation (s1 + ' ' + s2): Hello v sri siddarth
Repetition (s1 * 3): HelloHelloHello
Length of s3: 23
'Py' in s2? False
'java' not in s2? True

text = Programming
text[0:4]   = Prog
text[3:]    = gramming
text[:5]    = Progr
text[-4:]   = ming
text[::2]   = Pormig
text[::-1]  = gnimmargorP

Original sample: '   hello python world   '
strip()       -> 'hello python world'
upper()       ->    HELLO PYTHON WORLD   
lower()       ->    hello python world   
replace('python', 'Java') ->    hello Java world   
split() -> ['hello', 'python', 'world']
'-'.join(words) -> hello-python-world
find('python') -> 9
count('l') -> 3
startswith('   he') -> True
endswith('world   ') -> True
'HelloWorld'.isalpha() -> True
'12345'.isdigit() -> True
