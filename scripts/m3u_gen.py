"""
m3u_gen.py
----------

Given a PSX roms directory (~/games/roms/psx) and an optionally
hidden directory of folders containing sets of bin/cue files,
generate a m3u playlist file for each disc-set.

for each (folder of bin/cue):
    make m3u with all cue (discs files) present
"""

import os
import sys

DISC_SUBDIR = ".discs"


def write_playlist_files_for_discs(current_dir):
    titles = os.listdir(os.path.join(current_dir, ".discs"))
    disc_cue_map = {}
    for title in titles:
        print(title)
        disc_cue_map[title] = [
            df
            for df in os.listdir(os.path.join(current_dir, ".discs", title))
            if df.endswith(".cue")
        ]

    for title, cues in disc_cue_map.items():
        m3u_content = "\n".join([f".discs/{title}/{cue}" for cue in cues])
        filename = f"{title}.m3u"
        with open(os.path.join(current_dir, filename), "w") as f:
            f.write(m3u_content)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        current_dir = "."
    else:
        current_dir = sys.argv[1]
    write_playlist_files_for_discs(current_dir)
