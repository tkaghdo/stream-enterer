## 2. Csvstack ##

~$ head -10 Combined_hud.csv

## 3. Csvlook ##

~$ head -10 Combined_hud.csv | csvlook

## 4. Csvcut ##

~$ csvcut -c 2 Combined_hud.csv | head -10

## 5. Csvstat ##

~$ csvstat Combined_hud.csv --mean

## 6. Csvcut | csvstat ##

~$ csvcut -c 2 Combined_hud.csv | csvstat

## 7. Csvgrep ##

~$ csvgrep -c 2 -m -9 Combined_hud.csv | head -10 | csvlook

## 8. Filtering out problematic rows ##

~$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv