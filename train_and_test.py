# imports
from sklearn import svm, tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv, DataFrame

# features
features_df = read_csv('./data/features.csv')
train = features_df[0:60].values
test = features_df[60:90].values

X_train = train[:, 0:-1]# feature vector
y_train = train[:, -1]	# ground truth

X_test = test[:, 0:-1]	# feature vector
y_test = test[:, -1]	# ground truth

# train
svm_clf = svm.SVC().fit(X_train, y_train)
tree_clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
lr_clf = LogisticRegression().fit(X_train, y_train)
knn_clf = KNeighborsClassifier().fit(X_train, y_train)

# test
svm_score = svm_clf.score(X_test, y_test)
tree_score = tree_clf.score(X_test, y_test)
lr_score = lr_clf.score(X_test, y_test)
knn_score = knn_clf.score(X_test, y_test)

# report accuracies
print('ACCURACIES')
print('SupportVectorMachine:\t' + str(svm_score * 100) + '%')
print('DecisionTree:\t\t' + str(tree_score * 100) + '%')
print('LogisticRegression:\t' + str(lr_score * 100) + '%')
print('KNearestNeighbors:\t' + str(knn_score * 100) + '%')