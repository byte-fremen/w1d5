Caesar's Cipher
================

[Caesar's Cipher](http://en.wikipedia.org/wiki/Caesar_cipher) is named after Julius Caesar, who used it with a shift of three to protect messages of military significance.

A shift of three to the right would change the letters thusly:

	A => D
	B => E
	C => F
	...
	Z => C

A shift of three to the left would change the letters... 

	A => X 
	B => Y 
	C => Z
	D => A
	...

Of course this offers no communication security whatsoever - except in Roman times when most people couldn't read to begin with.

But the Caesar Cipher is [still used](http://en.wikipedia.org/wiki/ROT13) in cryptography, in addition to many other methods. So this is your first step into the world of security and data encryption.

To understand how to complete this challenge, you must first understand the [ASCII](http://en.wikipedia.org/wiki/ASCII) standard. In short, every key on your keyboard has an [assigned numeric value](http://www.asciitable.com/).

In Python, we use the following methods to get the ASCII decimal value.
```python
		ord('a') # => 97
		ord('A') # => 65
		ord('x') # => 120
```

To get the ASCII character from an integer, we use the `chr` function.
```python
		chr(97) # => 'a'
		chr(65) # => 'A'
		chr(32) # => ' ' (Yes that's an empty space, it has a value too!)
```
[Check out this video for some extra help understanding the Caesar Cipher](https://youtu.be/36xNpbosfTY).
#### Round 1

Write the `caesar` function that takes two inputs. The first input is a a message as a string. The second input is an integer, which is the number used for shifting in the Caesar Cipher. the `caesar` function should return the shifted message as a string.

Make sure you ignore spaces, symbols, and numbers. The end user wants to see these characters unchanged in the encrypted cipher. Capital letters should remain capital, and lower case letters should remain lower case.

#### Round 2
Create a new decrypt function. Again, you'll take two inputs. The first is analready encrypted string, the second input is shift number, The function should return the decrypted message as a string. 

#### Round 3

Using Python's `assert` write at least 6 tests to test your code output.

#### Extra Resources
[CS50 video about how a Caesar Cipher works](https://youtu.be/36xNpbosfTY).