from statistics import mode

class voteClassifier:
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    
    def predict(self, features):
        votes = []
        for c in self._classifiers:
                v = c.predict(features)
                votes.append(v)

        voted = []
        for i in range(len(votes[0])):
            temp = []
            for j in range(len(self._classifiers)):
                temp.append(votes[j][i])
            voted.append(mode(temp))
        return voted