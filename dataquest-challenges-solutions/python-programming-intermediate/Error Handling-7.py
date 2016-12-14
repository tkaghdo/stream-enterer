## 2. Sets ##

gender = []
for i in legislators:
    gender.append(i[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for i in legislators:
    party.append(i[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

for i in legislators:
    if i[3] == "":
        i[3] = "M"


## 5. Parsing Birth Years ##

birth_years = []
for i in legislators:
    parts = i[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float(hello)
except Exception:
    print("Error converting to float..")

## 7. Exception Instances ##

try:
    int("")
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for i in birth_years:
    try:
        i = int(i)
    except Exception:
        pass
    converted_years.append(i)

## 9. Convert Birth Years to Integers ##

for i in legislators:
    try:
        birth_year = int(i[2].split("-")[0])
    except Exception:
        birth_year = 0
    i.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for i in legislators:
    if i[7] == 0:
        i[7] = last_value
    last_value = i[7]