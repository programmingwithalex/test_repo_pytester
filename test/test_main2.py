import main2


def test_sub():
    assert main2.sub(3, 4) == -1
    assert main2.sub(4.5, 4) == 0
    assert main2.sub(3.9, 4) == -1
    assert main2.sub(4.2, 3.8) == 0


def test_word_count():
    assert main2.word_count('arm pod race', 'pod') == 1
    assert main2.word_count('arm pod race', 'lap') == 0
    assert main2.word_count('arm arm arm', 'arm') == 3

