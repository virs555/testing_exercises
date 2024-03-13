from functions.level_2.one_pr_url import is_github_pull_request_url

import pytest

def test__is_github_pull_request_url__success_return():
    assert is_github_pull_request_url('https://github.com/virs555/testing_exercises/pull/1') == True

@pytest.mark.xfail(reason='need to return True')
def test__is_github_pull_request_url__with_slash_end():
    assert is_github_pull_request_url('https://github.com/virs555/testing_exercises/pull/1/') == True

def test__is_github_pull_request_url__segments_over_seven():
    assert is_github_pull_request_url('https://github.com/virs555/lesson1/testing_exercises/pull/1/') == False

def test__is_github_pull_request_url__host_not_githubcom():
    assert is_github_pull_request_url('https://gethub.com/virs555/testing_exercises/pull/1') == False

def test__is_github_pull_request_url__six_segment_not_pull():
    assert is_github_pull_request_url('https://gethub.com/virs555/testing_exercises/pul/1') == False

def test__is_github_pull_request_url__random_string():
    assert is_github_pull_request_url('adfadfasdfasdfasdfasdf') == False

def test__is_github_pull_request_url__type_int():
    with pytest.raises(AttributeError):
        is_github_pull_request_url(7)


