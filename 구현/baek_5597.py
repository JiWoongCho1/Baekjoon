num_list = [i for i in range(1, 31)]
submit_list = []
for _ in range(28):
    submit = int(input())
    submit_list.append(submit)

sub = set(num_list) - set(submit_list)
sub = list(sub)
sub.sort()

for i in sub:
    print(i)