# FormLit: credits for its templates and demos

Copied unchanged from the formlit repository at its release 0.56.0. Each part below is one credits file of that repository, named by its path there.

## From `demo/CREDITS.md`

# Credits for the demo media

The 25 photographs in `assets/media/` come from Pexels and are used under the Pexels License (https://www.pexels.com/license/). Every photo page was opened and read before download, and each one stated "Free" and linked to that licence. No page marked a photo as AI-generated, and none shows a recognisable person, brand or logo as its subject.

## What was changed in every file

The original was downloaded from images.pexels.com at its full size, its orientation applied, scaled down so the long edge is at most 1600 px (never enlarged), and re-encoded as a progressive JPEG at quality 82 in sRGB. The original files carry no camera metadata, so the camera model, focal length, aperture, ISO, shutter speed and capture date that the Pexels photo page published for the photo were written back into the file as EXIF (model, FNumber, ISOSpeedRatings, FocalLength, ExposureTime, DateTimeOriginal) together with the photographer's name as Artist (folded to plain ASCII, as EXIF requires) and as XPAuthor (UTF-16, with the correct spelling). Where a page did not publish a value, the tag is absent.

Pages publish a capture date but no time of day, so DateTimeOriginal carries 00:00:00. Two photos have no published shutter time (autumn-02-birch-light.jpg and city-05-waterfront.jpg). Lens names are not published for any photo, so the demo shows none.

The files are shipped as JavaScript data packs (`assets/media/lakes.js`, `coast.js`, `city.js`, `autumn.js`), which hold the same JPEG bytes as base64 data URIs so the page can decode them from `file://`.

Ratings, flags, colour labels, keywords, collection names and the develop settings already applied to some photos were written for this demo and are not from the photographers or from Pexels.

## Photos

| File in the demo | Title | Photographer | Source page | Licence as stated on the page |
| --- | --- | --- | --- | --- |
| lakes-01-walensee.jpg | Sailing on Walensee Lake with Alpine Background | Paolo Bici | https://www.pexels.com/photo/sailing-on-walensee-lake-with-alpine-background-40090812/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-02-kolsai.jpg | Scenic View of Kolsai Lake in Almaty, Kazakhstan | Necip Duman | https://www.pexels.com/photo/scenic-view-of-kolsai-lake-in-almaty-kazakhstan-39859805/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-03-green-water.jpg | Green Lake Surrounded by Green Trees and Snow Covered Mountains | Markus Spiske | https://www.pexels.com/photo/green-lake-surrounded-by-green-trees-and-snow-covered-mountains-138903/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-04-braies.jpg | Green Trees on Rocky Mountains Near Lake | Sara Rubini | https://www.pexels.com/photo/green-trees-on-rocky-mountains-near-lake-9389047/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-05-lunersee.jpg | Amazing Lunersee in Alps | David Waschbüsch | https://www.pexels.com/photo/amazing-lunersee-in-alps-13308077/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-06-misty-lake.jpg | Green Island Surrounded by Water | Bob Krustev | https://www.pexels.com/photo/green-island-surrounded-by-water-163912/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-07-cirque.jpg | Stream in a Mountain Valley | Hristofor Stoyanov | https://www.pexels.com/photo/stream-in-a-mountain-valley-17887057/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-01-foggy-beach.jpg | Mountains Near Body of Water | Tiana | https://www.pexels.com/photo/mountains-near-body-of-water-529411/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-02-long-surf.jpg | Aerial View of Pristine Coastline and Ocean Waves | Laszlo Magyar | https://www.pexels.com/photo/aerial-view-of-pristine-coastline-and-ocean-waves-37753980/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-03-blue-rocks.jpg | Scenic Rocky Coastline with Blue Ocean under Clear Sky | Glen Zi | https://www.pexels.com/photo/scenic-rocky-coastline-with-blue-ocean-under-clear-sky-40629359/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-04-cliff-bay.jpg | Cliff and Bay | Cyrill | https://www.pexels.com/photo/cliff-and-bay-15663631/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-05-misty-cliffs.jpg | Misty Coastal Cliffs at Daybreak | Sandra | https://www.pexels.com/photo/misty-coastal-cliffs-at-daybreak-39130477/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-06-sea-cliff.jpg | Cliff, Sea and Clear Sky Landscape | Denis Larose | https://www.pexels.com/photo/cliff-sea-and-clear-sky-landscape-4616317/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-01-roundabout.jpg | Vibrant Urban Roundabout at Night with Light Trails | Oleksiy | https://www.pexels.com/photo/vibrant-urban-roundabout-at-night-with-light-trails-31531448/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-02-hill-town.jpg | A View of a Town at Night | Melike B | https://www.pexels.com/photo/a-view-of-a-town-at-night-8261543/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-03-river-towers.jpg | Skyscrapers by River in Austin at Night | Elsie Soto | https://www.pexels.com/photo/skyscrapers-by-river-in-austin-at-night-20185085/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-04-traffic-streaks.jpg | Blurred Motion of Traffic in the City | Famitsay Tamayo | https://www.pexels.com/photo/blurred-motion-of-traffic-in-the-city-12317907/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-05-waterfront.jpg | City Buildings Near Body of Water | Mack Kamp | https://www.pexels.com/photo/city-buildings-near-body-of-water-1449455/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| city-06-skyline.jpg | Skyline of a Modern City with Illuminated Buildings at Night | Johannes Plenio | https://www.pexels.com/photo/skyline-of-a-modern-city-with-illuminated-buildings-at-night-20208915/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-01-mist-branch.jpg | Misty Autumn Forest with Colorful Foliage | Adrian Limani | https://www.pexels.com/photo/misty-autumn-forest-with-colorful-foliage-34693090/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-02-birch-light.jpg | Trees in Autumn Forest | David Bartus | https://www.pexels.com/photo/trees-in-autumn-forest-1545345/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-03-red-maple.jpg | A View of the Forest During Autumn | Jason Thompson | https://www.pexels.com/photo/a-view-of-the-forest-during-autumn-11420370/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-04-orange-beech.jpg | Vibrant Autumn Forest with Orange Foliage | Mikałaj Prakopčyk | https://www.pexels.com/photo/vibrant-autumn-forest-with-orange-foliage-34574533/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-05-hillside.jpg | Vibrant Autumn Forest Landscape in Daylight | Gabriel Grip | https://www.pexels.com/photo/vibrant-autumn-forest-landscape-in-daylight-34427164/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-06-tall-trees.jpg | Vibrant Autumn Forest with Tall Trees | Christina & Peter | https://www.pexels.com/photo/vibrant-autumn-forest-with-tall-trees-34582296/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |

## From `demos/develop/CREDITS.md`

# Credits for the develop demo media

The nine photographs in `assets/media/develop.js` come from Pexels and are used under the Pexels License (https://www.pexels.com/license/). They are the same files, with the same EXIF, as nine of the photographs in `demo/assets/media/` (see `demo/CREDITS.md`, where each source page was opened and read before download: each stated "Free" and linked to that licence). No page marked a photo as AI-generated, and none shows a recognisable person, brand or logo as its subject.

## What was changed

Nothing beyond what `demo/CREDITS.md` records (long edge at most 1600 px, orientation applied, progressive JPEG at quality 82 in sRGB, camera model, focal length, aperture, ISO, shutter speed and capture date written back as EXIF from the values the Pexels photo page published, the photographer as Artist and XPAuthor). The nine files were repacked unchanged into one JavaScript data pack (`develop.js`) so the page can decode them from `file://`.

Ratings, flags, colour labels, keywords, the three shoot names, and every develop setting, mask and preset already applied were written for this demo and are not from the photographers or from Pexels.

## Photos

| File in the demo | Title | Photographer | Source page | Licence as stated on the page |
| --- | --- | --- | --- | --- |
| lakes-01-walensee.jpg | Sailing on Walensee Lake with Alpine Background | Paolo Bici | https://www.pexels.com/photo/sailing-on-walensee-lake-with-alpine-background-40090812/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-05-lunersee.jpg | Amazing Lunersee in Alps | David Waschbüsch | https://www.pexels.com/photo/amazing-lunersee-in-alps-13308077/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| lakes-02-kolsai.jpg | Scenic View of Kolsai Lake in Almaty, Kazakhstan | Necip Duman | https://www.pexels.com/photo/scenic-view-of-kolsai-lake-in-almaty-kazakhstan-39859805/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-01-foggy-beach.jpg | Mountains Near Body of Water | Tiana | https://www.pexels.com/photo/mountains-near-body-of-water-529411/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-03-blue-rocks.jpg | Scenic Rocky Coastline with Blue Ocean under Clear Sky | Glen Zi | https://www.pexels.com/photo/scenic-rocky-coastline-with-blue-ocean-under-clear-sky-40629359/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| coast-06-sea-cliff.jpg | Cliff, Sea and Clear Sky Landscape | Denis Larose | https://www.pexels.com/photo/cliff-sea-and-clear-sky-landscape-4616317/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-03-red-maple.jpg | A View of the Forest During Autumn | Jason Thompson | https://www.pexels.com/photo/a-view-of-the-forest-during-autumn-11420370/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-02-birch-light.jpg | Trees in Autumn Forest | David Bartus | https://www.pexels.com/photo/trees-in-autumn-forest-1545345/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |
| autumn-01-mist-branch.jpg | Misty Autumn Forest with Colorful Foliage | Adrian Limani | https://www.pexels.com/photo/misty-autumn-forest-with-colorful-foliage-34693090/ | Pexels License (page: "Free", linking to https://www.pexels.com/license/) |

## Selection bitmaps

`assets/media/masks.js` holds six 800 px grey-scale PNG bitmaps (five sky selections and one subject selection) that Select Sky and Select Subject use on the photos above. They were made for this demo from those photographs with OpenCV (GrabCut seeded from colour and position, then a guided filter), and carry the licence of the photographs they derive from (Pexels License). They contain no other third-party material.

| Bitmap key | Derived from | Selects |
| --- | --- | --- |
| lakes-01-walensee_sky | lakes-01-walensee.jpg | sky |
| lakes-05-lunersee_sky | lakes-05-lunersee.jpg | sky |
| coast-01-foggy-beach_sky | coast-01-foggy-beach.jpg | sky |
| coast-03-blue-rocks_sky | coast-03-blue-rocks.jpg | sky |
| coast-06-sea-cliff_sky | coast-06-sea-cliff.jpg | sky |
| autumn-03-red-maple_subject | autumn-03-red-maple.jpg | the red maple |

## Other assets

The interface, icons, fonts (Inter and JetBrains Mono, listed in `NOTICE.md`) and the favicon are the app's own and are bundled by the build. The demo uses no other third-party files.

## From `demos/share/CREDITS.md`

# Credits for the share demo media

## Photographs

The nineteen photographs in `assets/media/alps.js`, `world.js` and `more.js` come from Pexels and are used under the Pexels License (https://www.pexels.com/license/). Each source page was opened and read before use: each stated "Free" and linked to that licence. No page marked a photo as AI-generated, and none shows a recognisable person, brand or logo as its subject. Thirteen are the same files as in `demo/assets/media/` (see `demo/CREDITS.md`); six were added for this demo.

### What was changed

Long edge at most 1600 px, orientation applied, progressive JPEG at quality 80 in sRGB. Camera model, focal length, aperture, ISO, shutter speed and capture date are written back as EXIF from the values the Pexels photo page published (a photo whose page published none carries none). The photographer is written as Artist and as XPAuthor, and a copyright line reads "(c) Name, Pexels License". Thirteen photos carry a GPS position that was chosen for this demo from the place the photo title or page names (a lake, a village, a city); it is not the photographer's own location data, and the other six carry none so you can place them on the map. Ratings, flags, titles used as captions, the book, slideshow, print and web arrangements and the saved locations were written for this demo and are not from the photographers or from Pexels.

### Photos

| File in the demo | Title | Photographer | Source page |
| --- | --- | --- | --- |
| alps-01-walensee.jpg | Sailing on Walensee Lake with Alpine Background | Paolo Bici | https://www.pexels.com/photo/40090812/ |
| alps-02-lunersee.jpg | Amazing Lunersee in Alps | David Waschbüsch | https://www.pexels.com/photo/13308077/ |
| alps-03-braies.jpg | Green Trees on Rocky Mountains Near Lake | Sara Rubini | https://www.pexels.com/photo/9389047/ |
| alps-04-hallstatt.jpg | Idyllic Lakeside Village of Hallstatt, Austria | Ahmet Yüksek | https://www.pexels.com/photo/33467274/ |
| alps-05-bled.jpg | Aerial View of Lake Bled with Island Church | Jon Eliya | https://www.pexels.com/photo/32562800/ |
| world-01-reine.jpg | Reine, Lofoten | op23 | https://www.pexels.com/photo/12166189/ |
| world-02-kirkjufell.jpg | Majestic Kirkjufell and Waterfall in Iceland | Lorenzo Castellino | https://www.pexels.com/photo/39103198/ |
| world-03-santorini.jpg | Blue Sky over White Houses in Santorini, Greece | Ayoub SOUSSI | https://www.pexels.com/photo/23928841/ |
| world-04-rila.jpg | Green Island Surrounded by Water | Bob Krustev | https://www.pexels.com/photo/163912/ |
| world-05-kolsai.jpg | Scenic View of Kolsai Lake in Almaty, Kazakhstan | Necip Duman | https://www.pexels.com/photo/39859805/ |
| world-06-milford.jpg | Stunning Waterfalls in Milford Sound, New Zealand | Ling Xu | https://www.pexels.com/photo/33045304/ |
| world-07-austin.jpg | Skyscrapers by River in Austin at Night | Elsie Soto | https://www.pexels.com/photo/20185085/ |
| world-08-mexico-city.jpg | Blurred Motion of Traffic in the City | Famitsay Tamayo | https://www.pexels.com/photo/12317907/ |
| more-01-boats.jpg | Green Lake Surrounded by Green Trees and Snow Covered Mountains | Markus Spiske | https://www.pexels.com/photo/138903/ |
| more-02-tarn.jpg | Stream in a Mountain Valley | Hristofor Stoyanov | https://www.pexels.com/photo/17887057/ |
| more-03-surf.jpg | Aerial View of Pristine Coastline and Ocean Waves | Laszlo Magyar | https://www.pexels.com/photo/37753980/ |
| more-04-misty-cliffs.jpg | Misty Coastal Cliffs at Daybreak | Sandra | https://www.pexels.com/photo/39130477/ |
| more-05-autumn-mist.jpg | Misty Autumn Forest with Colorful Foliage | Adrian Limani | https://www.pexels.com/photo/34693090/ |
| more-06-roundabout.jpg | Vibrant Urban Roundabout at Night with Light Trails | Oleksiy | https://www.pexels.com/photo/31531448/ |

## Music

`assets/media/music.js` holds "Piano Fantasia No. 1" by Peter Bille Larsen, released under CC0 1.0 Universal (public domain dedication) on the Internet Archive: https://archive.org/details/3PeterbillelarsenCreativepatriot (the page states "CC0 1.0 Universal"). The slideshow uses a 64 second excerpt of the recording with a short fade in and a fade out, re-encoded as Ogg Opus at 64 kbit/s. The excerpt is the only change. CC0 needs no credit; it is given here anyway.

## Map

The map tiles are cut in the page from "Blue Marble: Next Generation w/ Topography and Bathymetry" (July), a NASA Earth Observatory image: https://science.nasa.gov/earth/earth-observatory/blue-marble-next-generation/base-topography-bathymetry (file `world.topo.bathy.200407.3x5400x2700.jpg` from assets.science.nasa.gov). NASA's media usage guidelines state that NASA imagery is generally not subject to copyright in the United States and may be used for non-commercial, factual purposes with NASA credited as the source (https://www.nasa.gov/nasa-brand-center/images-and-media/); the demo does not use the NASA insignia or logotype and does not imply endorsement. The only change is the reduction from 5400 by 2700 to 3600 by 1800 pixels (`assets/media/map.js`); the page then re-samples it per tile, tints it for the road, topo, light and dark styles, and draws the graticule and labels. The place names in `src/gazetteer.ts` are common geographic names typed for this demo; no map data from OpenStreetMap or another provider is used.

## Other assets

The interface, icons, fonts (Inter and JetBrains Mono, listed in `NOTICE.md`) and the favicon are the app's own and are bundled by the build. The demo uses no other third-party files.
