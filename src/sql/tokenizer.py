from enum import Enum


class TokenType(str, Enum):
    TK_CREATE = "CREATE"
    TK_TABLE = "TABLE"
    TK_ID = "IDENTIFIER"
    TK_LP = "("
    TK_RP = ")"

class TokenMap:
    map = {
        "CREATE": TokenType.TK_CREATE,
        "TABLE": TokenType.TK_TABLE,
        "(": TokenType.TK_LP,
        ")": TokenType.TK_RP,
    }

class Token:
    def __init__(self, type: TokenType, value: str):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token(type={self.type}, value={self.value})"

class Tokenizer:
    def __init__(self):
        pass

    def _determine_token(self, *, raw_token_string: str) -> Token:
        """Takes a character and finds the Token it maps to."""
        token_string_normalized = raw_token_string.upper()
        token_type = TokenMap.map.get(token_string_normalized)
        if token_type is None:
            token = Token(type=TokenType.TK_ID, value=token_string_normalized)
        else:
            token = Token(type=token_type, value=token_string_normalized)
        return token

    def generate_tokens(self, query: str) -> list[Token]:
        tokens: list[Token] = []
        char_pointer = 0
        curr_token = ""
        while char_pointer < len(query):
            char: str = query[char_pointer]
            if char == " ":
                if curr_token == "":
                    curr_token = ""
                    char_pointer += 1
                    continue
                token = self._determine_token(raw_token_string=curr_token)
                tokens.append(token)
                curr_token = ""
                char_pointer += 1
                continue
            if char == "(":
                if curr_token != "":
                    token = self._determine_token(raw_token_string=curr_token)
                    tokens.append(token)
                tokens.append(Token(type=TokenType.TK_LP, value="("))
                curr_token = ""
                char_pointer += 1
                continue
            if char == ")":
                if curr_token != "":
                    token = self._determine_token(raw_token_string=curr_token)
                    tokens.append(token)
                tokens.append(Token(type=TokenType.TK_RP, value=")"))
                curr_token = ""
                char_pointer += 1
                continue
            curr_token += char
            char_pointer += 1
            

        print(tokens)
        return tokens

    pass

if __name__ == "__main__":
    query = "CREATE TABLE TBLCARS ( NAME STRING )"
    tokenizer = Tokenizer()
    tokenizer.generate_tokens(query=query)
