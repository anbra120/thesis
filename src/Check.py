from src import DecisionTree, DataT, DataProcessing


##check the word count with variance
def word_count_variance(data_text, data_title):
    print("Check word count text with variance...")
    DecisionTree.above_average(data_text.amount_r, data_text.averageV)
    DecisionTree.under_average(data_text.amount_f, data_text.averageV)
    print()
    print("Check word count title with variance...")
    DecisionTree.under_average(data_title.amount_r, data_title.averageV)
    DecisionTree.above_average(data_title.amount_f, data_title.averageV)


##check the word count without variance
def word_count(data_text, data_title):
    print("Check word count text...")
    DecisionTree.above_average(data_text.amount_r, data_text.average)
    DecisionTree.under_average(data_text.amount_f, data_text.average)
    print()
    print("Check word count title...")
    DecisionTree.under_average(data_title.amount_r, data_title.average)
    DecisionTree.above_average(data_title.amount_f, data_title.average)


def adverb(data):
    adverb_r = DataProcessing.count_adverbs_rel(data.text_r, data.amount_r)
    adverb_f = DataProcessing.count_adverbs_rel(data.text_f, data.amount_f)

    adverb_average_r = DataProcessing.get_average_word(adverb_r)
    adverb_average_f = DataProcessing.get_average_word(adverb_f)
    average =(adverb_average_f + adverb_average_r ) / 2

    DecisionTree.under_average(adverb_r, average)
    DecisionTree.above_average(adverb_f, average)
