# AAVE vocabulary diffusion Twitter/X's #Genz and #BlackTwitter 

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
  * Of the observed words, adjectives had the lowest use retention in #GenZ after five years 
  * Of the observed words, nouns had the highest use retention in #GenZ after five years
  * Of the observed words, verbs had the lowest use retention in #BlackTwitter after five years 
  * Of the observed words, adjectives(only slighter more than nouns) had the highest use retention in #BlackTwitter after five years
  * Across all parts of speech, #BlackTwitter usage frequencies declined
  * #GenZ frequencies of nouns and verbs grew during the five-year interval, while adjective use declined after 5 years
- Frequenices of word usages can be seen in `frequenices.csv`
## Scripts
- `unique_tweets.py`: python script created by ChatGBT to create corpuses of tweet texts from the .json files, removing duplicates and counting unique tweets
- `unique_ids.py`: - `unique_tweets.py`: python script created by ChatGBT to create corpuses of tweet ids to enable publication of tweet data extracted from the .json files while respecting twitter privacy rules

## Sources used to define AAVE and linguistic patterns
-  *Bailey, G.  (2022, August 15). The History of African-American Vernacular English. Oxford 
Research Encyclopedia of Linguistics. Retrieved 17 Mar. 2026, from 
https://oxfordre.com/linguistics/view/10.1093/acrefore/9780199384655.001.0001/acrefore-9780199384655-e-926*
- *John R. Rickford. (2003). African American Vernacular English (AAVE). In International 
Encyclopedia of Linguistics (2nd ed.). Oxford University Press.*

## Sources that could be considered for future research
- *Ilbury, C. (2020). “Sassy Queens”: Stylistic orthographic variation in Twitter and the enregisterment of AAVE. Journal of Sociolinguistics, 24(2), 245–264. https://doi.org/10.1111/josl.12366*


## Corpuses 
- In total, 32,022 tweets were collected throughout the process, but not all data was used in the statistical analysis described above
- Three corpuses of data were created from #BlackTwitter tweets, corresponding to each year that was examined (#BlackTwitter2025, #BlackTwitter2023, #BlackTwitter2025)
- Three corpuses of data were created from #GenZ, corresponding to each year that was examined (#GenZ2025, #GenZ, #GenZ)
- An additional corpus containint the tweeet IDs for data scraped for the project, that helped confirm the vocabulary term's connection to AAVE and the decision to use #GenZ over other hashtags that were considered like #StanTwt, #StanTwitter, and #tiktok.  

## Limitations
- Hashtags are imperfect indicators of community identity
not all AAVE speakers can be represented through data extracted from #BlackTwitter
- Terms were 
- Semantic filtering introduces subjectivity

## Ethical Considerations
- This project used the offical Twitter/X API to ensure that the privacy and ethical standards set by Twitter to protect its users were respected and followed.
- Tweets examined in this study were posted publicly
- To further protect the creators of the tweet's used in this study, tweet id's will be published instead of the tweet texts
- AAVE has had a longer history of stigmatization, and it is essential that viewers are careful about the conclusion they draw from this small set, whose scope is affected by the limitations outlined above

## Further research
- The main goal of this was to see if there were relationships between word usage and the outlined categories
  * The relationships between part of speech and usage need more words to lead to stronger conclusions beyond the suggestion of a relationship
  * Examining determiners, discourse markers, and other parts of speech could be helpful
- The results and patterns shown are likely to be effected by the sample population, sample size, and medium of data
- Research on broader audiences (of both AAVE and non-AAVE) with more words and more temporal points would lead to clearer, more hollistic results
  * Different age groups, identity groups, and regions of non-AAVE speakers may have differences in rates and distributions of diffused words
  + Historically, the Southern-American has had close contact with AAVE, which could affect diffusion
  + Research has found a relationship between LGBT+ online community vernacular and AAVE (see Ilbury, C)
  
## Author
Alexandra Wingo

## Acknowledgments
- I would like to thank Nancy Apollo, Maya Hay, Carys Kirlew, Carter Hoskins, Dominique Quinonez, Erika Sowah, and Israel Allen for their help during the creation of the target word list. 
