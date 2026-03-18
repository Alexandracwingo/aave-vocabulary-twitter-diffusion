# AAVE Diffusion on Twitter/X

## Overview
This project analyzes how African American Vernacular English (AAVE) terms spread from #BlackTwitter to broader communities like #GenZ over time (2020–2025). 

## Research Question
How do different types of AAVE words (e.g., nouns vs. verbs, structurally tied vs. not) survive as they spread beyond their originating community?

## Methodology
- Words were chosen by a group of AAVE speakers that I consulted, and will be assumed to belong to AAVE, following the intuitions of my consultants 
- Tweets were collected using the official Twitter/X API
- Queries included:
  - target word
  - hashtag community (#BlackTwitter or #GenZ)
  - year (2020, 2023, 2025)
- Retweets were excluded
- Tweets were manually filtered for correct semantic meaning
- Duplicate tweets were removed

## Key Findings
- Words tied to AAVE grammatical structures show different survival patterns than standalone slang
- Part of speech appears to influence retention across communities

## Example Data
See `data/sample_tweets.csv` for a subset of processed tweets.

## Scripts
- `extract_text.py`: extracts tweet text from JSON files
- `unique_counter.py`: removes duplicates and counts unique tweets

## Limitations
- Hashtags are imperfect indicators of community identity and not all AAVE speakers can be represented through data extracted from #BlackTwitter
- Terms were 
- API sampling may not capture all relevant tweets
- Semantic filtering introduces subjectivity

## Author
Alexandra Wingo
