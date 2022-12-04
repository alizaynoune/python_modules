
class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list)\
            or not len(coefs) or len(coefs) != len(words) or \
                not all(isinstance(v, str) for v in words) or \
                not all(isinstance(v, (int, float)) for v in coefs):
            return -1
        res = 0
        for w, c in zip(words, coefs):
            res += len(w) * c

        return res

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list)\
            or not len(coefs) or len(coefs) != len(words) or \
                not all(isinstance(v, str) for v in words) or \
                not all(isinstance(v, (int, float)) for v in coefs):
            return -1
        res = 0
        for i, w in enumerate(words):
            res += len(w) * coefs[i]
        return res

