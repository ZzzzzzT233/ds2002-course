#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me an adjective: " ADJ2
read -p "3. Please give me a noun: " NOUN1
read -p "4. Please give me a noun: " NOUN2
read -p "5. Please give me a verb: " VERB1
read -p "6. Please give me a verb: " VERB2
read -p "7. Please give me an adverb: " ADV1
read -p "8. Please give me an adverb: " ADV2


echo "This weekend I am going camping with $NOUN1. I packed my lantern, sleeping bag, and "
echo "$NOUN2. I am so $ADJ1 to $VERB1 $ADV2 in a tent. I am also $ADJ2 to $VERB2 $ADV1 while hiking." 

