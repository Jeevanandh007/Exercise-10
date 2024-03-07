def f10(input_file,output_file):
  with open(input_file,'r') as file_in:
    with open(output_file,'w') as file_out:
      for line in file_in:
        factors,multiples=line.split(':')
        factors_list_str=factors.split()
        multiples_list_str=multiples.split()
        factors_list=list(map(int,factors_list_str))
        multiples_list=list(map(int,multiples_list_str))
        s=sum(i for i in multiples_list if any(i%j==0 for j in factors_list))
        file_out.write(str(s)+':'+str(line))
      file_out.write('\n')


with open('input','w') as f:
  f.write('3 5:1 2 3 4 5 6 7 8 9\n3 5:')
  for i in range(1000):
    f.write(str(i)+' ')
  f.write('\n2 3 5:1 2 3 4 5 6 7 8 9')

f10('input','output')

with open('sampleoutput','w') as f: # for comparison to actual
  f.write('23:3 5:1 2 3 4 5 6 7 8 9\n233168:3 5:')
  for i in range(1000):
    f.write(str(i)+' ')
  f.write('\n37:2 3 5:1 2 3 4 5 6 7 8 9')
