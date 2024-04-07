file_names = ['txt1.txt', 'txt2.txt']
with open('output-file.txt', 'w', encoding='utf-8') as output_file:
  for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
      for line in file:
        output_file.write(line)