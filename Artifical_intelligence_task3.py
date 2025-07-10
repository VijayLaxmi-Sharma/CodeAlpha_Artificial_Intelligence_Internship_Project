import mido
from mido import MidiFile, MidiTrack, Message
import random
import pygame
import time

# 🎵 Define scale notes (C Major)
scale_notes = [60, 62, 64, 65, 67, 69, 71, 72]

# 🎼 Create MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 🕒 Add notes with timing
for _ in range(100):
    note = random.choice(scale_notes)
    velocity = random.randint(60, 100)
    duration = random.randint(200, 400)
    gap = random.randint(100, 300)

    track.append(Message('note_on', note=note, velocity=velocity, time=gap))
    track.append(Message('note_off', note=note, velocity=velocity, time=duration))

# 💾 Save file
midi_filename = "simple_generated_music.mid"
mid.save(midi_filename)
print("🎉 Corrected music saved successfully!")

# 🔊 Playback using pygame
pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load(midi_filename)
    pygame.mixer.music.play()
    print("🔈 Playing your generated music...")

    # ⏳ Wait until it finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

except Exception as e:
    
    print("⚠️ Error during playback:", e)

pygame.quit()
