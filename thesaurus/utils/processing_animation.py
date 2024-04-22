import itertools, sys, time

def animateProcessing(done):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rprossessing request...' + c)
        sys.stdout.flush()
        time.sleep(0.1)
