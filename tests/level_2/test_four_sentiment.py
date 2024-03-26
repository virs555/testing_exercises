from functions.level_2.four_sentiment import check_tweet_sentiment

import pytest

def test__check_tweet_sentiment__return_bad_when_tweet_has_more_bad_words(bad_words):
    text = 'What beautiful weather we were having today until the fucking rain ruined it'
    good_words = ('beautiful')
    assert check_tweet_sentiment(text, good_words, bad_words) == 'BAD'

def test__check_tweet_sentiment__return_good_when_tweet_has_more_good_words(good_words, bad_words):
    text = 'What beautiful and bright weather we had today until the rain ruined it'
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'

def test__check_tweet_sentiment_return_none_when_tweet_has_equal_number_good_and_bad_words(good_words, bad_words):
    text = 'What beautiful and bright weather we had today until the fucking rain ruined it'
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__return_none_when_empty_words():
    text = 'What beautiful and bright weather we had today until the fucking rain ruined it'
    good_words = ()
    bad_words = ()
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__return_none_when_empty_text(good_words, bad_words):
    text = ''
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__return_good_when_text_is_big_and_has_more_good_words(good_words, bad_words):
    text = "beautiful " * 10000
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'
    