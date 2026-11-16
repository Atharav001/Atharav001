"""Render the rotating radar banner as a GitHub-friendly GIF."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess

root = Path(__file__).resolve().parents[1]
source = (root / 'assets/hero.svg').read_text()
with TemporaryDirectory() as directory:
    frames = Path(directory)
    for index in range(48):
        angle = index * 360 / 48
        svg = source.replace('rotate(0 1000 170)', f'rotate({angle:.1f} 1000 170)')
        subprocess.run(
            ['rsvg-convert', '-w', '1200', '-h', '340', '-o', str(frames / f'frame_{index:03}.png')],
            input=svg.encode(), check=True,
        )
    subprocess.run([
        'ffmpeg', '-loglevel', 'error', '-y', '-framerate', '12',
        '-i', str(frames / 'frame_%03d.png'),
        '-filter_complex', '[0:v]split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer:bayer_scale=5',
        '-loop', '0', str(root / 'assets/hero.gif'),
    ], check=True)
