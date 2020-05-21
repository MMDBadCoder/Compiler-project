import re

def get_tokens(content):
    from LexicalAnalyser.tokens import undefined_token
    from  LexicalAnalyser.tokens import comment_token
    matched_tokens = []
    while content.__len__() > 0:
        content = remove_whitespaces_from_first(content)

        if content == '':
            break

        new_matched_token = get_first_matched_token(content)
        if new_matched_token['token'] is not comment_token:
            matched_tokens.append(new_matched_token)
        if new_matched_token['token'] is undefined_token:
            break

        matched_content = new_matched_token['matched_content']
        content = content[matched_content.__len__():]

    return matched_tokens


def get_first_matched_token(content):
    from LexicalAnalyser.tokens import tokens, undefined_token
    from LexicalAnalyser.configs import debug_char_length

    max_matched_length = -1
    matched = None

    for token in tokens:
        matched_token = token['token']
        pattern = '^' + token['pattern']
        search_node = re.search(pattern, content)
        if search_node is not None:
            matched_content = search_node.group()
            matched_length = matched_content.__len__()
            if matched_length > max_matched_length:
                max_matched_length = matched_length
                matched = {
                    'token': matched_token,
                    'matched_content': matched_content
                }

    if matched is None:
        return {
            'matched_content': '',
            'token': undefined_token
        }
    return matched


def remove_whitespaces_from_first(content):
    content = re.sub('^\s*', '', content)
    return content
