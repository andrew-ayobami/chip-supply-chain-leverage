# Conditions, not cutoffs: chip-supply-chain leverage for AI safety

Oct 8, 2026 · @Andrew

## Research question

Which AI-safety-relevant asks can chip-supply-chain countries outside the US and China credibly attach to their leverage: what should they coordinate on, and what should they avoid?

Track C (Diplomacy). Working hypothesis to test: the credible asks are conditions attached to supply, not threats to cut it.

## How the steps connect

Every ask needs two judgments: is it worth having (safety value), and can the coalition get it (credibility)? Credibility is the hard part. For asks that need a threat behind them, we compare the coalition's leverage today (Steps 1 and 4) with past supplier coalitions whose endings we know (Steps 2 and 3).

Step 5 lists and screens the asks, Step 6 sorts them, and Step 7 writes it up. Times assume about 11 working hours; if the day is shorter, trim the write-up, not the scoring.

## Step 1 · Pick the countries (about 1 hour)

We select chokepoints first and let the countries follow, so the set comes from a stated rule rather than our own picks.

- [x] Download the data from the [ETO Supply Chain Explorer](https://eto.tech/tool-docs/chipexplorer) and note the year of each figure
- [x] List the supply chain steps in scope: manufacturing equipment, materials, leading-edge fabrication, HBM memory, advanced packaging. Out of scope: chip design and design software (US-held) and raw minerals (mostly China)
- [x] For each step, list the countries whose firms hold at least 40% of world supply
- [x] Remove the US and China, the parties the coalition would bargain with
- [x] Rerun the screen at 25% and 60%, and note who moves in or out
- [x] Write down the final country set (expected: Netherlands, Japan, South Korea, Taiwan, Germany)

Taiwan stays in if it passes the screen and is scored like any other country. We don't analyse whether it could join a coalition openly; that goes in the limits.

## Step 2 · Fix the variables (about 30 minutes)

To compare past cases with today fairly, we describe both with the same six features. The "target" is the side the leverage is aimed at; for today, that's the US.

| Variable | Question (works for past cases and today) |
| --- | --- |
| Concentration | What share of the supply the target needs from outside does the supplier (or group) hold? |
| Substitutability | Can the target switch to another supplier or redesign around it? |
| Time to replace | How long would the target need to build its own supply? |
| Cohesion | How many separate actors must hold the line to keep the supplier's share? (counted, not judged; changed 21 Oct, see notes/decisions.md) |
| Dependence on the target | How much does the supplier rely on the target, for security or markets? |
| State control | Can the government direct the firms that hold the supply? |

- [x] Agree the six variables and the questions above
- [x] Write one line on what low, medium and high mean for each variable
- [x] Agree how you'll settle disagreements in scoring

## Step 3 · Score the past cases (about 3 hours)

Credibility is a prediction, and the only evidence we have is past attempts with known endings.

| Case | Who used the leverage | Why it's here |
| --- | --- | --- |
| Arab oil embargo, 1973–74 | Arab oil producers (OAPEC) | Supply cut tied to a political demand; buyers then organised |
| CIPEC, from 1967 | Copper exporters | A supplier group that never managed to move prices |
| International Tin Council, 1985 | Tin producers, with consumer members | Price support collapsed when its money ran out |
| China's rare-earth squeeze on Japan, 2010 | China | Coercive use of a chokepoint that pushed the buyer to diversify |
| Japan's materials restrictions on Korea, 2019–2023 | Japan | A squeeze inside our own candidate set |

- [x] Gather two or three good sources per case
- [x] Write a three-line summary per case: what the supplier wanted, how the target responded, how long the leverage lasted
- [x] Score each case on the six variables (changed 31 Oct for time: Claude drafted, Andrew reviewed and decided; one scorer per case)
- [x] Compare scores, settle differences, and record how often you agreed (not done: one scorer, so no agreement figure; stated as a limit)
- [x] Record each case's outcome: worked, partly worked, or backfired
- [x] Write three or four rules of thumb from the pattern, e.g. "threats backfire when the target can replace supply within a few years"
- [x] Note any variable that doesn't separate successes from failures, and any factor you're missing

## Step 4 · Score today's chokepoints (about 1.5 hours)

This gives the coalition's leverage profile: where its hold is strong, where it is weak, and which past case it most resembles.

- [x] Make one row per chokepoint (country and step), e.g. Netherlands–EUV lithography, Korea–HBM memory
- [x] Add the share, year and source for each row
- [x] Score each row on the six variables with the US as the target (changed 31 Oct for time: Claude drafted, Andrew reviewed and decided; one scorer per row)
- [ ] Compare scores, settle differences, and record how often you agreed (not done: one scorer, so no agreement figure; stated as a limit)
- [x] Write a short profile: where the leverage is strongest and weakest, and which past case it most resembles

## Step 5 · List and screen the asks (about 1 hour)

These are the candidates the answer will sort.

- [ ] Review the starting list below, adding or cutting to reach six to eight asks
- [ ] For each ask, write down what it requires of the US government or US firms
- [ ] Mark whether it needs a threat to cut or condition supply behind it
- [ ] Score its safety value (low, medium, high): which risk it reduces, and how directly
- [ ] Note who has to agree: members, firms, or the US government

**Starting list of asks**

- Shared anti-diversion and end-use checks, so advanced chips don't reach uncontrolled actors
- A joint consultation seat in US export-control rule-making
- Frontier model access for members' governments and evaluators
- Safety conditions on buyers above a set compute scale, such as evaluations and incident reporting
- Support for hardware-based verification features, such as location checks
- To test as things to avoid: withholding supply, coordinating prices, threatening to sell to China

## Step 6 · Judge credibility and sort the asks (about 1.5 hours)

This is where the answer comes from.

- [ ] For asks with no threat behind them, check whether the US would plausibly accept them because they cost it little or help it too
- [ ] For asks that need a threat, compare the coalition's profile (Step 4) with the rules of thumb (Step 3): does it look like a case that worked, or one that backfired?
- [ ] Place each ask on credibility against safety value
- [ ] Sort the asks into "coordinate on" (credible and worth having) and "avoid" (not credible, or likely to backfire)
- [ ] Check which verdicts would flip if your most disputed score went the other way

## Step 7 · Write up and submit (about 2.5 hours)

- [ ] Prepare two exhibits: the chokepoint table, and a chart of the asks on credibility against safety value
- [ ] Write the report (4–6 pages): question, method, findings, recommendations, limits
- [ ] Put the data and scoring sheet on GitHub
- [ ] Check every figure against its source
- [ ] Read it through together and submit

## Limits we will state

- Market shares come from one source at one date, and some inputs use older data.
- Time to replace and cohesion are judgment calls; we report how often our two independent scores agreed.
- Most historical cases are commodity markets. Chips are harder to substitute, so the lessons transfer imperfectly.
- Leverage sits with firms whose interests may differ from their governments'; we don't model firm behaviour.
- We can't see private negotiations or classified export-control deliberations.
- Taiwan is scored like any other country; we don't analyse whether it could join a coalition openly.
- No interviews with officials or firms, so the recommendations are a first cut for others to test.

## Summary and theory of change

**Summary.** A handful of countries outside the US and China hold steps of the AI chip supply chain that nobody can yet do without. This project maps those chokepoints using a stated rule, draws on five past supplier coalitions to see what makes such leverage hold or collapse, and scores which AI-safety asks these countries could make without threatening supply. The output is a sorted set of asks: what to coordinate on and what to avoid.

**Theory of change.**

1. **The problem:** these chokepoints are a wasting asset, because the US and China are spending heavily to build their own. The countries holding them have not yet used them for AI policy goals.
2. **Two ways to waste it:** never use it, or use it badly. OPEC-style threats would push the US to reshore faster, burn the leverage, or split the coalition.
3. **What we add:** a clear, checkable answer to "what can we credibly ask for?" that officials and researchers in these countries can pick up and test.
4. **What changes if it works:** the leverage buys safety outcomes before it erodes — fewer advanced chips reaching uncontrolled actors, a voice in the rules that govern compute, and frontier model access for their evaluators.
5. **Why it matters for safety:** more independent checks on frontier AI, and less unchecked concentration of compute.

**Assumptions that could break it:** the chokepoints last long enough to matter; governments can steer their firms; the US reads these asks as cooperative rather than hostile. A one-day project won't change policy on its own. Its realistic job is to be a credible first cut that people working on chip diplomacy can build on.

Sources: [Middle Powers and Transformative AI RFP](https://middlepowers.ai/) (Astralis Foundation) · [ETO Supply Chain Explorer documentation](https://eto.tech/tool-docs/chipexplorer)
