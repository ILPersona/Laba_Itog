def greet(name):
    return f"Привет, {name}!"


def is_even(n):
    return n % 2 == 0


def max_of_three(a, b, c):
    return max(a, b, c)


def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result


def count_vowels(s):
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count


def split_even_odd(nums):
    even = []
    odd = []
    for x in nums:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd


def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total


def is_palindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]


def multiply(*args):
    result = 1
    for x in args:
        result *= x
    return result


def build_user_profile(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, bool) and not key.startswith("is_"):
            result["is_" + key] = value
        else:
            result[key] = value
    return result


def student_email(user):
    return f"{user}@uni.ru"


def is_freezing(C):
    return C < 0


def to_minutes(hours, minutes):
    return hours * 60 + minutes


def drop_first(t):
    return t[1:]


def count_spaces(s):
    count = 0
    for ch in s:
        if ch == " ":
            count += 1
    return count


def split_pass_fail(grades):
    passed = []
    failed = []
    for g in grades:
        if g >= 3:
            passed.append(g)
        else:
            failed.append(g)
    return passed, failed


def max_in_list(nums):
    if len(nums) == 0:
        return None
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best


def is_yes(s):
    return s.strip().lower() in ("да", "yes")


def longest(*args):
    result = ""
    for s in args:
        if len(s) > len(result):
            result = s
    return result


def head_and_len(t):
    if len(t) == 0:
        return None
    return t[0], len(t)


def stars(n):
    return "*" * n


def is_working_hour(h):
    return 9 <= h <= 18


def first_in_alphabet(a, b):
    if b < a:
        return b
    return a


def first_word(s):
    words = s.split()
    if len(words) == 0:
        return ""
    return words[0]


def long_words(words):
    result = []
    for w in words:
        if len(w) >= 4:
            result.append(w)
    return result


def plus_one(nums):
    result = []
    for n in nums:
        result.append(n + 1)
    return result


def last_digit(n):
    return n % 10


def make_path(parts):
    return "/".join(parts)


def can_be_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b


def without_last(s):
    return s[:-1]


def test_greet():
    assert greet("Анна") == "Привет, Анна!"
    assert greet("Мир") == "Привет, Мир!"


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(3, 2, 1) == 3
    assert max_of_three(2, 3, 1) == 3
    assert max_of_three(5, 5, 5) == 5


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abcde") == "edcba"
    assert reverse_string("") == ""


def test_count_vowels():
    assert count_vowels("Привет") == 2
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("т") == 0


def test_split_even_odd():
    assert split_even_odd([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])
    assert split_even_odd([]) == ([], [])
    assert split_even_odd([2, 4]) == ([2, 4], [])
    assert split_even_odd([1, 3]) == ([], [1, 3])


def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([-1, 1, -2, 2]) == 0
    assert sum_list([]) == 0


def test_is_palindrome():
    assert is_palindrome("Аргентина манит негра") is True
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True


def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(10, 2) == 20
    assert multiply() == 1
    assert multiply(5) == 5


def test_build_user_profile():
    profile = build_user_profile(name="Иван", active=True, admin=False, age=30)
    assert profile == {
        "name": "Иван",
        "is_active": True,
        "is_admin": False,
        "age": 30,
    }
    assert build_user_profile(is_active=True) == {"is_active": True}


def test_student_email():
    assert student_email("ivan") == "ivan@uni.ru"
    assert student_email("anna") == "anna@uni.ru"


def test_is_freezing():
    assert is_freezing(-1) is True
    assert is_freezing(0) is False
    assert is_freezing(5) is False


def test_to_minutes():
    assert to_minutes(2, 30) == 150
    assert to_minutes(0, 45) == 45
    assert to_minutes(1, 0) == 60


def test_drop_first():
    assert drop_first((10, 20, 30)) == (20, 30)
    assert drop_first((7,)) == ()
    assert drop_first(()) == ()


def test_count_spaces():
    assert count_spaces("а б в") == 2
    assert count_spaces("нет") == 0
    assert count_spaces("  ") == 2
    assert count_spaces("") == 0


def test_split_pass_fail():
    assert split_pass_fail([5, 2, 3, 4]) == ([5, 3, 4], [2])
    assert split_pass_fail([]) == ([], [])
    assert split_pass_fail([5, 4]) == ([5, 4], [])
    assert split_pass_fail([2, 1]) == ([], [2, 1])


def test_max_in_list():
    assert max_in_list([1, 7, 3]) == 7
    assert max_in_list([-5, -1, -9]) == -1
    assert max_in_list([4]) == 4
    assert max_in_list([]) is None


def test_is_yes():
    assert is_yes("ДА") is True
    assert is_yes("  yes ") is True
    assert is_yes("да") is True
    assert is_yes("нет") is False
    assert is_yes("") is False


def test_longest():
    assert longest("кот", "собака", "я") == "собака"
    assert longest("мир", "дом") == "мир"
    assert longest("ок") == "ок"
    assert longest() == ""


def test_head_and_len():
    assert head_and_len((7, 8, 9)) == (7, 3)
    assert head_and_len((7,)) == (7, 1)
    assert head_and_len(()) is None


def test_stars():
    assert stars(3) == "***"
    assert stars(1) == "*"
    assert stars(0) == ""


def test_is_working_hour():
    assert is_working_hour(9) is True
    assert is_working_hour(18) is True
    assert is_working_hour(12) is True
    assert is_working_hour(8) is False
    assert is_working_hour(19) is False


def test_first_in_alphabet():
    assert first_in_alphabet("яблоко", "абрикос") == "абрикос"
    assert first_in_alphabet("мир", "мир") == "мир"
    assert first_in_alphabet("кот", "кит") == "кит"


def test_first_word():
    assert first_word("раз два три") == "раз"
    assert first_word("  раз два") == "раз"
    assert first_word("один") == "один"
    assert first_word("") == ""
    assert first_word("   ") == ""


def test_long_words():
    assert long_words(["кот", "рыба", "я", "стол"]) == ["рыба", "стол"]
    assert long_words([]) == []
    assert long_words(["я", "он"]) == []
    assert long_words(["зима"]) == ["зима"]


def test_plus_one():
    assert plus_one([1, -2, 0]) == [2, -1, 1]
    assert plus_one([]) == []
    assert plus_one([9]) == [10]


def test_last_digit():
    assert last_digit(123) == 3
    assert last_digit(0) == 0
    assert last_digit(100) == 0
    assert last_digit(9) == 9


def test_make_path():
    assert make_path(["home", "user", "docs"]) == "home/user/docs"
    assert make_path(["file.txt"]) == "file.txt"
    assert make_path([]) == ""


def test_can_be_triangle():
    assert can_be_triangle(3, 4, 5) is True
    assert can_be_triangle(5, 5, 5) is True
    assert can_be_triangle(1, 2, 3) is False
    assert can_be_triangle(1, 1, 10) is False


def test_without_last():
    assert without_last("кот") == "ко"
    assert without_last("я") == ""
    assert without_last("") == ""
    assert without_last("аб") == "а"


def run_tests():
    failed = []
    for name, func in list(globals().items()):
        if name.startswith("test_") and callable(func):
            try:
                func()
            except AssertionError:
                failed.append(name)
    if failed:
        print("не прошли:", ", ".join(failed))
    else:
        print("все тесты прошли")


if __name__ == "__main__":
    run_tests()
