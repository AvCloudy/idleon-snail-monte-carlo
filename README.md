Usage: idleonmonte.py \<snail level\> \<encouragement level\> \<treble notes\> 
\<target success rate\> \<number of sims\>

If no values provided, defaults to 19, 13, 10920000000, 0.8 and 1000000. 

Does a monte carlo simulation for Idleon snail upgrades at a given level, and simulates how likely you are to get an upgrade vs a reset, and 
how many attempts on average you'll need to successfully upgrade. Uses that information to figure out how many times you need to encourage the snail to reach a target percent rate (suggest 0.8 or 0.9. Use something low but non-zero to just find base chances).

Formulas derived from https://docs.google.com/spreadsheets/d/1HTlligzywM5xtN1BfPhoolynZwqFmf1h/edit?gid=1764016313#gid=1764016313 courtesy of
EternallyFrumheldt#7296 who himself derived them from Chyromyr#1448.

Absolutely ridiculous way to do this, but I wanted to test intuitive notions vs simple formulae. 
