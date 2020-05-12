# -*- coding: utf-8 -*-

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    
    document = types.Document(
    content=text_content,
    type=enums.Document.Type.PLAIN_TEXT)

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document=document).document_sentiment
    
    rtn = response.score
    
    #print(u"Language of the text: {}".format(response.language))
    return rtn

if __name__== '__main__':
  content = "This school is like a jail"
  print(content)
  print(sample_analyze_sentiment(content))
  content = "this school is like shit"
  print(content)
  print(sample_analyze_sentiment(content))

  content = "this school is like garden"
  print(content)
  print(sample_analyze_sentiment(content))

  content = "this school is like paradise. This school is like a jail."
  print(content)
  print(sample_analyze_sentiment(content))

 
