# Project 2 - Streamlit Portfolio App for Data Visualization

## Part 1

### Step 1: Choose a Dataset

- **Dataset Name:** Data Developer Salary in 2024
- **Source Link:** https://www.kaggle.com/datasets/shahzadi786/111111111111111111111
- **Number of Rows:** 16534
- **Short description (2–3 sentences):** The 2024 data developer salary dataset provides insights into the job market for Data Science related jobs. It includes variables including but not limited to first year in industry, experience level, employment type, job title, and salary. This dataset will give insight into which jobs pay the most as well as insight into how the variables listed above impact that observation.

### Step 2: Asking Better Questions (Using the 5E Data Questioning Cycle)

**Engage:** Write down 2–3 questions you personally wonder about your dataset.
  - Which Job Titles pay the most?
  - Is there a fall off between years of experience and salary?
  - What is the distribution of salaries?

**Explore:** Use a Generative AI tool to expand your questioning.
  **Write down:**
  - **Exact prompt(s)**
    >For Google Gemini 2.5 flash model - Raw CSV was uploaded in conjunction with prompt
    Analyze the dataset and information on this Kaggle page https://www.kaggle.com/datasets/shahzadi786/111111111111111111111
    Come up with a collection of exploratory questions for the data set. This is for the "explore" section of the 5E Data Questioning Cycle, as described in this class prompt: Explore: Use a Generative AI tool to expand your questioning.
    Write down:
    Exact prompt(s)
    List of AI-generated questions
    Only provide exploratory questions. Do not try to interpret them
    
  - **List of AI-generated questions**
    >1.  What is the **overall distribution of `salary_in_usd`**, and is it heavily skewed? Where do the mean, median, and mode fall within this distribution?
    >2.  How has the **median `salary_in_usd`** changed across the different **`work_year`** entries ($2020$ through $2024$)?
    >3.  What is the relationship between the categorical **`experience_level`** (EN, MI, SE, EX) and the **median `salary_in_usd`**?
    >4.  Which of the top 10 most frequent **`job_title`** entries commands the highest and lowest **median `salary_in_usd`**?
    >5.  How does the **`remote_ratio`** ($0$, $50$, $100$) influence the **median `salary_in_usd`** across all records?
    >6.  How does the **median `salary_in_usd`** compare for professionals who have a different **`employee_residence`** versus those whose **`employee_residence`** matches their **`company_location`**?
    >7.  How does **`company_size`** (S, M, L) relate to the **median `salary_in_usd`** within each **`experience_level`**?
    >8.  Are there any significant outliers or clusters of anomalies in the **`salary_in_usd`** column? If so, what are their associated **`job_title`** and **`work_year`**?
    >9.  What is the frequency distribution of **`employment_type`** (FT, PT, CT, FL) in the dataset, and what is the range of **`salary_in_usd`** for each type?
    >10. What is the geographical concentration of the data? Which countries in **`employee_residence`** and **`company_location`** account for the majority of the data points?
    >11. How does the **variance of `salary_in_usd`** differ between the three **`company_size`** categories?
    >12. What is the ratio of **`work_year`** $2024$ entries that have a **`remote_ratio`** of $100$ compared to those with a **`remote_ratio`** of $0$?
    >13. How has the popularity of specific **`job_title`** entries (e.g., "Data Scientist" vs. "AI Engineer") changed from the earliest **`work_year`** to the latest?
    >14. For the records where the **`salary_currency`** is not USD, how does the original **`salary`** distribution look compared to the converted **`salary_in_usd`** distribution?
    >15. What are the common characteristics of roles that have a **`remote_ratio`** of $50$?
    >16. Is there a consistent difference in **`salary_in_usd`** between the US and the second-most represented country, controlling for **`experience_level`**?

**Explain:** Choose two questions you wrote and two questions from the AI and explain why they matter. Write down the questions and the explanation.

*My Questions*

1. Is there a fall off between years of experience and salary?
*Why it matters:*  This matters because it shows whether extra years of experience keep increasing pay or if it levels off
2. What is the distribution of salaries?
*Why it matters:* This matters because it tells you whether most people earn around the same amount or if pay is very spread out.

*AI Questions*

1. How has the median salary_in_usd changed across the different work_year entries (2020 through 2024)?
*Why it matters:* This matters because it shows whether typical pay for these jobs is going up, down, or staying the same over time.
2. What is the ratio of work_year 2024 entries that have a remote_ratio of 100 compared to those with a remote_ratio of 0?
*Why it matters:* This matters because it shows how common fully remote jobs are compared to fully on-site jobs in the most recent year.

**Elaborate:** Decide what type of visualization could answer each question, and justify it.

- **Question1:** multiple Box plots of `salary_in_usd` by `experience_level`.
*Justification:*  a collection of box plots shows median, spread, and potential drop‑offs or plateaus in salaries as experience level changes.

- **Question2:** Histogram of `salary_in_usd`
*Justification:*  a histogram shows the distribution of salaries.

- **Question3:** Scatter plot of `salary_in_usd` by `work_year`, with median salary trend line.
*Justification:*  a scatter plot shows the relationship between salary and work year, and a trend line shows the median salary over time.
*Note:* I changed this to just a line graph once I remembered that Work Year is a categorical variable, not a continuous one.

- **Question4:**  Bar chart comparing counts for `remote_ratio = 0` and `remote_ratio = 100` in 2024.
*Justification:*  a bar chart shows very easily the amount of remote workers compared to on-site workers.

**Evaluate:** Reflect in 3–5 sentences:
- Did AI introduce questions you hadn’t thought of?
- Did it expand or shift the direction of your analysis?

The AI did expose me to knew questions, and thoughts I hadn't considered. My questions were, frankly, kind of week, but the AI questions really got me thinking. It hadn't occurred to me to look at yearly trends, or to look at remote ratios. Instead I was simply interested in what I thought would affect me. After reading through the  16 questions the AI provided, I see new avenues for how I'll layout the data for the streamlit app, as well as how I try to tell my story.