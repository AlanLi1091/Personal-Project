import math
import numpy as np

def score(note, perfect_notes, good_notes):
    score_per_note_base = 1000000 / int(note)
    perfect_note_score = score_per_note_base
    good_note_score = score_per_note_base * 0.5
    player_score = int(perfect_notes) * float(perfect_note_score) + int(good_notes) * float(good_note_score)
    return player_score

notes_no = input()
perfect_notes_no = input()
good_notes_no = input()
missed_notes = int(notes_no) - int(perfect_notes_no) - int(good_notes_no)

print("Number of notes: " + str(notes_no))
print("Number of perfect notes: " + str(perfect_notes_no))
print("Number of good notes: " + str(good_notes_no))

if missed_notes < 0:
    print("Invalid input.")
if (notes_no.isnumeric is False) or (notes_no.isdecimal is True): 
    print("Invalid input")
if (perfect_notes_no.isnumeric is False) or (perfect_notes_no.isdecimal is True):
    print("Invalid input")
if (good_notes_no.isnumeric is False) or (good_notes_no.isdecimal is True):
    print("Invalid input")

play_score = score(notes_no, perfect_notes_no, good_notes_no)
print(str(play_score))