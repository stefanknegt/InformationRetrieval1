from subprocess import Popen, PIPE
process = Popen(['cd trec_eval','./trec_eval -m map -m P.5 -m ndcg -m recall.1000 qrel_test JelinekMercer.run'],stdout = PIPE, shell=True)
line = process.stdout.readline()
print (line)
