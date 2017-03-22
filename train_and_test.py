# imports
from sklearn import svm, tree
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv, DataFrame

# features
features_df = read_csv('./data/features.csv')
train_df = features_df[0:60]
test_df = features_df[60:90]

train_X = train_df[:, 0:-1]	# feature vector
train_y = train_df[:, -1]	# ground truth

test_X = test_df[:, 0:-1]	# feature vector
test_y = test_df[:, -1]		# ground truth

# train
svm_clf = svm.SVC()
svm_clf.fit(train_X, train_y)

tree_clf = tree.DecisionTreeClassifier()
tree_clf.fit(train_X, train_y)

lr_clf = LogisticRegression()
lr_clf.fit(train_X, train_y)

knn_clf = KNeighborsClassifier()
knn_clf.fit(train_X, train_y)

# test