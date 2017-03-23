# imports
from pandas import read_csv, DataFrame
from sklearn import svm, tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.utils import shuffle

# features
features_df = read_csv('./data/features.csv')

train = shuffle(features_df[0:60]).values
test = shuffle(features_df[60:90]).values

X_train = train[:, 0:-1]# feature vector
y_train = train[:, -1]	# ground truth

X_test = test[:, 0:-1]	# feature vector
y_test = test[:, -1]    # ground truth

# train
svm_clf = svm.SVC().fit(X_train, y_train)
tree_clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
lr_clf = LogisticRegression().fit(X_train, y_train)
knn_clf = KNeighborsClassifier().fit(X_train, y_train)

# test
svm_predictions = svm_clf.predict(X_test)
tree_predictions = tree_clf.predict(X_test)
lr_predictions = lr_clf.predict(X_test)
knn_predictions = knn_clf.predict(X_test)

svm_p_r = precision_recall_fscore_support( \
  y_test, svm_predictions, average='weighted')[:2]
tree_p_r = precision_recall_fscore_support( \
  y_test, tree_predictions, average='weighted')[:2]
lr_p_r = precision_recall_fscore_support( \
  y_test, lr_predictions, average='weighted')[:2]
knn_p_r = precision_recall_fscore_support( \
  y_test, knn_predictions, average='weighted')[:2]

svm_score = svm_clf.score(X_test, y_test)
tree_score = tree_clf.score(X_test, y_test)
lr_score = lr_clf.score(X_test, y_test)
knn_score = knn_clf.score(X_test, y_test)

# report metrics
results = open('results.txt', 'w')
results.write('ACCURACIES' + '\n')
results.write('SupportVectorMachine:\t' + str(svm_score) + '\n')
results.write('DecisionTree:\t\t' + str(tree_score) + '\n')
results.write('LogisticRegression:\t' + str(lr_score) + '\n')
results.write('KNearestNeighbors:\t' + str(knn_score) + '\n')
results.write('\n')

results.write('PRECISION' + '\n')
results.write('SupportVectorMachine:\t' + str(svm_p_r[0]) + '\n')
results.write('DecisionTree:\t\t' + str(tree_p_r[0]) + '\n')
results.write('LogisticRegression:\t' + str(lr_p_r[0]) + '\n')
results.write('KNearestNeighbors:\t' + str(knn_p_r[0]) + '\n')
results.write('\n')

results.write('RECALL' + '\n')
results.write('SupportVectorMachine:\t' + str(svm_p_r[1]) + '\n')
results.write('DecisionTree:\t\t' + str(tree_p_r[1]) + '\n')
results.write('LogisticRegression:\t' + str(lr_p_r[1]) + '\n')
results.write('KNearestNeighbors:\t' + str(knn_p_r[1]) + '\n')
results.write('\n')