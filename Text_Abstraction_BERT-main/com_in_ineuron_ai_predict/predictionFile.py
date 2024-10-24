import requests
import json
from collections import OrderedDict
import os
import numpy as np
import tensorflow as tf

import sys

if not 'texar_repo' in sys.path:
    sys.path += ['texar_repo']

from config import *
from model import *
from preprocess import *
from accuracyScore import accuracy_sentences

start_tokens = tf.fill([tx.utils.get_batch_size(src_input_ids)],
                       bos_token_id)
predictions = decoder(
    memory=encoder_output,
    memory_sequence_length=src_input_length,
    decoding_strategy='infer_greedy',
    beam_width=beam_width,
    alpha=alpha,
    start_tokens=start_tokens,
    end_token=eos_token_id,
    max_decoding_length=400,
    mode=tf.estimator.ModeKeys.PREDICT
)
if beam_width <= 1:
    inferred_ids = predictions[0].sample_id
else:
    # Uses the best sample by beam search
    inferred_ids = predictions['sample_id'][:, :, 0]

tokenizer = tokenization.FullTokenizer(
    vocab_file=os.path.join(bert_pretrain_dir, 'vocab.txt'),
    do_lower_case=True)

# sess = tf.Session()


def infer_single_example(sess, story, actual_summary, tokenizer):
    example = {"src_txt": story,
               "tgt_txt": actual_summary
               }
    features = convert_single_example(1, example, max_seq_length_src, max_seq_length_tgt,
                                      tokenizer)
    feed_dict = {
        src_input_ids: np.array(features.src_input_ids).reshape(1, -1),
        src_segment_ids: np.array(features.src_segment_ids).reshape(1, -1)

    }

    references, hypotheses = [], []
    fetches = {
        'inferred_ids': inferred_ids,
    }
    print("Story : ", story)
    fetches_ = sess.run(fetches, feed_dict=feed_dict)
    # print("fetches_ : ", fetches_)
    labels = np.array(features.tgt_labels).reshape(-1, 1)
    # print("labels : ", labels)
    hypotheses.extend(h.tolist() for h in fetches_['inferred_ids'])
    # print("hypotheses : ", hypotheses)
    references.extend(r.tolist() for r in labels)
    # print("references : ", references)
    hypotheses = utils.list_strip_eos(hypotheses, eos_token_id)
    # print("hypotheses : ", hypotheses)
    references = utils.list_strip_eos(references, eos_token_id)
    # print("references : ", references)
    hwords = tokenizer.convert_ids_to_tokens(hypotheses[0])
    # print("hwords : ", hwords)
    rwords = tokenizer.convert_ids_to_tokens(references[0])
    # print("rwords : ", rwords)

    hwords = tx.utils.str_join(hwords).replace(" ##", "")
    # print("hwords : ", hwords)
    rwords = tx.utils.str_join(rwords).replace(" ##", "")
    # print("rwords : ", rwords)
    print("Original", rwords)
    print("Generated", hwords)
    return hwords


storyFile = []
summaryFile = []


def results(testStoryFileName, testSummaryFileName):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    sess.run(tf.tables_initializer())
    saver.restore(sess, tf.train.latest_checkpoint(model_dir))

    if testStoryFileName is not "":
        f = open("testData/" + testStoryFileName, "r")
        for x in f:
            storyFile.append(x)
        f.close()
    if testSummaryFileName is not "":
        f = open("testData/" + testSummaryFileName, "r")
        for x in f:
            summaryFile.append(x)
        f.close()
    predictedSummary = []
    responseDict = {}
    for story in storyFile:
        # story = request.form['story']
        # summary = request.form['summary']
        predictedSummary.append(infer_single_example(sess, story, "", tokenizer))
    else:
        hwords = "Please Upload all files first before going for prediction."

    accuracy_dict = accuracy_sentences(predictedSummary, summaryFile)

    responseDict["InputStory"] = storyFile
    responseDict["PredictedSummary"] = predictedSummary
    responseDict["ActualSummary"] = summaryFile

    responseDict["AccuracyN1"] = accuracy_dict['score_n1']
    responseDict["AccuracyN2"] = accuracy_dict['score_n2']

    # data = zip(storyFile, predictedSummary, summaryFile, accuracy_dict['score_n1'], accuracy_dict['score_n2'])
    return responseDict
