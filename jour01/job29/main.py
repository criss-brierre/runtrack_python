def rounded_list_for_notes(notes):
    for i in range(len(notes)):
        if (notes[i] % 5 >= 3):
            notes[i] = notes[i] - notes[i] % 5 + 5
    print(notes)

rounded_list_for_notes([24, 20, 57, 93, 98, 68])