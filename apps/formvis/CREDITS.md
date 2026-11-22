# FormVis: credits for its templates and demos

Copied unchanged from the formvis repository at its release 2.8.1. Each part below is one credits file of that repository, named by its path there.

## From `demo/CREDITS.md`

# Demo media credits

Every picture in the demo comes from Pexels. Each source page was opened and read before the file was downloaded; each page labels the photo "Free" (or "Free to use") and links the Pexels License (https://www.pexels.com/license/), which states that the photos can be downloaded and used for free, that attribution is not required, and that they can be modified. Credit is given anyway.

Nothing else in the demo is third-party media. The fonts (Inter, JetBrains Mono) are listed in `NOTICE.md`. The masks listed below, the gradient mask and all text on the poster were made for this demo.

The photos ship as JavaScript data packs in `demo/assets/media/` (so the page opens from `file://` and the pixels can be read). Originals were downloaded with curl from images.pexels.com and re-encoded with Pillow; nothing was upscaled.

The app opens this demo from Home > Demos and Help > Demos. Its copy of the same eleven photographs and three masks is in `frontend/public/demos/paint/`: the packs' bytes written out unchanged as `.jpg` and `.png` files by `scripts/demo-media.py`, so the credits below cover them too.

## The poster "Above the Clouds"

| File in the demo | Title | Photographer | Source page | Licence as stated on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/sky.js` | Orange and Blue Cloudy Sky during Sunset | Edgar Rodrigo | https://www.pexels.com/photo/orange-and-blue-cloudy-sky-during-sunset-13515706/ | Free, Pexels License | Scaled to 1080 px wide, top 1350 px kept, JPEG quality 86 |
| `assets/media/mountains.js` | Silhouette of Mountains Under the Blue Sky | Matteo Milan | https://www.pexels.com/photo/silhouette-of-mountains-under-the-blue-sky-10770234/ | Free, Pexels License | Scaled to 1080 px wide, top 1350 px kept, JPEG quality 88; an alpha mask that removes the original sky was computed with OpenCV and stored as a grey PNG in the same pack |
| `assets/media/balloon.js` | Colorful Hot Air Balloon Against Clear Blue Sky | Gamze | https://www.pexels.com/photo/colorful-hot-air-balloon-against-clear-blue-sky-32616907/ | Free, Pexels License | Cropped to the balloon, scaled to 30 percent (423 by 471 px), JPEG quality 90; the cut-out mask was computed with OpenCV GrabCut, holes filled and edge feathered, stored as a grey PNG in the same pack |
| `assets/media/birds.js` | Flock of birds flying in white sky | Skyler Ewing | https://www.pexels.com/photo/flock-of-birds-flying-in-white-sky-4598338/ | Free to use, Pexels License | A 3600 by 2100 px region scaled to 1080 by 630 px, JPEG quality 84 (used with the Multiply blend mode) |
| `assets/media/mist.js` | Fog in the Forest in Black and White | Yetkin Agac | https://www.pexels.com/photo/fog-in-the-forest-in-black-and-white-17941592/ | Free, Pexels License | Rows 1300 to 3000 kept and scaled to 1080 px wide, JPEG quality 84; a soft vertical gradient mask was generated for it (used with the Screen blend mode) |

## The session photograph and the photo tabs

`tray-night` is the photograph the opening painting session is built on ("dawn-over-the-range"); the same pack's mist from the poster (`mist.js`) is its masked "Valley mist" layer. The other five open as their own document tabs.

| File in the demo | Title | Photographer | Source page | Licence as stated on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/tray-lake.js` | Starting Point - Oeschinensee Lake Hike | Nanda Gopal Lakshman | https://www.pexels.com/photo/starting-point-oeschinensee-lake-hike-27667695/ | Free, Pexels License | Scaled to 1600 px on the long side, JPEG quality 82 |
| `assets/media/tray-night.js` | Mountain Range against the Starry Sky at Dawn | Uzair Ansari | https://www.pexels.com/photo/mountain-range-against-the-starry-sky-at-dawn-14696300/ | Free, Pexels License | Same as above |
| `assets/media/tray-larch.js` | Autumn Larches in North Cascades National Park | Alex Moliski | https://www.pexels.com/photo/autumn-larches-in-north-cascades-national-park-28997992/ | Free, Pexels License | Same as above |
| `assets/media/tray-surf.js` | Ocean Waves Crashing on Rocks | Eduardo Ocampo | https://www.pexels.com/photo/ocean-waves-crashing-on-rocks-12972177/ | Free, Pexels License | Same as above |
| `assets/media/tray-dunes.js` | Serene Desert Dunes at Sunrise | Stephen Leonardi | https://www.pexels.com/photo/serene-desert-dunes-at-sunrise-28638836/ | Free, Pexels License | Same as above |
| `assets/media/tray-glacier.js` | Snowy Mountain | Sergei A | https://www.pexels.com/photo/snowy-mountain-2539429/ | Free, Pexels License | Same as above |

## Pack format

Each pack is one line: `(window.FV_MEDIA = window.FV_MEDIA || {})["name"] = { img: "data:image/jpeg;base64,...", mask: "data:image/png;base64,..." };`. The demo injects the script tag on demand (`src/media.ts`), decodes the data URIs into canvases and turns each grey mask into an alpha channel.

## From `demos/design/CREDITS.md`

# Demo credits: type and design

Every picture comes from Pexels. Each source page was opened and read before the file was downloaded; each page labels the photograph "Free" or "Free to use" and links the Pexels License (https://www.pexels.com/license/), which allows free use and modification without attribution. Credit is given anyway.

The photographs ship as JavaScript data packs in `assets/media/` (so the page opens from `file://` and the engine can read the pixels). Originals were downloaded with curl from images.pexels.com and re-encoded with Pillow; nothing was upscaled.

The app opens this demo from Home > Demos and Help > Demos. Its copy of the same three photographs is in `frontend/public/demos/design/`, the packs' bytes written out unchanged by `scripts/demo-media.py`, so the credits below cover them too; the type families are the app's own copies in `frontend/public/fonts/`.

| File in the demo | Title | Photographer | Source page | Licence as stated on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/lanterns.js` | Lighted Paper Lanterns in Various Colors Hanging in the Dark | Vladimir Sladek | https://www.pexels.com/photo/lighted-paper-lanterns-in-various-colors-hanging-in-the-dark-10059347/ | Free, Pexels License | Scaled from 6016 by 4016 px to 1500 by 1001 px, JPEG quality 86; placed in the document at 1160 px wide as a smart object |
| `assets/media/tree.js` | Illuminated Paper Lanterns Hanging on Tree Branches at Night | ym z | https://www.pexels.com/photo/illuminated-paper-lanterns-hanging-on-tree-branches-at-night-31367353/ | Free to use, Pexels License | Centre 4644 by 8256 px cropped to 9:16 and scaled to 1080 by 1920 px, JPEG quality 84 |
| `assets/media/bokeh.js` | Yellow String Lights in Bokeh Photography | Anatolii Kiriak | https://www.pexels.com/photo/yellow-string-lights-in-bokeh-photography-722432/ | Free to use, Pexels License | A 2832 by 1593 px band cropped and scaled to 1920 by 1080 px, JPEG quality 84 |

## Fonts

The three families the type layers use are the application's own bundled, SIL OFL 1.1 licensed files from `frontend/public/fonts/` (already listed in `NOTICE.md`), copied unchanged with their licence texts into `fonts/`: Bebas Neue, Playfair Display and Montserrat. Inter and JetBrains Mono, used by the window, come in through the application's stylesheets (OFL 1.1, via @fontsource).

## Not third-party

The event ("Lantern Night", Harbour Square, the dates and times) is invented for this demo. All type, shapes, gradients, layer styles and smart filters were made in the page with the application's engine.

## From `demos/retouch/CREDITS.md`

# Demo credits: selections and retouching

Both pictures come from Pexels. Each source page was opened and read before the file was used; each page labels the photograph "Free" and links the Pexels License (https://www.pexels.com/license/), which allows free use and modification without attribution. Credit is given anyway. Neither picture shows a person, a brand or a logo.

The photographs ship as JavaScript data packs in `assets/media/` (so the page opens from `file://` and the engine can read the pixels). Originals were downloaded with curl from images.pexels.com and re-encoded with Pillow; nothing was upscaled.

The app opens this demo from Home > Demos and Help > Demos. Its copy of the same two photographs is in `frontend/public/demos/retouch/`, the packs' bytes written out unchanged by `scripts/demo-media.py`, so the credits below cover them too.

| File in the demo | Title | Photographer | Source page | Licence as stated on the page | What was changed |
| --- | --- | --- | --- | --- | --- |
| `assets/media/golden-portrait.js` | Golden Retriever Portrait in Natural Light | Masood Aslami | https://www.pexels.com/photo/golden-retriever-portrait-in-natural-light-30810888/ | Free, Pexels License | Scaled from 6401 by 4267 px to 1600 by 1067 px, re-encoded as JPEG |
| `assets/media/golden-chain.js` | Golden Retriever Dog Outdoors Portrait | Rajesh S Balouria | https://www.pexels.com/photo/golden-retriever-dog-outdoors-portrait-40009093/ | Free, Pexels License | Scaled from 5492 by 4000 px to 1600 by 1165 px, re-encoded as JPEG |

## Fonts

The window uses Inter and JetBrains Mono (SIL OFL 1.1, via @fontsource, already listed in `NOTICE.md`), bundled into `assets/`.

## Not third-party

Every retouching layer, selection, mask and adjustment in the opening session was made in the page by the application's own engine (Spot Healing, Clone Stamp, Selection-Aware Fill, Color Range, Select and Mask, a Gaussian Blur and a Vibrance layer behind layer masks made from a saved selection). The two outlines in `src/outlines.ts` are hand-placed polygons for this demo.
