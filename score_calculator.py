import math
import numpy as np

def accuracy_score(note, perfect_notes, good_notes):
    score_per_note_base = 900000 / int(note)
    perfect_note_score = score_per_note_base
    good_note_score = score_per_note_base * 0.5
    player_accuracy_score = int(perfect_notes) * float(perfect_note_score) + int(good_notes) * float(good_note_score)
    return player_accuracy_score

def combo_score(note, max_combo):
    combo_score_per_note_base = 100000 / int(note)
    player_combo_score = int(max_combo) * float(combo_score_per_note_base)
    return player_combo_score
    

notes_no = int(input())
perfect_notes_no = int(input())
good_notes_no = int(input())
missed_notes = notes_no - perfect_notes_no - good_notes_no
max_combo_number = int(input())
print(missed_notes)

if max_combo_number > notes_no:
    print("Invalid input")
if max_combo_number < (notes_no - missed_notes) / missed_notes:
    print("Invalid input")

print("Number of notes: " + str(notes_no))
print("Number of perfect notes: " + str(perfect_notes_no))
print("Number of good notes: " + str(good_notes_no))
print("Longest Streak: " + str(max_combo_number))

player_accuracy_score = accuracy_score(notes_no, perfect_notes_no, good_notes_no) 
player_combo_score = combo_score(notes_no, max_combo_number)
print(str(player_accuracy_score))
print(str(player_combo_score))
player_total_score = float(player_accuracy_score) + float(player_combo_score)
print(str(player_total_score))