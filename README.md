# tello-move-spinning

A simple Python script that controls a DJI Tello drone to perform a spinning flight routine.

## What it does

1. Connects to the drone and takes off
2. Moves up 50 cm
3. Performs 2 loops of: clockwise spin (360°), counter-clockwise spin (1080°), move down and back up
4. Lands the drone

## Requirements

- Python 3
- [djitellopy](https://github.com/damiafuentes/DJITelloPy)

## Usage

```bash
pip install djitellopy
python main.py
```
