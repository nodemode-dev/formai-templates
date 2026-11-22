# FormCut: credits for its templates and demos

Copied unchanged from the formcut repository at its release 2.20.1. Each part below is one credits file of that repository, named by its path there.

## From `demo/CREDITS.md`

# Credits for the demo media

Every file below was opened on its source page and its licence read there before it was downloaded. None of it is formcut's own work, and none of it is covered by formcut's Apache-2.0 licence; each keeps the licence on its source page. The demo ships them as JavaScript data packs in `demo/assets/media/` (`clip-NN.js`, `music.js`) with `film.js` as the manifest; the packs hold the re-encoded files as base64 so the page can decode them from `file://`.

The Pexels License (https://www.pexels.com/license/) allows free use and modification, asks for no attribution, and forbids selling unaltered copies, redistributing the files on other stock platforms, implying endorsement, and portraying identifiable people badly. The film shows landscapes, sky, fire and water; no person, logo or brand is a subject of any clip.

## Video, from Pexels

All eight clips: video track kept, audio dropped, trimmed to the span used, cropped to 16:9 where needed, scaled to 1280x720 with Lanczos, re-encoded H.264 (x264, CRF 21, `-preset veryfast`, keyframe every 15 frames, faststart). The 60 fps sources were reduced to 30 fps.

| Demo name | File in the demo | Title | Photographer | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Milky Way (`film-01`) | `clip-01.js` | Stunning Milky Way Timelapse Over Mountains | Erhan Dayi (@moments) | https://www.pexels.com/video/stunning-milky-way-timelapse-over-mountains-39220755/ | License: Free (Pexels License) | 2560x1440 source file; first 7.0 s; 1280x720; 24 fps |
| Sunrise ridge (`film-02`) | `clip-02.js` | Stunning Mountain Sunrise Aerial View | GIANG VU | https://www.pexels.com/video/stunning-mountain-sunrise-aerial-view-33354461/ | License: Free (Pexels License) | 2560x1440 source; 7.9 s from 0:03; 1280x720; 30 fps |
| Snow peaks (`film-03`) | `clip-03.js` | Dramatic Sunrise Over Snowy Swiss Peaks | Marek Piwnicki | https://www.pexels.com/video/dramatic-sunrise-over-snowy-swiss-peaks-39264188/ | License: Free (Pexels License) | 2560x1440 source; 6.4 s from 0:02; 1280x720; 30 fps |
| Fog and forest (`film-04`) | `clip-04.js` | Aerial View of Misty Forest in Autumn | Julien Goettelmann | https://www.pexels.com/video/aerial-view-of-misty-forest-in-autumn-29792712/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps; 6.9 s from 0:01; 1280x720; 30 fps |
| Waterfall slope (`film-05`) | `clip-05.js` | Stunning Cascading Waterfall in Remote Valley | Gylfi Gylfason | https://www.pexels.com/video/stunning-cascading-waterfall-in-remote-valley-40393750/ | License: Free (Pexels License) | 2560x1440 source; 6.9 s from 0:04; 1280x720; 30 fps |
| Cloud sea (`film-06`) | `clip-06.js` | Breathtaking Sunrise Over Ocean of Clouds | 小小 兵 (pexels.com/@1516822895) | https://www.pexels.com/video/breathtaking-sunrise-over-ocean-of-clouds-34470558/ | License: Free (Pexels License) | 2560x1440 source; 8.4 s from 0:28; 1280x720; 30 fps |
| Campfire (`film-07`) | `clip-07.js` | Evening Campfire Glowing in Dark Outdoors | yaman ozuduru | https://www.pexels.com/video/evening-campfire-glowing-in-dark-outdoors-33667473/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps; 6.9 s from 0:05; 1280x720; 30 fps |
| Southern lights (`film-08`) | `clip-08.js` | Stunning Southern Lights Over Queenstown Lake | Eclipse Chasers | https://www.pexels.com/video/stunning-southern-lights-over-queenstown-lake-34794659/ | License: Free (Pexels License) | 2158x1440 source; cropped to 2158x1214 (16:9); 8.9 s from 0:02; 1280x720; 25 fps |

## Music

| Demo name | File in the demo | Title | Performer and project | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Goldberg Aria (`film-music`) | `music.js` | J.S. Bach, Aria from the Goldberg Variations, BWV 988 (track 01 of The Open Goldberg Variations) | Kimiko Ishizaka | https://archive.org/details/OpenGoldbergVariations | CC0 1.0 Universal, license URL http://creativecommons.org/publicdomain/zero/1.0/ | Ogg Vorbis file from the item; first 1.7 s of lead-in silence removed, 52 s kept, loudness normalised (EBU R128, -17 LUFS integrated, -1.5 dBTP), resampled to 44.1 kHz, MP3 128 kbps |

## Not used

freepd.com was considered and not used: its home page says the site is permanently closed and its category pages no longer answer. The Musopen recording of Grieg's Morning Mood on Wikimedia Commons (public domain on its description page) was read and chosen first, but upload.wikimedia.org refused every download with HTTP 429, so it was dropped rather than fetched by other means. `examples/demo` carries no licence grant and nothing from it is in this demo.

## From `demos/deliver/CREDITS.md`

# Credits for the deliver demo media

Every file below was opened on its source page and its licence read there before it was downloaded. None of it is formcut's own work, and none of it is covered by formcut's Apache-2.0 licence; each keeps the licence on its source page. The demo ships them as JavaScript data packs in `assets/media/` (`talk-01.js` to `talk-08.js`, `voice.js`, `music.js`) with `film.js` as the manifest; each pack holds the re-encoded file as base64 so the page can decode it from `file://`. Nothing from `examples/demo` is used.

The Pexels License (https://www.pexels.com/license/) allows free use and modification, asks for no attribution, and forbids selling unaltered copies, redistributing the files on other stock platforms, implying endorsement, and portraying identifiable people badly. The picture shows landscapes, sky, water and fire; no person, logo or brand is a subject of any clip.

## Video, from Pexels

Eight clips, video track kept and audio dropped, a span cut from each, scaled to 1280x720 with Lanczos, re-encoded H.264 (x264, CRF 27, `-preset veryfast`, keyframe every 15 frames, faststart) at 30 fps. Some of the Pexels clips are the same as in the other two demos, cut at other spans and colour-graded only by the page at play time.

| Demo name | File in the demo | Title | Photographer | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| First light (`talk-01`) | `talk-01.js` | Stunning Mountain Sunrise Aerial View | GIANG VU | https://www.pexels.com/video/stunning-mountain-sunrise-aerial-view-33354461/ | License: Free (Pexels License) | 2560x1440 source, 11.5 s from 0:18 |
| Mist and pine (`talk-02`) | `talk-02.js` | Aerial View of Misty Forest in Autumn | Julien Goettelmann | https://www.pexels.com/video/aerial-view-of-misty-forest-in-autumn-29792712/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps, 11.5 s from 0:02.5, 30 fps |
| The stream (`talk-03`) | `talk-03.js` | Stunning Cascading Waterfall in Remote Valley | Gylfi Gylfason | https://www.pexels.com/video/stunning-cascading-waterfall-in-remote-valley-40393750/ | License: Free (Pexels License) | 2560x1440 source, 11.5 s from 0:10 |
| Open water (`talk-04`) | `talk-04.js` | Silhouette Of Mountains At Sunset | Engin Akyurt | https://www.pexels.com/video/silhouette-of-mountains-at-sunset-1722697/ | License: Free (Pexels License) | 3840x2160 source at 25 fps, 11.5 s from 0:30, 30 fps |
| Peaks (`talk-05`) | `talk-05.js` | Dramatic Sunrise Over Snowy Swiss Peaks | Marek Piwnicki | https://www.pexels.com/video/dramatic-sunrise-over-snowy-swiss-peaks-39264188/ | License: Free (Pexels License) | 2560x1440 source, 11.5 s from 0:08 |
| Fire (`talk-06`) | `talk-06.js` | Evening Campfire Glowing in Dark Outdoors | yaman ozuduru | https://www.pexels.com/video/evening-campfire-glowing-in-dark-outdoors-33667473/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps, 11.5 s from 0:14, 30 fps |
| Above the clouds (`talk-07`) | `talk-07.js` | Breathtaking Sunrise Over Ocean of Clouds | 小小 兵 (pexels.com/@1516822895) | https://www.pexels.com/video/breathtaking-sunrise-over-ocean-of-clouds-34470558/ | License: Free (Pexels License) | 2560x1440 source, 11.5 s from 0:40 |
| Night sky (`talk-08`) | `talk-08.js` | Stunning Milky Way Timelapse Over Mountains | Erhan Dayi (@moments) | https://www.pexels.com/video/stunning-milky-way-timelapse-over-mountains-39220755/ | License: Free (Pexels License) | 2560x1440 source at 24 fps, first 12.5 s, 30 fps |

## Voice

| Demo name | File in the demo | Title | Reader and project | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Walden, Where I Lived (`talk-voice`) | `voice.js` | Henry David Thoreau, Walden (1854), chapter 2 "Where I Lived, and What I Lived For", part 2 (`walden_c02_p02_64kb.mp3`) | Gord Mackenzie for LibriVox | https://archive.org/details/walden_librivox | Usage: Public Domain, license URL http://creativecommons.org/licenses/publicdomain/ | 78 s cut from 0:28.6 (the opening "I went to the woods"), 70 Hz high-pass, loudness normalised (EBU R128, -18 LUFS integrated, -1.5 dBTP), mono, MP3 80 kbps |

The captions in `src/data.ts` are Thoreau's public-domain text, hand-typed and timed against a word-level alignment of the recording made with an offline speech model (Vosk small English, Apache-2.0) used only as a build tool; the model is not shipped.

## Music

| Demo name | File in the demo | Title | Performer and project | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Goldberg Variation 13 (`talk-music`) | `music.js` | J.S. Bach, Variatio 13 a 2 Clav., BWV 988 (The Open Goldberg Variations) | Kimiko Ishizaka | https://archive.org/details/OpenGoldbergVariations | CC0 1.0 Universal, license URL http://creativecommons.org/publicdomain/zero/1.0/ | Ogg Vorbis file from the item, first 90 s, loudness normalised (EBU R128, -21 LUFS integrated, -1.5 dBTP), 44.1 kHz stereo, MP3 112 kbps |

## Reframe paths

`src/paths.ts` holds crop paths produced by running the engine's own `reframe()` (`backend/app/subject.py`) on the shipped clips at 2 frames per second; they are numbers derived from the footage and carry no licence of their own.

## From `demos/grade/CREDITS.md`

# Credits for the grade demo media

Every file below was opened on its source page and its licence read there before it was downloaded. None of it is formcut's own work, and none of it is covered by formcut's Apache-2.0 licence; each keeps the licence on its source page. The demo ships them as JavaScript data packs in `assets/media/` (`grade-01.js` to `grade-06.js`, `music.js`) with `film.js` as the manifest; each pack holds the re-encoded file as base64 so the page can decode it from `file://`. Nothing from `examples/demo` is used.

The Pexels License (https://www.pexels.com/license/) allows free use and modification, asks for no attribution, and forbids selling unaltered copies, redistributing the files on other stock platforms, implying endorsement, and portraying identifiable people badly. The film shows landscapes, sky, water and fire; no person, logo or brand is a subject of any clip.

## Video, from Pexels

Six clips, video track kept and audio dropped, a span cut from each, scaled to 1280x720 with Lanczos, re-encoded H.264 (x264, CRF 25, `-preset veryfast`, keyframe every 15 frames, faststart) at 30 fps. Each is deliberately flattened on encode (`eq=contrast=0.80:saturation=0.74:brightness=0.025`) so the grade the page applies has room to work; this is a change to the file and is shown as such in the Media tab.

| Demo name | File in the demo | Title | Photographer | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Last light (`grade-01`) | `grade-01.js` | Silhouette Of Mountains At Sunset | Engin Akyurt | https://www.pexels.com/video/silhouette-of-mountains-at-sunset-1722697/ | License: Free (Pexels License) | 3840x2160 source at 25 fps, 13 s from 0:03, flattened, 30 fps |
| Open water (`grade-02`) | `grade-02.js` | Silhouette Of Mountains At Sunset | Engin Akyurt | https://www.pexels.com/video/silhouette-of-mountains-at-sunset-1722697/ | License: Free (Pexels License) | the same file, 10 s from 0:34, flattened, 30 fps |
| Warm peaks (`grade-03`) | `grade-03.js` | Dramatic Sunrise Over Snowy Swiss Peaks | Marek Piwnicki | https://www.pexels.com/video/dramatic-sunrise-over-snowy-swiss-peaks-39264188/ | License: Free (Pexels License) | 2560x1440 source, 10 s from 0:04, flattened |
| Mist and pine (`grade-04`) | `grade-04.js` | Aerial View of Misty Forest in Autumn | Julien Goettelmann | https://www.pexels.com/video/aerial-view-of-misty-forest-in-autumn-29792712/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps, 10 s from 0:02, flattened, 30 fps |
| Fire (`grade-05`) | `grade-05.js` | Evening Campfire Glowing in Dark Outdoors | yaman ozuduru | https://www.pexels.com/video/evening-campfire-glowing-in-dark-outdoors-33667473/ | License: Free (Pexels License) | 1920x1080 source at 59.94 fps, 8.5 s from 0:12, flattened, 30 fps |
| Southern lights (`grade-06`) | `grade-06.js` | Stunning Southern Lights Over Queenstown Lake | Eclipse Chasers | https://www.pexels.com/video/stunning-southern-lights-over-queenstown-lake-34794659/ | License: Free (Pexels License) | 2158x1440 source at 25 fps, cropped to 2158x1214 (16:9), 11 s from 0:08, flattened |

## Music

| Demo name | File in the demo | Title | Performer and project | Source page | Licence as stated on the page | What changed |
| --- | --- | --- | --- | --- | --- | --- |
| Goldberg Variation 13 (`grade-music`) | `music.js` | J.S. Bach, Variatio 13 a 2 Clav., BWV 988 (The Open Goldberg Variations) | Kimiko Ishizaka | https://archive.org/details/OpenGoldbergVariations | CC0 1.0 Universal, license URL http://creativecommons.org/publicdomain/zero/1.0/ | Ogg Vorbis file from the item, first 46 s, loudness normalised (EBU R128, -17 LUFS integrated, -1.5 dBTP), 4 s fade out, 44.1 kHz stereo, MP3 128 kbps |

## From `examples/demo/README.md`

# Demo media

The four files the demo project loads (**Load demo** in the app, or `POST /api/demo`).
They are sample media, **not covered by formcut's Apache-2.0 licence**: each keeps
the licence it came with, below.

| File | What it is | Source | Licence |
| --- | --- | --- | --- |
| `input-clip-example.mp4` | 10 s, 1920×1080, 30 fps: warm glowing particles, the opening clip | Pexels video [34637281](https://www.pexels.com/video/abstract-digital-light-particle-animation-34637281/), "Abstract Digital Light Particle Animation" by [Nicola Narracci](https://www.pexels.com/@nicola-narracci-157460431/) | [Pexels License](https://www.pexels.com/license/) |
| `model-drop-MV.mp4` | 10 s, 1920×1080, 30 fps: blue and violet waves, the second clip | Pexels video [38724728](https://www.pexels.com/video/abstract-waves-of-blue-and-purple-animation-38724728/), "Abstract Waves of Blue and Purple Animation" by [Nicola Narracci](https://www.pexels.com/@nicola-narracci-157460431/) | [Pexels License](https://www.pexels.com/license/) |
| `effect-example-image.jpg` | 3840×2160 abstract orange render: the overlay, and the image effect thumbnails are drawn on | Pexels photo [36025195](https://www.pexels.com/photo/abstract-orange-sculptural-form-on-gradient-background-36025195/), "Abstract Orange Sculptural Form on Gradient Background" by [Mahmoud Ramadan](https://www.pexels.com/@mahmoudramadan/) | [Pexels License](https://www.pexels.com/license/) |
| `a-sample.wav` | 2.2 s spoken line, 24 kHz mono | Generated for formcut with [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) (Kokoro-82M, Apache-2.0) | Generated for this project |

The Pexels License allows free use and modification without attribution; it does not
allow selling unaltered copies or redistributing the files on their own as stock
media. The credits above are given as a courtesy.

These files are for the demo project and development. They are not bundled into
formcut's release builds.
