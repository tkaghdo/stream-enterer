## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags[flags["bars"] == flags["bars"].max()]["name"].iloc[0]
highest_population_country = flags[flags["population"] == flags["population"].max()]["name"].iloc[0]

## 2. Calculating probability ##

total_countries = flags.shape[0]
orange_probability = flags[flags["orange"] == 1].shape[0] / total_countries
stripe_probability = flags[flags["stripes"] > 1].shape[0] / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_flags = flags.shape[0]
red_countries = flags[flags["red"] == 1]
total_red_countries = red_countries.shape[0]
three_red = (total_red_countries / total_flags) * ((total_red_countries - 1)/ (total_flags - 1)) * ((total_red_countries - 2)/(total_flags-2))

## 5. Disjunctive probability ##

start = 1
end = 18000
pop_1 = []
pop_2 = []
for i in range(1,18000):
    if (i % 100 == 0):
        pop_1.append(i)
    if (i % 70 == 0):
        pop_2.append(i)
        
hundred_prob = len(pop_1) / 18000
seventy_prob = len(pop_2) / 18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
total_countries = flags.shape[0]
total_red_countries = flags[flags["red"] == 1].shape[0]
total_orange_countries = flags[flags["orange"] == 1].shape[0]
total_red_and_orange_countries = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0]
prob_red = total_red_countries / total_countries
prob_orange = total_orange_countries / total_countries
red_or_orange = (prob_red + prob_orange) - (total_red_and_orange_countries/total_countries)

total_stripes = flags[flags["stripes"] > 0].shape[0]
total_bars = flags[flags["bars"] > 0].shape[0]
total_stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0]
prob_stripes = total_stripes / total_countries
prob_bars = total_bars / total_countries
prob_stripes_and_bars = total_stripes_and_bars / total_countries
stripes_or_bars = (prob_stripes + prob_bars) - prob_stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
heads_or = 1 - (1/2 * 1/2 * 1/2)