# ACM Research Coding Challenge (Spring 2022)

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-S22`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uTpjeA8G).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/-DRAFT-Coding-Challenge-S22#question-one)Question One

[Binary classification](https://en.wikipedia.org/wiki/Binary_classification) is a type of classification task that labels elements of a set (i.e. dataset) into two different groups. An example of this type of classification would be identifying if people had a specific disease or not based on certain health characteristics. The dataset found in `mushrooms.csv` holds data (22 different characteristics, specifically) about different types of mushrooms, including a mushroom's cap shape, cap surface texture, cap color, bruising, odor, and more. Remember to split the data into test and training sets (you can choose your own percent split). Information about the meaning of the letters under each column can be found within the file `attributelegend.txt`.

**With the file `mushrooms.csv`, use an algorithm of your choice to classify whether a mushroom is poisonous or edible.**

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library or API you want to implement this, just document which ones you used in this README file.** Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## My solution

I started by exploring the data. First, I wanted to assess the quality of the
dataset, so I checked how many samples are edible and how many are poisonous. I
found that there is a 52:48 ratio of edible to poisonous samples. This was good
because an even split between the two classes is ideal for training a model. I
also checked for any missing data. I found that 2480 of the samples are missing
data about their stalk root. I decided to drop the entire feature and move on.
Lastly, I noticed that all the features are nominal or ordinal.

I used logistic regression to classify the mushrooms because it is effective
and the math behind it is not too sophisticated. To use this method, I needed to
create numeric columns from the categorical columns. To do this, I used
`sklearn.preprocessing.OneHotEncoder`. It turns a column of n categorical
variables into n columns where every column in a row is 0 except for one.
Each row can be thought of as a bitfield, although it is better understood in
the context of linear algebra and unit vectors. I used `OneHotEncoder` for
every feature even though some features looked ordinal to me because I wasn't
100% sure. For example, population looks ordinal but it's hard to tell which
order is correct. While using `OneHotEncoder`, I came across some issues which
were fixed after reading a Medium article\[1\]. I also heavily used the
scikit-learn documentation\[2\]. I thought about using `sklearn.decomposition`
to reduce the dimensionality of the data, but decided against it due to time
constraints. I started off with a 80:20 training to test split and kept
reducing it while checking the quality of my model. In the end, a 20:80
training to test split gave me 100% accuracy.

The first draft of my code is in `exploration.ipynb` and the final, cleaned up
draft is in `solution.py`. I would like to mention that an interesting twist to
evaluating this model is that false-negatives are much worse than
false-positives. That is, classifying an edible mushroom as poisonous is bad,
but classifying a poisonous mushroom as edible is potentially deadly.

Here are the results of calling `classification_report`:

```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00      3379
         1.0       1.00      0.99      1.00      3121

    accuracy                           1.00      6500
   macro avg       1.00      1.00      1.00      6500
weighted avg       1.00      1.00      1.00      6500
```

### References

1. <https://towardsdatascience.com/guide-to-encoding-categorical-features-using-scikit-learn-for-machine-learning-5048997a5c79>
2. <https://scikit-learn.org/stable/user_guide.html>
