#!/usr/bin/env python
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
	"This is a long string.",
	"That is super long.",
	"Meh, So much to type.",
	"Fuck this exercise."
)
