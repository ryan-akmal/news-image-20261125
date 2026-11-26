[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ryan-akmal/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ryan-akmal/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World in One Day — Wednesday, 25 November 2026

**make.fun competition:** `news-image-20261125` — "Sum up 25 November's world news in one image"
**Entry title:** The World in One Day — Wednesday, 25 November 2026

A one-page newspaper front page that sums up Wednesday 25 November 2026 in
a single image. The date is named in the masthead; six stories cover the
Strait of Hormuz, Ukraine, Yemen and Saudi Arabia, Gaza, markets and tech,
with six more in the "Also in the news" strip.

## The six stories

1. **Tankers ablaze in Hormuz** — Iran's Revolutionary Guard says two oil
   tankers struck naval mines and caught fire in the Strait of Hormuz; the
   vessels were on an unauthorised route, Tehran says.
2. **Ukraine hits two refineries** — Ukrainian drones hit the Syzran and
   Kuibyshev Rosneft refineries in Russia's Samara region overnight; fires,
   one killed, 145 drones downed.
3. **Houthis hit Ras Tanura** — Yemen's Houthis say they attacked Saudi
   Arabia's Ras Tanura oil refinery; fires reported at the terminal.
4. **Israel kills Hamas colonel** — An Israeli strike kills Hamas interior
   security colonel Mohammad Abuelouf, his wife and two children in Gaza
   City.
5. **Asian stocks tumble** — South Korea's KOSPI falls 6.16%, Japan's
   Nikkei 2.78%; Nasdaq -1.5% on Tuesday, the S&P 500 -0.5% for an eighth
   loss in nine days, while the Dow closes above 50,000 for the first time.
6. **Huawei convicted** — A Brooklyn jury convicts Huawei on 10 of 12
   counts, including bank fraud, wire fraud, sanctions violations and
   trade-secret theft.

Also in the news: Poland pushes for a permanent US troop presence after two
Russian airspace incursions; Sudan: RSF drone strikes kill 19 civilians;
Colombia frees all hostages in the Cartagena supermarket siege; Australia
and Solomon Islands sign a treaty; the Bogor mine flood toll rises to six;
Shenzhou-24 docks with Tiangong.

## How the image was made

`generate_image.py` draws the front page with Pillow: flat vector-style
pictograms and DejaVu typesetting, no photographs, no copied artwork, no
network. `main.ts` copies the finished `entry.png` to the output directory
the grader reads.

Run it: `python3 generate_image.py` (writes `entry.png`), then
`mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts`.
