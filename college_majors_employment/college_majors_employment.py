#Author: Tamby Kaghdo

import pandas as pd


def totals_by_major_categoty(major_df):
    major_dict = {}
    # get unique major categories
    for i in major_df["Major_category"].value_counts().index:
        #create a data frame for each major category
        category_df = major_df[major_df["Major_category"] == i]
        # sum all totals for the category
        total = category_df["Total"].sum(axis=0)
        # insert totals into categories dictionary
        major_dict[i] = total
    return major_dict

def main():
    all_ages_file = "C:\\Workspace\\data\\college_majors_employment\\all-ages.csv"
    recent_grads_file = "C:\\Workspace\\data\\college_majors_employment\\recent-grads.csv"

    # import the ages file into a panda data frame
    all_ages_df = pd.read_csv(all_ages_file)
    recent_grad_df = pd.read_csv(recent_grads_file)

    all_ages_major_categories = {}
    recent_grads_major_categories = {}

    #get student totals by major catergory
    all_ages_major_categories = totals_by_major_categoty(all_ages_df)
    recent_grads_major_categories = totals_by_major_categoty(recent_grad_df)

    print(all_ages_major_categories)
    print(recent_grads_major_categories)

    #calculate the percent of recent job graduates with low paying jobs
    recent_grad_total = recent_grad_df["Total"].sum(axis=0)
    recent_grad_low_paying_jobs = recent_grad_df["Low_wage_jobs"].sum(axis=0)
    recent_grad_low_paying_jobs_percent = recent_grad_low_paying_jobs / recent_grad_total
    print(recent_grad_low_paying_jobs_percent)

    #compare all ages and recent grads data to see the difference between unemployment
    majors = recent_grad_df["Major"].value_counts().index

    recent_grads_lower_unemp_count = 0
    all_ages_lower_unemp_count = 0

    for i in majors:
        recent_major_df = recent_grad_df[recent_grad_df["Major"] == i]
        recent_grads_unemployment_total = recent_major_df["Unemployment_rate"].sum(axis=0)

        all_ages_major_df = all_ages_df[all_ages_df["Major"] == i]
        all_ages_unemployment_total = all_ages_major_df["Unemployment_rate"].sum(axis=0)

        if recent_grads_unemployment_total < all_ages_unemployment_total:
            recent_grads_lower_unemp_count += 1
        elif all_ages_unemployment_total < recent_grads_unemployment_total:
            all_ages_lower_unemp_count += 1

    print(recent_grads_lower_unemp_count)
    print(all_ages_lower_unemp_count)



if __name__ == '__main__':
    main()




