# FormAT: credits for its templates and demos

Copied unchanged from the formAT repository at its release 0.32.0. Each part below is one credits file of that repository, named by its path there.

## From `backend/app/demos/solar-system/files/CREDITS.md`

# Orrery: image credits and sources

## Real maps

All 26 surface maps in `artifact.html` come from one source. They are not all photographic: Venus is a radar map with filled gaps, and the Saturn, Neptune and Titan textures are painted or concept art, as their NASA pages say. Each map has its own credit line and source page, given in the second table below.

- Repository: `https://github.com/nasa/NASA-3D-Resources`, folder `Images and Textures`, commit `11ebb4ee043715aefbba6aeec8a61746fad67fa7` (shallow sparse clone, JPEG files only). Each map is also published on NASA Science's 3D Resources catalogue (`https://science.nasa.gov/3d-resources/`), which is the page each credit below was read from on 15 November 2026.
- Status: NASA content, not subject to copyright in the United States (NASA media guidelines, `https://www.nasa.gov/nasa-brand-center/images-and-media/`: NASA content "generally are not subject to copyright in the United States", and "NASA should be acknowledged as the source of the material"). The repository README says of its models, textures and images, "These assets are free and without copyright", and the catalogue says "All of these assets are free to download and use". No map page states a licence of its own; each only links to NASA's usage guidelines. The repository's `meta.json` lists the licence of the repository as "NASA Open Source Agreement Version 1.3". Maps whose credit names the USGS are work of a US federal agency, which states that its own content is in the US public domain (`https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits`).
- Credit lines: each is given exactly as its page gives it. Where a page gives none (Venus, Saturn, Titan and the six Saturn moons below) none is invented: the page says "From the database of JPL/Caltech generated planetary maps", and JPL's own map tables (`https://maps.jpl.nasa.gov/tmaps/`) list the owner of those maps as JPL/Caltech (Caltech/JPL/USGS for the moons).
- NASA's name and these images are used for identification of the maps only. Nothing here suggests NASA endorses this page.

Each file was downscaled and re-encoded as JPEG and embedded as a data URI. Some were also edited, as listed. No original file is distributed.

| Body | Source file in `Images and Textures/` | Embedded as | Changes besides resizing |
| --- | --- | --- | --- |
| Earth | `Earth (A)/Earth (A).jpg` | 1024x512 colour | none. This is a shaded-relief colour map without clouds; the clouds on the page are generated |
| Mars | `Mars/Mars.jpg` | 1024x512 colour | none |
| Venus | `Venus/Venus.jpg` | 1024x512 colour | none (radar map of the surface) |
| Jupiter | `Jupiter/Jupiter.jpg` | 1024x512 colour | enlarged from 720x360 |
| Saturn | `Saturn/Saturn.jpg` | 1024x512 colour | enlarged from 720x360 |
| Neptune | `Neptune/Neptune.jpg` | 512x256 colour | none |
| Moon | `Moon/Moon.jpg` | 512x256 colour | the source is a photo of the near side as a disc, not a map. It is projected onto the near hemisphere; the far side, which the photo does not show, is a blurred mirror copy of the near side and is not real |
| Io | `Jupiter - Io (B)/Jupiter - Io (B).jpg` | 512x256 colour | none |
| Europa | `Jupiter - Europa/Jupiter - Europa.jpg` | 512x256 grey | tinted on the page; white no-data areas at the poles left as they are |
| Ganymede | `Jupiter - Ganymede/Jupiter - Ganymede.jpg` | 512x256 grey | white no-data areas filled with the average tone; tinted on the page |
| Callisto | `Jupiter - Callisto/Jupiter - Callisto.jpg` | 512x256 grey | white no-data areas filled with the average tone; tinted on the page |
| Phobos | `Mars - Phobos/Mars - Phobos.jpg` | 256x128 grey | tinted; drawn as a squashed sphere |
| Deimos | `Mars - Deimos/Mars - Deimos.jpg` | 256x128 grey | tinted; drawn as a squashed sphere |
| Mimas, Enceladus, Tethys, Dione, Rhea, Iapetus | `Saturn - <name>/Saturn - <name>.jpg` | 256x128 grey | none; white areas in the source are unmapped regions |
| Titan | `Saturn - Titan/Saturn - Titan.jpg` | 256x128 colour | none |
| Miranda, Ariel, Umbriel, Titania, Oberon | `Uranus - <name>/Uranus - <name>.jpg` | 256x128 grey | the source maps cover the southern half only (black elsewhere); the black is filled with the average tone, so the northern half is blank; tinted on the page |
| Triton | `Neptune - Triton/Neptune - Triton.jpg` | 256x128 colour | the source covers one region (black elsewhere); the black is filled with the average tone |

### Credit and source page for each map

Credit lines are copied from the NASA Science 3D Resources page of each map, read on 15 November 2026. "None on the page" means the page has no credit line.

| Body | Credit line on the page | Source page | What the page says it is | Status |
| --- | --- | --- | --- | --- |
| Earth | USGS & NASA/Jet Propulsion Laboratory | https://science.nasa.gov/3d-resources/earth-a/ | "Nice topography-like map colored by land and ocean from the USGS." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Mars | NASA/Jet Propulsion Laboratory & Caltech | https://science.nasa.gov/3d-resources/mars/ | "From Viking images processed at the USGS." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Venus | none on the page (JPL map table: owner JPL/Caltech) | https://science.nasa.gov/3d-resources/venus/ | "Stitched from Magellan RADAR imagery. Gaps filled in with global texture." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Jupiter | JPL & Caltech | https://science.nasa.gov/3d-resources/jupiter/ | "From Voyager images." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Saturn | none on the page (JPL map table: creator Don Davis, owner JPL/Caltech) | https://science.nasa.gov/3d-resources/saturn/ | "Fictional." An artist's texture, not a map of the planet | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Neptune | Don Davis & JPL/Caltech | https://science.nasa.gov/3d-resources/neptune/ | "Fictional. Texture created by Don Davis with cloud features." JPL's map table lists JPL/Caltech as owner | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Moon | Johnson Space Center | https://science.nasa.gov/3d-resources/apollo-11-view-of-the-moon/ | Apollo 11 photograph AS11-44-6665 (21 July 1969) of the entire nearside | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Io | USGS, JPL, & Caltech | https://science.nasa.gov/3d-resources/jupiter-io-b/ | "Mostly from the Caltech/JPL/USGS map with color taken from a recent Galileo global mosaic." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Europa | USGS, JPL, & Caltech | https://science.nasa.gov/3d-resources/jupiter-europa/ | "From the USGS, mosaicked with Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Ganymede | USGS, JPL, & Caltech | https://science.nasa.gov/3d-resources/jupiter-ganymede/ | "From the USGS, mosaicked with Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Callisto | USGS, JPL, & Caltech | https://science.nasa.gov/3d-resources/jupiter-callisto/ | "From the USGS, mosaicked with Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Phobos | NASA/JPL/Solar System Simulator | https://science.nasa.gov/3d-resources/mars-phobos/ | "From Viking images processed at the USGS." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Deimos | NASA/JPL/Solar System Simulator | https://science.nasa.gov/3d-resources/mars-deimos/ | "From Viking images, processed at the USGS." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Mimas | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-mimas/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Enceladus | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-enceladus/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Tethys | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-tethys/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Dione | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-dione/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Rhea | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-rhea/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Titan | none on the page (JPL map table: creator Seal, owner JPL/Caltech) | https://science.nasa.gov/3d-resources/saturn-titan/ | "Fictional. Titan concept with color from Voyager images." A concept texture, not a map of the surface | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Iapetus | none on the page (JPL map table: owner Caltech/JPL/USGS) | https://science.nasa.gov/3d-resources/saturn-iapetus/ | "Mosaic from the Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines) |
| Miranda | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/uranus-miranda/ | "From the USGS; a mosaic using Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Ariel | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/uranus-ariel/ | "From the USGS; a mosaic using Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Umbriel | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/uranus-umbriel/ | "Mosaicked with Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Titania | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/uranus-titania/ | "Mosaicked with Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Oberon | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/uranus-oberon/ | "From the USGS; a mosaic using Voyager imagery." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |
| Triton | USGS/Tammy Becker & JPL/Caltech | https://science.nasa.gov/3d-resources/neptune-triton/ | "Stitched together from limited Voyager imagery by the USGS." | NASA content, not subject to copyright in the United States (NASA media guidelines); USGS work is in the US public domain |

Two page quirks, noted so nobody is misled: the Miranda page lists its download under the name `Uranus - Ariel.jpg`, and the Oberon page shows Ariel's JPEG size; the files in the repository are `Uranus - Miranda.jpg` (313.74 KB) and `Uranus - Oberon.jpg` (50.01 KB), and the embedded maps were compared with them.

## Generated by the page's own code (not photographs)

- Sun: animated granulation from noise.
- Mercury: noise plus about 420 generated craters. The repository has no Mercury map.
- Uranus: a pale banded gradient. The repository has no map of the planet itself.
- Saturn's rings and the faint rings of Uranus: one-dimensional brightness profiles written by hand (C ring, B ring, Cassini division, A ring, Encke gap).
- Earth's clouds, the star field, the Milky Way band, the asteroid belt, atmosphere glows and the Sun's lens glow.

## Figures

The numbers in the information panel were checked against NASA's planetary fact sheets (`https://nssdc.gsfc.nasa.gov/planetary/factsheet/`) and NASA Science pages (`https://science.nasa.gov/`) on 15 November 2026. Moon counts change as discoveries are confirmed; the page shows 115 for Jupiter (NASA's Jupiter moons page, `https://science.nasa.gov/jupiter/jupiter-moons/`, last updated 21 September 2026), 274 for Saturn, 28 for Uranus and 16 for Neptune, as those pages gave them on that date. `FIGURES.md`, the next file in this chat, gives the page and the words behind every figure, and says which values are converted (a radius doubled, hours turned into days) or computed.

## In the page

The Orrery's own Credits button, at the top left of the page, lists the credit line of each of the 26 maps given above with a link to its source page, and says which parts the page generates itself and where its figures come from.
