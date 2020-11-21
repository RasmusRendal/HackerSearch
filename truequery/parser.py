from truequery import Query, Subject
from .keyword_finder import is_keyword

def parse(query_string):
    """Given a string, it returns a Query object.
    This is the main entrypoint of the application"""
    query = Query()
    query.full_text = query_string
    for w in query_string.split():
        if ":" in w:
            key, value = w.split(":")
            if key == "kw":
                query.keywords.append(value)
            if key == "sjt":
                if value == "programming":
                    query.subject = Subject.PROGRAMMING
        else:
            if is_keyword(w):
                query.keywords.append(w)
            else:
                if len(query.text) > 0:
                    query.text += " "
                query.text += w
    return query
