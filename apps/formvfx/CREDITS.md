# FormVFX: credits for its templates and demos

Copied unchanged from the formVFX repository at its release 0.60.0. Each part below is one credits file of that repository, named by its path there.

## From `demo/CREDITS.md`

# Demo media credits

The Coastline project that the demo opens on uses five files from Pexels. Each source page was opened and read before the file was downloaded; the licence column quotes what the page states for that file. Pexels files are free to use under the Pexels License (https://www.pexels.com/license/).

In the demo the media travels as data packs, `demo/assets/media/<name>.js`, each one a data: URI that the page decodes into a video element or an image, because a page opened from `file://` cannot fetch local files or read pixels from them.

| File in the demo | Title | Author | Source page | Licence on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `dusk-shore.webm` | Aerial Shot of an Ocean During Sunset | Lachlan Ross | https://www.pexels.com/video/aerial-shot-of-an-ocean-during-sunset-5967989/ | Free (Pexels License) | 1920x1080 H.264 with sound re-encoded to 1280x720 VP9, 24 fps, the whole 9 s, sound removed |
| `rocky-surf.webm` | Waves Crashing On the Coast | Taryn Elliott | https://www.pexels.com/video/waves-crashing-on-the-coast-9239758/ | Free to use (Pexels License) | 2560x1440 25 fps clip trimmed to the 12 s from 0:14, scaled to 1280x720, re-encoded to VP9 |
| `cliff-edge.webm` | Stunning Coastal Cliffs and Ocean Waves | Dahlia E. Akhaine | https://www.pexels.com/video/stunning-coastal-cliffs-and-ocean-waves-37922027/ | Free (Pexels License) | 1080x1920 30 fps portrait clip trimmed to 9 s from 0:15, scaled to 406x720, re-encoded to VP9 |
| `headland-lighthouse.jpg` | Light House Near Rock Formation Body of Water | Miro Alt | https://www.pexels.com/photo/light-house-near-rock-formation-body-of-water-176382/ | Free (Pexels License) | 4289x2859 resized to 1600x1066, JPEG re-encoded |
| `soaring-gull.jpg` | Soaring Seagull Against a Clear Blue Sky | James Collington | https://www.pexels.com/photo/soaring-seagull-against-a-clear-blue-sky-30481070/ | Free (Pexels License) | 4836x3224 resized to 1600x1066, JPEG re-encoded |

Inside the demo the footage is graded, keyed, masked and animated by the Coastline project; those are edits made in the demo, not in the files.

The demo's interface, icons and fonts are the application's own (see `NOTICE.md`).

## From `demos/keying/CREDITS.md`

# Keying demo credits

Each source page was opened and read before the file was downloaded; the licence column quotes what the page states for that file. Pexels files are free to use under the Pexels License (https://www.pexels.com/license/).

| File in the demo | Title | Author | Source page | Licence on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/phone-screen.js` (a data pack holding `phone-screen-green.webm`) | Hand Holding Cellphone with Green Screen | Towfiqu barbhuiya | https://www.pexels.com/video/hand-holding-cellphone-with-green-screen-13863534/ | Free (Pexels License) | 3840x2160 29.97 fps source (the 2560x1440 file) scaled to 1280x720, 30 fps, the whole 8 s, re-encoded to VP9 with a keyframe every 12 frames, no sound |
| `../../demo/assets/media/dusk-shore.js` (referenced by path, not copied) | Aerial Shot of an Ocean During Sunset | Lachlan Ross | https://www.pexels.com/video/aerial-shot-of-an-ocean-during-sunset-5967989/ | Free (Pexels License) | see `demo/CREDITS.md`: 1280x720 VP9, 24 fps, sound removed. Here it plays inside the phone screen |

Data files made from the footage above, with no third-party content:

| File | What it is |
| --- | --- |
| `assets/media/roto-paths.js` | The outline of the hand and phone, traced from `phone-screen-green.webm` with OpenCV (colour thresholds, largest region, outline resampled to 100 points by arc length) at 11 frames, 24 frames apart. It becomes the keyframed Mask Path of the Roto Isolate composition. |
| `assets/media/track-corner.js` | The 240 positions this demo's own tracker produced for the phone's top right corner. They are re-applied at start with the tracker's Apply, for the tag, the screen content and the stabilized layer. |

The demo's interface, icons and fonts are the application's own (see `NOTICE.md`).

## From `demos/motion/CREDITS.md`

# Motion demo credits

Each source page was opened and read before the file was downloaded; the licence column quotes what the page states for that file. Pexels files are free to use under the Pexels License (https://www.pexels.com/license/). The Pexels pages list no other licence for these files.

| File in the demo | Title | Author | Source page | Licence on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/sky-timelapse.js` (a data pack holding `sky-timelapse.webm`) | Blue Sky With White Clouds -Timelapse Mode | Alexander Lutkov | https://www.pexels.com/video/blue-sky-with-white-clouds-timelapse-mode-1860175/ | Free (Pexels License) | 2560x1440 30 fps source (`1860175-uhd_2560_1440_30fps.mp4`) scaled to 1280x720, the whole 9 s, re-encoded to VP9, no sound |
| `assets/media/card-concrete.js` (a data pack holding `card-concrete.jpg`) | Modern Concrete Architectural Space with Minimalist Design | Jean-Daniel Francoeur | https://www.pexels.com/photo/28993989/ | Free (Pexels License) | 4555x6832 original cropped to 3:4 and scaled to 1200x1600, JPEG |
| `assets/media/card-tower.js` (a data pack holding `card-tower.jpg`) | Gray Concrete Building | Diana (Pexels handle @didsss) | https://www.pexels.com/photo/11467937/ | Free (Pexels License) | 3944x5916 original cropped to 3:4 and scaled to 1200x1600, JPEG |
| `assets/media/card-rowhouses.js` (a data pack holding `card-rowhouses.jpg`) | White and Teal Concrete Buildings | Miguel A. Padrinan | https://www.pexels.com/photo/434139/ | Free (Pexels License) | 6016x3864 original cropped to 3:4 and scaled to 1200x1600, JPEG |

No person is the subject of any file above and none shows a recognisable brand or logo.

The demo's interface, icons and fonts are the application's own (see `NOTICE.md`). The title text, shapes, expressions and Template Controls are authored in the demo and contain no third-party content.
