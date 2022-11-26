https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import sys
from perceptron_pos_tagger import Perceptron_POS_Tagger
from data_structures import Sentence


def read_in_gold_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [[tup.split('_') for tup in line.split()] for line in lines]
        sents = [Sentence(line) for line in lines]

    return sents 


def read_in_plain_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        sents = [Sentence(line) for line in lines]

    return sents 


def output_auto_data(auto_data):
    ''' According to the data structure you used for "auto_data",
        write code here to output your auto tagged data into a file,
        using the same format as the provided gold data (i.e. word_pos word_pos ...). 
    '''
    return


if __name__ == '__main__':

    # Run python train_test_tagger.py train/ptb_02-21.tagged dev/ptb_22.tagged dev/ptb_22.snt test/ptb_23.snt to train & test your tagger
    train_file = sys.argv[1]
    gold_dev_file = sys.argv[2]
    plain_dev_file = sys.argv[3]
    test_file = sys.argv[4]

    # Read in data
    train_data = read_in_gold_data(train_file)
    gold_dev_data = read_in_gold_data(gold_dev_file)
    plain_dev_data = read_in_plain_data(plain_dev_file)
    test_data = read_in_plain_data(test_file)

    # Train your tagger
    my_tagger = Perceptron_POS_Tagger()
    my_tagger.train(train_data, gold_dev_data)

    # Apply your tagger on dev & test data
    auto_dev_data = my_tagger.tag(plain_dev_data)
    auto_test_data = my_tagger.tag(test_data)

    # Outpur your auto tagged data
    output_auto_data(auto_dev_data)
    output_auto_data(auto_test_data)
