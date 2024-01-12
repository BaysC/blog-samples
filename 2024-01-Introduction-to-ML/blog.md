# Beyond the Buzzwords: Demystifying Machine Learning

In a world that is inundated with data, 
introducing Machine Learning can help companies stay ahead of the curve by boosting efficiency and
improving their decision-making.

In this blog, we will dive beyond the buzzwords and explore the concepts that underpin machine learning.

Machine learning is a subfield of Artificial Intelligence (AI) that involves the development of algorithms and models.
These algorithms provide computers with the ability to learn for themselves through data, rather than being explicitly programmed.

Here, we attempt to put in a nutshell, the end-to-end process of building an ML model.

1. __Understanding the Problem__

Before anything else, make sure you have a clear definition of the expected outcome.

Some questions to ask yourself to help define a solution are as follows:
- What are you trying to model?
- Are there any ethical considerations surrounding the problem?
For example, are there any biases present in the training data?
- Can an incorrect prediction have a significant negative impact? If so, should any predictions be made?
- Training time vs prediction time? Do you need a model with a fast prediction time, but the training time is not of huge importance? An example of this could be a self-driving car.
- How important is explainability? If the model makes accurate predictions, but you are unable to explain how exactly it is doing so, does it still satisfy the aim of the problem?

The answers to all of these questions should help guide your choice of which machine learning models are suitable.


2. __Understanding the Data Available__

The phrase __"garbage in, garbage out"__ is the mantra of machine learning.

Spending time cleaning and transforming your raw data into a suitable format is a crucial step in the process.

3. __Types of Machine Learning__

Once the goal and the data available has been established, the ML models that are applicable will have been significantly narrowed down.

There are two common types of Machine Learning; _Supervised Learning_ and _Unsupervised Learning_ which work on different types of data and solve different types of challenges.

- __Supervised learning__: A model is trained on a labelled dataset, where the input data is paired with the corresponding outputs.

- __Unsupervised Learning__: A model is given unlabelled data and can uncover hidden patterns within the data.


2. __Common Algorithms__

Depending on the problem, here are a few examples of common ML techniques:

| Supervised Learning |
|---------------------|
| Linear Regression |
| Decision Trees |
| Random Forest |
| Support Vector Machines (SVM) |


| Unsupervised Learning |
|-----------------------|
| K-Means Clustering |
| Hierarchical Clustering |
| Principal Component Analysis |

3. __Model Evaluation__

Once you have selected a few candidate models, the next step is to fit them to the data and measure the performances.

One way to evaluate the performance of a model is by using __Cross-validation__. Cross-validation uses different portions of the data to test and train a model on different iterations, and the results are combined at the end, giving an idea of how well the model would perform on unseen data.

It is important in the validating and testing stage to identify whether the model is overfitting or underfitting the data. __Overfitting__ is where the model learns the training data too well (including noise in the training data), and performs poorly when generalizing to unseen data. __Underfitting__ is where a model is too simple and is unable to capture underlying patterns in the training data (for example, using a linear model when the relationship is not a linear one).

__Hyperparameter Tuning__ is an important consideration when trying to boost model performance. Each algorithm has it's own set of hyperparameters, and hyperparameter tuning involves finding the combination that optimises the model's performance.

__Finally__

Machine learning is a powerful field, and keeping up to date in the latest advancements and best practices is crucial for practitioners. Additionally, understanding the specific needs and challenges of the problem at hand is essential for selecting the most appropriate machine learning technique.


