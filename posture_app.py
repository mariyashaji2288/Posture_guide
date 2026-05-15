 if face_top_rel < 0.12:
    label = "Leaning Back"

elif face_top_rel > 0.42:
    label = "Slouching"

else:
    label = "Good Posture"
