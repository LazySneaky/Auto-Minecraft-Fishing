# Auto-Minecraft-Fishing
## still under construction lol

# 🎣 Minecraft Auto Fishing Bot

A Python-based bot that automatically detects fishing splash sounds in Minecraft and reels in the fish for you!

---

## ⚙️ How It Works

This bot listens to **in-game audio** using your PC's audio output (not your mic!) and reacts when it hears the splash sound of a fish biting.

---

## ❗ Important Notes

- 🔊 **Only works with Stereo Mix / loopback-supported audio devices.**  
  This allows the program to "hear" what's playing through your speakers (like Minecraft).
- 🎧 Will **not** work with microphone input or systems that don't support internal audio capture.

---

## ✅ Requirements

- Python 3.9+
- `sounddevice`
- `numpy`
- `pyautogui`

Install them with:

```bash
pip install sounddevice numpy pyautogui
