def steps():
    likelihoods = {("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)}
    return(likelihoods)
def run():
    good_steps = []
    bad_steps = []
    all_steps = steps()
    for a in all_steps:
        if (a[1] >= 50):
             bad_steps.append(a)
        else:
            good_steps.append(a)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
run()