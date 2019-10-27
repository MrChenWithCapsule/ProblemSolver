import csv
import re

if __name__ == "__main__":
    problem_file = open('Problem.txt')
    data_file = open('Data.txt')
    result_file = open('Result.txt', 'w')
    checker = re.compile(r' *<.+')
    problem_list = list()
    for line in re.sub(r'<p>(.+?)</p>', r'\n\1\n', problem_file.read()).split('\n'):
        if not checker.fullmatch(line):
            problem_list.append(line)
    table = csv.DictReader(data_file)
    answer_dict = dict()
    for row in table:
        answer_dict[row['problem']] = list()
        answer_list = row['answers'].split('|')
        for correct_id in row['correctanswer'].split('|'):
            try:
                if correct_id == 'A' or correct_id == 'Y':
                    answer_dict[row['problem']].append(answer_list[0])
                elif correct_id == 'B' or correct_id == 'N':
                    answer_dict[row['problem']].append(answer_list[1])
                elif correct_id == 'C':
                    answer_dict[row['problem']].append(answer_list[2])
                elif correct_id == 'D':
                    answer_dict[row['problem']].append(answer_list[3])
            except:
                answer_dict[row['problem']].append(correct_id)
    for current_problem in problem_list:
        print(current_problem, file=result_file)
        for answer in answer_dict[current_problem]:
            print('\t', answer, file=result_file)
        print('\n', sep='', file=result_file)
