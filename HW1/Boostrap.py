#Bootstrap test
import scipy as sp
import scipy.stats

def get_confidence_interval(data):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+0.95)/2., n-1)
    return m, m-h, m+h

def bootstrap(option):
    diff_array = []
    num_samples = 5000
    out_of_bounds = 0
    _,_,_,_,_,_,_,_,_,_,ap_total,err_total,ndcg_total = check_performance(combinations,False)
    ap_total_flat = ap_total
    err_total_flat = err_total
    ndcg_total_flat = ndcg_total

    assert (len(ap_total_flat) == len(err_total_flat) == len(ndcg_total_flat))

    ap_winner = []
    err_winner = []
    ndcg_winner = []

    for item in ap_total_flat:
        if item > 0:
            ap_winner.append(1)
        elif item < 0:
            ap_winner.append(0)
        else:
            ap_winner.append(0.5)

    for item in err_total_flat:
        if item > 0:
            err_winner.append(1)
        elif item < 0:
            err_winner.append(0)
        else:
            err_winner.append(0.5)

    for item in ndcg_total_flat:

        if item > 0:
            ndcg_winner.append(1)
        elif item < 0:
            ndcg_winner.append(0)
        else:
            ndcg_winner.append(0.5)
    actual_diff = [x1 - x2 for (x1, x2) in zip(ap_winner, err_winner)]
    actual_mean,lower,higher = get_confidence_interval(actual_diff)

    for i in range(0,num_samples):
        ap_total = []
        err_total = []
        ndcg_total = []
        ap = []
        err = []
        ndcg = []
        a = np.random.randint(0,len(combinations)-10)
        combinations_check = combinations[a:a+10]
        _,_,_,_,_,_,_,_,_,_,ap_total,err_total,ndcg_total = check_performance(combinations_check,False)

        assert (len(ap_total) == len(err_total) == len(ndcg_total))

        ap_winner = []
        err_winner = []
        ndcg_winner = []

        for item in ap_total:
            if item > 0:
                ap_winner.append(1)
            elif item < 0:
                ap_winner.append(0)
            else:
                ap_winner.append(0.5)

        for item in err_total:
            if item > 0:
                err_winner.append(1)
            elif item < 0:
                err_winner.append(0)
            else:
                err_winner.append(0.5)

        for item in ndcg_total:
            if item > 0:
                ndcg_winner.append(1)
            elif item < 0:
                ndcg_winner.append(0)
            else:
                ndcg_winner.append(0.5)

        if option == 1:
            diff = np.mean(ndcg_winner) - np.mean(err_winner)
            diff_array.append(diff)
        if option == 2:
            diff = np.mean(ap_winner) - np.mean(err_winner)
            diff_array.append(diff)
        if option == 1:
            diff = np.mean(ap_winner) - np.mean(ndcg_winner)
            diff_array.append(diff)

    for element in diff_array:
        if np.mean(element) < lower or np.mean(element) > higher:
            out_of_bounds += 1

    return out_of_bounds/len(diff_array)


bootstrap(1)
bootstrap(2)
bootstrap(3)
