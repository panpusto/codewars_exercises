# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
#
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    chars = [[s[0]]]
    for char in s[1:]:
        if chars[-1][-1].islower() and char.isupper():
            chars.append(list(char))
        else:
            chars[-1].append(char)

    return ' '.join([''.join(char) for char in chars])


print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))