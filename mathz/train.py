from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def main():
    # Load Dataset
    iris = load_iris()
    data, labels = iris.data, iris.target
    # 70%/30% split
    training_data, test_data, training_labels, test_labels = train_test_split(
        data, labels, test_size=0.30
    )
    # Logistics Regression Model
    model = LogisticRegression(multi_class="multinomial", max_iter=200)
    # Train Model
    model.fit(training_data, training_labels)
    # Score Model
    accuracy = model.score(test_data, test_labels)
    # Print Accuracy
    print("Accuracy: {:.2f}".format(accuracy))

    # save the model
    # pickle.dump(model, open("model.pkl", "wb"))


if __name__ == "__main__":
    main()
