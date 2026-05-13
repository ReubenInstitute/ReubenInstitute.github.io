# Reading Cycles: A Mathematically Defined Approach

Traditional methods for dividing the Psalms often result in highly unbalanced daily readings, which can be impractical for consistent engagement. The reading cycles developed by the Institute were designed to provide a more balanced and accessible structure, moving beyond arbitrary divisions to establish uniquely determined and universally verifiable systems.

Each cycle formulates the division of Psalms as a precise mathematical optimization problem. The problem's clear objective and explicit constraints serve as its “source code,” ensuring that its solution is unique. Modern computational capabilities, including advanced Language Models, can consistently generate the exact same optimal reading schedule from this defined problem.

The strength of the cycles lies in their transparent, constraint‑based definition. If one agrees with the underlying constraints and objectives of the mathematical problem, the resulting schedule is the only possible solution. This transparency also allows for modification of the constraints to generate custom schedules, reflecting an “open‑source” approach where the definition of the problem is paramount.

### Traditional Cycle

The traditional monthly reading cycle divides the 150 Psalms into 30 daily portions, corresponding to the days of the month. This division follows a simple numerical sequence — Psalms 1‑9 on day 1, 10‑17 on day 2, and so on — without regard to the length or structure of the text.

The result is a highly unbalanced schedule. Some days contain only a few short psalms and can be read in a couple of minutes, while others consist of a single enormous psalm — most notably Psalm 119 on day 13, which alone is longer than many entire weekly portions. A reader following this cycle experiences wildly inconsistent daily commitments, which can discourage regular engagement.

The Institute’s reading cycles address this imbalance by treating the schedule as a formal optimization problem, with explicit constraints and a chosen objective — either equalising the number of letters, the total audio duration, or a combination of both — to produce a more balanced and practical daily rhythm.

### 4 Week Cycle (letter count based)

The Four‑Week Letter‑Count Cycle balances daily reading loads using the precise number of letters in each psalm. It follows the traditional liturgical week with a double portion on Shabbat, allowing Psalm 119 to fit naturally without being split.

#### Problem

> The goal is to divide the 150 Psalms, with their precise verse letter-lengths, into 28 daily readings to minimize the maximum difference in total letter-length between any two readings, subject to the following constraints:
>
> *   Psalms must be sequenced by cycling through the five traditional books.
> *   Readings must start with Psalm 1 and end with Psalm 150.
> *   Shabbat readings must be double the length of standard weekday readings.
> *   Psalm 119 must be in a Shabbat reading.
> *   Daily readings are limited to 9 psalms for weekdays and 16 for Shabbat.

#### Schedule

| Week | Day | Psalms |
| :--- | :--- | :--- |
| First Week | Sunday | 1, 18, 49 |
|  | Monday | 78, 93 |
|  | Tuesday | 37, 107 |
|  | Wednesday | 68, 73, 97 |
|  | Thursday | 22, 65, 109 |
|  | Friday | 89, 102, 117 |
|  | Shabbat | 35, 69, 74, 106, 147 |
| Second Week | Sunday | 40, 44, 77, 100, 134 |
|  | Monday | 38, 71, 88, 101 |
|  | Tuesday | 9, 55, 82, 139 |
|  | Wednesday | 27, 105, 118 |
|  | Thursday | 50, 80, 104 |
|  | Friday | 34, 59, 84, 136 |
|  | Shabbat | 103, 119 |
| Third Week | Sunday | 25, 51, 86, 90 |
|  | Monday | 10, 45, 79, 145 |
|  | Tuesday | 33, 66, 94, 135 |
|  | Wednesday | 17, 52, 83, 92, 144 |
|  | Thursday | 7, 57, 81, 91, 132 |
|  | Friday | 39, 72, 85, 96, 116 |
|  | Shabbat | 19, 41, 42, 56, 75, 76, 87, 95, 98, 99, 115, 131, 143 |
| Fourth Week | Sunday | 5, 32, 48, 60, 110, 140 |
|  | Monday | 21, 31, 58, 62, 141, 148 |
|  | Tuesday | 15, 30, 36, 46, 63, 108, 137 |
|  | Wednesday | 2, 4, 47, 53, 64, 112, 128, 146 |
|  | Thursday | 16, 26, 28, 43, 54, 61, 111, 142 |
|  | Friday | 6, 8, 24, 67, 70, 122, 126, 138, 149 |
|  | Shabbat | 3, 11, 12, 13, 14, 20, 23, 29, 113, 114, 124, 125, 127, 129, 130, 150 |

## Duration based cycles

Audio duration based cycles share a common data file, durations.csv, which lists every unit together with its duration in seconds, Psalms 1–150 (with Psalm 119 split into its 22 individual stanzas, named 119.1 through 119.22).

[durations.csv](durations.csv)


### 4 Week Cycle

This is the same problem as the letter‑count cycle, with the single difference that the weight of each psalm is taken from `durations.csv` rather than from its letter count. The objective remains to minimise the maximum difference in total audio duration between any two days, under the identical constraints (book‑cycling, Shabbat double length, Psalm 119 unsplit, and the 9/16 psalm‑count limits).

### 6 Week Study Cycle

The Six‑Week Study Cycle balances daily reading loads. Psalm 119 is split into two parts; Sunday–Thursday are full days, Friday is a half day, and Shabbat is a rest.

**Long psalms** (> 5 min):  
`18, 37, 68, 69, 78, 89, 105, 106`

**Medium psalms** (2½–5 min):  
`7, 9, 10, 22, 25, 27, 31, 33, 34, 35, 38, 40, 44, 45, 49, 50, 51, 55, 59, 66, 71, 72, 73, 74, 77, 80, 86, 88, 94, 102, 103, 104, 107, 109, 118, 135, 139, 145`

| Week | Sunday | Monday | Tuesday | Wednesday | Thursday | Friday |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 2 medium | 2 medium | 2 medium | 2 medium | — |
| 2 | 2 medium | 2 medium | 2 medium | long | long | — |
| 3 | 2 medium | 2 medium | 2 medium | long | long | — |
| 4 | 2 medium | 2 medium | 2 medium | long | long | — |
| 5 | 2 medium | 2 medium | 2 medium | long | long | — |
| 6 | 2 medium | 2 medium | 2 medium | 119a | 119b | 150 |

The anchor items are placed as follows: Psalm 1 opens the first Sunday, the eight long psalms occupy Wednesdays and Thursdays of weeks 2‑5 (two per week, alternating), the two halves of Psalm 119 occupy the final Wednesday and Thursday (week 6), and Psalm 150 closes the final Friday. This arrangement keeps the heaviest readings away from the beginning and end of the week, placing them instead on the mid‑week days where they can serve as the core of each week’s study. The 38 medium psalms are then distributed exactly two per day across the remaining 19 full‑day slots (Sundays, Mondays, and Tuesdays of all weeks, plus Thursday of week 1). Fridays (except for the final one) are left empty of medium or long psalms — the Institute deliberately keeps them short, using only the shorter psalms to fill a half‑day, so that each week closes gently.

#### Problem

> The goal is to fill the 36 daily slots of the table above with the 151 units from `durations.csv` (the 149 whole psalms and the two parts of Psalm 119, each a whole number of consecutive stanzas, with an initial split of 11 + 11) so as to **minimise the maximum difference in total audio duration between any two days**, subject to the following constraints:
>
> *   The twelve anchor items (Psalm 1, the eight long psalms, the two parts of Psalm 119, and Psalm 150) are fixed in the positions shown in the table.
> *   The thirty‑eight medium psalms must be assigned to the 19 slots marked “medium”, exactly two per slot.
> *   The remaining short psalms must be distributed across all slots to complete each day.
> *   Within each day, psalms must be selected by cycling through the five books (1 → 2 → 3 → 4 → 5 → 1 …), taking exactly one psalm from the current book before moving to the next.
> *   Sunday–Thursday are full days; Friday is a half day; Shabbat is empty.
