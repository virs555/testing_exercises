from functions.level_2.one_pr_url import is_github_pull_request_url

import pytest

@pytest.mark.parametrize(('url', 'expected'), [
    ('https://github.com/virs555/testing_exercises/pull/1', True),
    ('https://github.com/virs555/testing_exercises/pull/2', True),
    ('https://github.com/virs555/testing_exercises/pull/3', True),
])
def test__is_github_pull_request_url__return_true_for_correct_url(url, expected):
    assert is_github_pull_request_url(url) is True

@pytest.mark.xfail(reason='need to return True')
def test__is_github_pull_request_url__return_true_with_slash_end():
    assert is_github_pull_request_url('https://github.com/virs555/testing_exercises/pull/1/') is True

def test__is_github_pull_request_url__return_true_when_request_url_rejects_subfolder_pr_links():
    assert is_github_pull_request_url('https://github.com/virs555/lesson1/testing_exercises/pull/1/') is False

def test__is_github_pull_request_url__return_false_when_host_not_githubcom():
    assert is_github_pull_request_url('https://gethub.com/virs555/testing_exercises/pull/1') is False

def test__is_github_pull_request_url__return_false_when_random_string():
    assert is_github_pull_request_url('adfadfasdfasdfasdfasdf') is False


