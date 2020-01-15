import math
import numpy as np

def accuracy_score(note, perfect_notes, good_notes, bad_notes):
    score_per_note_base = 900000 / int(note)
    perfect_note_score = score_per_note_base
    good_note_score = score_per_note_base * 0.7
    bad_note_score = score_per_note_base * 0.3
    player_accuracy_score = int(perfect_notes) * float(perfect_note_score) + int(good_notes) * float(good_note_score) + int(bad_notes) * float(bad_note_score)
    return player_accuracy_score

notes_no = int(input("Number of notes: " ))
perfect_notes_no = int(input("Number of perfect notes: "))
good_notes_no = int(input("Number of good notes: "))
bad_notes_no = int(input("Number of bad notes: "))
missed_notes = notes_no - perfect_notes_no - good_notes_no - bad_notes_no
combo_breaks = bad_notes_no + missed_notes
print("Number of missed notes: " + str(missed_notes))
print("Number of combo breaks: " + str(combo_breaks))

def combo_score_by_streak_base(note, combo):
    combo_score_per_note_base = 100000 / ((int(note) - 1) * int(note) / 2) * (int(combo) - 1)
    return combo_score_per_note_base
    
streaks = list(map(int,input("Enter your streak: ").strip().split()))[:(combo_breaks + 1)]
max_combo_number = max(streaks)
if len(streaks) > int(combo_breaks + 1):
    print("Invalid input.")
elif max_combo_number > notes_no:
    print("Invalid input")
elif combo_breaks > 0:
    if max_combo_number < (notes_no - combo_breaks) / combo_breaks:
        print("Invalid input")
else:
    print(max_combo_number)
    print(streaks)

individual_combo = []
for streak in streaks:
    for number in range(1, streak + 1):
        individual_combo.append(number)

print(individual_combo)

def combo_score(individual_combo):
    score = 0
    for number in individual_combo:
        score += combo_score_by_streak_base(notes_no, number)
    return score

#print("Number of notes: " + str(notes_no))
#print("Number of perfect notes: " + str(perfect_notes_no))
#print("Number of good notes: " + str(good_notes_no))
#print("Number of bad notes: " + str(bad_notes_no))
#print("Longest Streak: " + str(max_combo_number))

player_accuracy_score = accuracy_score(notes_no, perfect_notes_no, good_notes_no, bad_notes_no) 
player_combo_score = combo_score(individual_combo)
print(str(float(player_accuracy_score)))
print(str(float(player_combo_score)))
player_total_score = float(player_accuracy_score) + float(player_combo_score)
print(str(player_total_score))