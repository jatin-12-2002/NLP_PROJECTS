from rouge import rouge_score
import en_core_web_sm


def accuracy_sentences(predicted_sentence, reference_sentence):


    nlp = en_core_web_sm.load()
    accuracy_dict ={}
    for i in range(0, len(predicted_sentence)):
        templist1 = []
        templist2 = []
        doc1 = nlp(reference_sentence[i].lower())
        doc2 = nlp(predicted_sentence[i].lower())
        for token in doc1:
            templist1.append(str(token))
        for token in doc2:
            templist2.append(str(token))
        scoren1 = rouge_score.rouge_n(templist2, templist1, n=1)
        scoren2 = rouge_score.rouge_n(templist2, templist1, n=2)
        if 'score_n1' not in accuracy_dict.keys():
            templist1 = []
            templist1.append(scoren1)
            accuracy_dict['score_n1'] = templist1
        else:
            accuracy_dict['score_n1'].append(scoren1)
        if 'score_n2' not in accuracy_dict.keys():
             templist2 = []
             templist2.append(scoren2)
             accuracy_dict['score_n2'] = templist2
        else:
            accuracy_dict['score_n2'].append(scoren2)
    return accuracy_dict
