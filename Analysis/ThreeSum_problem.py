import time

from Analysis.ThreeSum_bruteForce import three_sum


def main(source):
    a = [int(i.strip()) for i in source if i]

    start = time.time()
    print(three_sum(a))
    print('Elapsed {} seconds'.format(time.time() - start))


if __name__ == "__main__":
    while True:
        choice = input('What do you want?\n'
                       '[1] Test\n'
                       '[2] Execute from cli\n'
                       '[3] Execute from file\n'
                       '[4] Quit\n'
                       'Choose: ')
        if choice == '1':
            main('30 -40 -20 -10 40 0 10 5'.split())
            test_files = '1Kints.txt', '2Kints.txt', '4Kints.txt', '8Kints.txt'
            for file in test_files:
                print('\nProcessing {} file...'.format(file))
                main(open(file).readlines())
        elif choice == '2':
            main(input('Enter values delimited by spaces: ').split())
        elif choice == '3':
            main(open(input('Enter file name: ')).readlines())
        elif choice == '4':
            print('Bye')
            break
