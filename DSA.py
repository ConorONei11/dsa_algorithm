# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:54:26 2022

@author: Con67
"""
#DSA algorithm
#Conor ONeill 40204711

#Setting parameter values, where p,q are prime and (p-1) mod q =0. 
#g is found using x**(p-1/q) mod p, where x is an integer >1, usually x = 2 is used
#a is private key, and A is public key
#k is chosen at random
p=307
q=17
g=(2**18) %p
a=11 
A=(g**a) %p 
k=15 #random

#Creating the hash function
def hash(word):
    asci=[0]*(len(word))
    z=0
    for i in range(len(word)):
        asci[i]=ord(word[i])
        z=z*32 + asci[i]
        h = z%2317
    return (h)

#The value h known as hash digest
#The example was used as a Wordle - so any 5 letter word will do 
h = hash('SHAKE')

#Signature function which uses the inputs to out put r and s
def signature(p,q,g,a,h,k):
    X=(g**k) %p
    r=X%q
    k**-1 %q
    s=k**(q-2) *(h +a*r)%q
    return(r,s)

print(signature(p,q,g,a,h,k))


(r,s)= signature(p,q,g,a,h,k)
#Verify r,s<q
#Verification function which verifies the message if from the correct sender if v-r=0.
def verification(p,q,g,A,h):
  w = s**(q-2) %q
  u1=h*w % q
  u2=r*w % q
  X=(g**u1)*(A**u2) % p
  v = X %q
  return(v-r)

print(verification(p, q, g, A, h))

#Verified if prints 0

