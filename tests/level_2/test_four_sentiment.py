from functions.level_2.four_sentiment import check_tweet_sentiment

import pytest

def test__check_tweet_sentiment__bad_tweet_return_bad():
    text = 'What beautiful weather we were having today until the fucking rain ruined it'
    good_words = ('beautiful')
    bad_words = ('fucking', 'ruined')

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'BAD'

def test__check_tweet_sentiment__good_tweet_return_good():
    text = 'What beautiful and bright weather we had today until the rain ruined it'
    good_words = ('beautiful', 'bright')
    bad_words = ('fucking', 'ruined')

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'GOOD'

    


def test__check_tweet_sentiment__neutral_tweet_return_none():
    text = 'What beautiful and bright weather we had today until the fucking rain ruined it'
    good_words = ('beautiful', 'bright')
    bad_words = ('fucking', 'ruined')

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None

def test__check_tweet_sentiment__empty_words_return_none():
    text = 'What beautiful and bright weather we had today until the fucking rain ruined it'
    good_words = ()
    bad_words = ()

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None


def test__check_tweet_sentiment__empty_text_return_none():
    text = ''
    good_words = ('beautiful', 'bright')
    bad_words = ('fucking', 'ruined')

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None


def test__check_tweet_sentiment__big_text_return_good():
    text = "beautiful " * 10000
    good_words = ('beautiful', 'bright')
    bad_words = ('fucking', 'ruined')

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'GOOD'
    