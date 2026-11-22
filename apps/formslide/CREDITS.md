# FormDeck: credits for its templates and demos

Copied unchanged from the formdeck repository at its release 0.46.3. Each part below is one credits file of that repository, named by its path there.

## From `demo/CREDITS.md`

# Demo credits

The pictures and data in the demo deck "Worlds Beyond". Every source page was opened and read before the file was downloaded. All pictures are NASA images; none shows a person, a logo or a brand.

Licence basis for NASA material: NASA's guidelines page (https://www.nasa.gov/nasa-brand-center/images-and-media/) states that NASA content "generally are not subject to copyright in the United States". The individual NASA pages below carry a credit line and no licence text of their own, so the licence column says so. No NASA insignia is used or shown.

Every picture was resized (never enlarged) and re-encoded to WebP at quality 80 to 88 with Pillow, then embedded as a data URL in `assets/media/deck.js` or `assets/media/tray.js`. No picture was cropped or retouched in the files; the deck crops them on the slide with the `cover` fit and a focus point.

The app ships the same twelve files (the nine below and img_edge, img_moj and img_chey from the Photos tray) as plain WebP in `frontend/public/demos/nasa/`, decoded unchanged by `scripts/demo-media.py`, so Home > Demos opens this deck and the Present demo's talk inside the app.

## Pictures in the deck (`assets/media/deck.js`)

| In the demo | Title | Credit | Source page | Licence as stated on the page | Changes |
| --- | --- | --- | --- | --- | --- |
| img_rise | Earthrise, Apollo 8 (AS08-14-2383) | NASA/William Anders | https://www.nasa.gov/image-detail/moon-landing-l-7-months-10-apollo-8-earthrise-photo-as08-14-2383 | No licence text; credit line "Image Credit: NASA/William Anders"; NASA content, see above | 3000x1971 JPEG resized to 1400x920 WebP |
| img_set | A Breathtaking Earthset from Orion (art002e021278), April 6, 2026 | NASA | http://images-assets.nasa.gov/image/art002e021278/metadata.json (NASA Image and Video Library record) | No licence text; photographer field "NASA"; NASA content, see above | 5568x3712 JPEG resized to 1400x933 WebP |
| img_cur | Looking Up at Mars Rover Curiosity in 'Buckskin' Selfie (PIA19808) | NASA/JPL-Caltech/MSSS | https://science.nasa.gov/photojournal/looking-up-at-mars-rover-curiosity-in-buckskin-selfie/ | No licence text; credit line as given; NASA content, see above | 4841x2949 JPEG resized to 1600x975 WebP |
| img_per | Perseverance's Selfie with Ingenuity (PIA24542) | NASA/JPL-Caltech/MSSS | https://science.nasa.gov/photojournal/perseverances-selfie-with-ingenuity/ | No licence text; credit line as given; NASA content, see above | 12341x9076 JPEG resized to 1600x1177 WebP |
| img_jup | Cassini Jupiter Portrait (PIA04866) | NASA/JPL/Space Science Institute | https://science.nasa.gov/photojournal/cassini-jupiter-portrait/ | No licence text; credit line as given; NASA content, see above | 1920x2400 JPEG resized to 800x1000 WebP |
| img_sat | The Greatest Saturn Portrait ...Yet (PIA06193) | NASA/JPL/Space Science Institute | https://science.nasa.gov/photojournal/the-greatest-saturn-portrait-yet/ | No licence text; credit line as given; NASA content, see above | 8888x4544 JPEG resized to 1600x818 WebP |
| img_dot | Solar System Portrait, Earth as Pale Blue Dot (PIA00452) | NASA/JPL (Voyager 1); the page's Image Credit field is blank and names JPL as producer | https://photojournal.jpl.nasa.gov/catalog/PIA00452 | No licence text; NASA content, see above | 453x614 JPEG resized to 334x453 WebP |
| img_smile | The Day the Earth Smiled (PIA17172) | NASA/JPL-Caltech/SSI | https://science.nasa.gov/photojournal/the-day-the-earth-smiled/ | No licence text; credit line as given; NASA content, see above | 9000x3500 JPEG resized to 1600x622 WebP |
| img_udf | Hubble Ultra Deep Field | NASA and the European Space Agency | https://commons.wikimedia.org/wiki/File:Hubble_ultra_deep_field.jpg | "This file is in the public domain because it was created by NASA and ESA." | 3100x3100 JPEG resized to 1400x1400 WebP |

## Pictures in the Photos tray (`assets/media/tray.js`)

| In the demo | Title | Credit | Source page | Licence as stated on the page | Changes |
| --- | --- | --- | --- | --- | --- |
| img_edge | The Edge of the Night (PIA17199) | NASA/JPL-Caltech/Space Science Institute | https://science.nasa.gov/photojournal/the-edge-of-the-night/ | No licence text; credit line as given; NASA content, see above | 4399x980 grayscale JPEG resized to 1600x356 WebP |
| img_moj | Curiosity Self-Portrait at 'Mojave' Site on Mount Sharp (PIA19142) | NASA/JPL-Caltech/MSSS | https://science.nasa.gov/photojournal/curiosity-self-portrait-at-mojave-site-on-mount-sharp/ | No licence text; credit line as given; NASA content, see above | 9015x4617 JPEG resized to 1600x819 WebP |
| img_chey | Perseverance's Selfie With 'Cheyava Falls' (PIA26344) | NASA/JPL-Caltech/MSSS | https://science.nasa.gov/photojournal/perseverances-selfie-with-cheyava-falls/ | No licence text; credit line as given; NASA content, see above | 10502x7458 JPEG resized to 1400x994 WebP |

## Data

| In the demo | Title | Source | Licence | Changes |
| --- | --- | --- | --- | --- |
| Slide 9 chart | Confirmed planets by discovery year, added up as a running total (6,464 through 2026) | NASA Exoplanet Archive (https://exoplanetarchive.ipac.caltech.edu/), planetary systems composite table, counted by discovery year with the archive's TAP service on 2026-11-07 | The archive's acknowledgement page (https://exoplanetarchive.ipac.caltech.edu/docs/acknowledge.html) states no licence. These are factual counts. The requested acknowledgement is given here: "This research has made use of the NASA Exoplanet Archive, which is operated by the California Institute of Technology, under contract with the National Aeronautics and Space Administration under the Exoplanet Exploration Program." | Counts per year summed to a running total, years 1995 to 2026 shown |
| Slides 7 and 11 captions | Facts such as "more than 4 billion miles", "126 images", "62 images", "3.9 meters", dates | The caption text of the NASA pages listed above | NASA content, see above | Shortened and reworded |

## From `demos/build/CREDITS.md`

# Demo credits: Build From Material

The deck "Mill Street Roastery" (a launch plan for a made-up neighbourhood coffee roaster) uses eight Pexels photographs. Every source page was opened and read before the file was downloaded: the photographer and title match the page, and the page marks the photo free under the Pexels License (https://www.pexels.com/license/). No photo shows a recognisable person, a logo or a brand. The roastery, its people and every figure in the sample scripts are invented and labelled as such inside the demo. The text of the scripts is original.

Each photo was resized (never enlarged) to the longest side listed and re-encoded to WebP at quality 80 with Pillow, then embedded as a data URL in `assets/media/photos.js`. Nothing was cropped or retouched in the files; slides crop with the cover fit.

The app ships the same eight files as plain WebP in `frontend/public/demos/build/`, decoded unchanged by `scripts/demo-media.py`, so Home > Demos builds this deck inside the app with the engine's own compiler.

## Photographs (`assets/media/photos.js`)

| In the demo | Title | Photographer | Source page | Licence as stated on the page | Changes |
| --- | --- | --- | --- | --- | --- |
| cherries | Close-up of a Branch of Coffee Plant with Beans | Julian Cabrera S | https://www.pexels.com/photo/close-up-of-a-branch-of-coffee-plant-with-beans-19455179/ | Free, under the Pexels License | resized to 1063x1700 WebP |
| cups | Overhead Shot of Cups with Coffee Beans | H. Hümâ Yardim | https://www.pexels.com/photo/overhead-shot-of-cups-with-coffee-beans-11552880/ | Free, Pexels License | resized to 1600x1066 WebP |
| drum | Coffee beans roasting in professional metal equipment | Maria Orlova | https://www.pexels.com/photo/coffee-beans-roasting-in-professional-metal-equipment-4940744/ | Free, Pexels License | resized to 1600x1066 WebP |
| roast | Macro Close-Up of Roasted Coffee Beans | Ahmet Yüksek | https://www.pexels.com/photo/macro-close-up-of-roasted-coffee-beans-39719509/ | Free, Pexels License | resized to 1600x1067 WebP |
| beans | Close-Up Texture of Roasted Coffee Beans | Haberdoedas Photography | https://www.pexels.com/photo/close-up-texture-of-roasted-coffee-beans-33788268/ | Free, Pexels License | resized to 1275x1700 WebP |
| cafe | Interior of stylish cafe with wooden counter and stools placed near window | Maria Orlova | https://www.pexels.com/photo/interior-of-stylish-cafe-with-wooden-counter-and-stools-placed-near-window-4913351/ | Free to use, Pexels License | resized to 1133x1700 WebP |
| cup | Minimalist Coffee Cup on Wooden Table Top View | Seljan Salimova | https://www.pexels.com/photo/minimalist-coffee-cup-on-wooden-table-top-view-28593519/ | Free to use, Pexels License | resized to 1133x1700 WebP |
| sacks | Beans on Tray | Quang Nguyen Vinh | https://www.pexels.com/photo/beans-on-tray-2131905/ | Free, Pexels License | resized to 1600x1067 WebP |

Each photo also carries its credit as media metadata, so the .fdec and deck.json exports keep it, and the sample script names the photographers in the speaker notes.

## Templates (`assets/media/templates.js`)

The 67 built-in template designs (masters and layouts) were exported by running FormDeck's own generator (`backend/app/services/templates/catalog.py`), Apache-2.0 and part of this repository. No third-party design is included.

## Fonts (`assets/media/fonts.js`)

Complete, unmodified copies of the variable font files already in `frontend/public/fonts/full/` (SIL OFL 1.1, their licences are in each family's folder and in `../../NOTICE.md`): Lora, Playfair Display, Raleway and Source Sans 3. Other families a template names use the Latin subsets of `@fontsource` packages (OFL-1.1, listed in `../../NOTICE.md`). Merriweather is not shipped in this demo, so the one template that names it shows the browser's serif.

## Code

`fflate` (MIT) is bundled through the first demo's readers and writers. No new dependency.
